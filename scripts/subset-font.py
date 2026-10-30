#!/usr/bin/env python3
"""按站点实际用到的字符重建 LXGW WenKai Screen 子集。

背景：
  · 站点从 jsDelivr 加载 lxgw-wenkai-screen-webfont@1.7.0，97 个 woff2 分块共 5.10 MB；
    任意一页实际要拉 1.0–1.9 MB。全站用到的码位只有 ~1670 个。
  · 该包构建自源字体 v1.250.2，而 GitHub 上已找不到 v1.250 的发布包。
    因此这里把 97 个分块合并回完整字体，再从它切子集——保证与线上字形逐点相同。

用法：
  python3 scripts/subset-font.py            # 生成 scripts/fonts/lxgw-subset.woff2 + .css
  python3 scripts/subset-font.py --check    # 只校验，不写文件；有漂移则退出码 1

何时需要重跑：
  新文章里出现了此前从没出现过的字符时。--check 是发现这件事的唯一机制，
  建议放在 pre-commit 或 CI 里（不进 hexo 构建）。

依赖：首次运行会自动建 scripts/.venv 并安装 fonttools + brotli。
"""
from __future__ import annotations

import argparse
import concurrent.futures as futures
import glob
import hashlib
import json
import os
import re
import subprocess
import sys
import time
import urllib.request

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = os.path.join(REPO, "scripts", ".cache")
OUT = os.path.join(REPO, "scripts", "fonts")
VENV = os.path.join(REPO, "scripts", ".venv")

PKG = "lxgw-wenkai-screen-webfont"
VER = "1.7.0"
BASE = f"https://gcore.jsdelivr.net/npm/{PKG}@{VER}/"
# 站点 CSS 里声明的族名必须与 _config.stellar.yml 的 font_family.body 第一项一致。
CSS_FAMILY = "LXGW WenKai Screen"
# OFL 保留字体名：修改后的版本不得继续使用。
RFN_PARTS = ("霞鹜", "霞鶩")
NEW_FAMILY = "WenKai Screen Subset"
NEW_PS = "WenKaiScreenSubset"

# 站点码位之外额外保留的范围（未来的西文内容）
EXTRA_RANGES = [(0x20, 0x7E), (0xA0, 0xFF), (0x100, 0x17F)]


# ---------------------------------------------------------------- bootstrap
def ensure_venv() -> None:
    """没有 fontTools/brotli 时，建一个隔离 venv 并把当前进程搬进去。"""
    try:
        import brotli  # noqa: F401
        import fontTools  # noqa: F401
        return
    except ImportError:
        pass
    if os.environ.get("SUBSET_FONT_BOOTSTRAPPED"):
        sys.exit("venv 里仍缺 fonttools/brotli，请删除 scripts/.venv 后重试")
    if not os.path.isdir(os.path.join(VENV, "bin")):
        print(f"→ 建立 {VENV}", flush=True)
        subprocess.run([sys.executable, "-m", "venv", VENV], check=True)
        subprocess.run([os.path.join(VENV, "bin", "pip"), "-q", "install", "fonttools", "brotli"], check=True)
    env = dict(os.environ, SUBSET_FONT_BOOTSTRAPPED="1", PYTHONHASHSEED="0")
    os.execve(os.path.join(VENV, "bin", "python"), [sys.executable, __file__, *sys.argv[1:]], env)


def ensure_deterministic() -> None:
    """fontTools 内部用 set 迭代字形，哈希随机化会让产物字节每次不同。"""
    if os.environ.get("PYTHONHASHSEED") != "0":
        env = dict(os.environ, PYTHONHASHSEED="0")
        os.execve(sys.executable, [sys.executable, __file__, *sys.argv[1:]], env)



# ---------------------------------------------------------------- 站点字符集
def page_text(path: str) -> str:
    raw = open(path, encoding="utf-8", errors="replace").read()
    chunks, i, n, lower = [], 0, len(raw), raw.lower()
    while i < n:
        j = raw.find("<", i)
        if j < 0:
            chunks.append(raw[i:])
            break
        chunks.append(raw[i:j])
        k = raw.find(">", j)
        if k < 0:
            break
        tag = lower[j:k + 1]
        i = k + 1
        if tag.startswith("<script") or tag.startswith("<style"):
            close = "</script>" if tag.startswith("<script") else "</style>"
            e = lower.find(close, i)
            i = e + len(close) if e > 0 else n
    return "".join(chunks)


def site_codepoints() -> tuple[set[int], int]:
    pages = sorted(glob.glob(os.path.join(REPO, "public", "**", "*.html"), recursive=True))
    if not pages:
        sys.exit("找不到 public/**/*.html，先跑 `npx hexo generate`")
    cps: set[int] = set()
    for p in pages:
        cps |= {ord(c) for c in page_text(p)}
    return cps, len(pages)


# ---------------------------------------------------------------- 字体获取
def fetch(path: str) -> str:
    dest = os.path.join(CACHE, os.path.basename(path))
    if not os.path.exists(dest):
        with urllib.request.urlopen(BASE + path, timeout=60) as r, open(dest, "wb") as f:
            f.write(r.read())
    return dest


def load_faces() -> list[dict]:
    """解析上游 CSS，得到每个分块的 unicode-range。"""
    css = fetch("lxgwwenkaiscreen.css")
    text = open(css, encoding="utf-8").read()
    faces = []
    for part in text.split("@font-face")[1:]:
        body = part.split("}")[0]
        url = rng = None
        for line in body.splitlines():
            s = line.strip()
            if s.startswith("src:"):
                url = s.split("'")[1].lstrip("./")
            elif s.startswith("unicode-range:"):
                rng = s.split(":", 1)[1].strip()
        ranges = []
        for piece in rng.split(","):
            piece = piece.strip()[2:]
            lo, _, hi = piece.partition("-")
            ranges.append((int(lo, 16), int(hi, 16) if hi else int(lo, 16)))
        faces.append({"url": url, "ranges": ranges})
    return faces


def merged_font(faces: list[dict]) -> str:
    """把 97 个分块合并回完整字体（源 v1.250.2 已无发布包可取）。"""
    from fontTools.merge import Merger
    from fontTools.ttLib import TTFont

    dest = os.path.join(CACHE, f"merged-{VER}.woff2")
    if os.path.exists(dest):
        return dest
    with futures.ThreadPoolExecutor(8) as pool:
        paths = list(pool.map(fetch, [f["url"] for f in faces]))
    print(f"→ 合并 {len(paths)} 个分块", flush=True)
    font = Merger().merge(paths)
    version = font["name"].getDebugName(5) or ""
    if "1.250" not in version:
        sys.exit(f"上游版本变了（{version}），站点与子集的字形可能不一致，人工确认后再继续")
    font.flavor = "woff2"
    tmp = dest + ".tmp"
    font.save(tmp)
    os.replace(tmp, dest)
    return dest


# ---------------------------------------------------------------- 子集化
def rename_for_ofl(src: str, dst: str) -> None:
    """OFL 保留字体名：修改后的版本必须改名（copyright 与 RFN 声明保留）。"""
    from fontTools.ttLib import TTFont

    font = TTFont(src)
    # subsetter 保存时会把 head.modified 刷成当前时间，导致每次产物字节不同。
    font.recalcTimestamp = False
    font["head"].modified = font["head"].created
    name = font["name"]
    for rec in list(name.names):
        if rec.nameID in (1, 3, 4):
            name.setName(NEW_FAMILY if rec.nameID != 3 else f"{NEW_FAMILY}:{rec.toUnicode().split(':')[-1]}",
                         rec.nameID, rec.platformID, rec.platEncID, rec.langID)
        elif rec.nameID == 6:
            name.setName(NEW_PS, rec.nameID, rec.platformID, rec.platEncID, rec.langID)
    for rec in list(name.names):
        if rec.nameID in (1, 3, 4, 6):
            val = rec.toUnicode()
            if any(p in val for p in RFN_PARTS):
                sys.exit(f"name[{rec.nameID}] 仍含保留字体名：{val}")
    font.save(dst)


def build(target: set[int], faces: list[dict]) -> tuple[str, str]:
    os.makedirs(OUT, exist_ok=True)
    merged = merged_font(faces)

    raw = os.path.join(CACHE, "subset-raw.woff2")
    unicodes = ",".join("U+%X" % c for c in sorted(target))
    subprocess.run([
        sys.executable, "-m", "fontTools.subset", merged,
        "--unicodes=" + unicodes,
        "--flavor=woff2", "--output-file=" + raw,
        "--no-glyph-names", "--recalc-bounds",
        "--name-IDs=0,1,2,3,4,5,6",
    ], check=True)

    woff2 = os.path.join(OUT, "lxgw-subset.woff2")
    rename_for_ofl(raw, woff2)

    css = os.path.join(OUT, "lxgw-subset.css")
    with open(css, "w", encoding="utf-8") as f:
        f.write(
            "/* 由 scripts/subset-font.py 生成，不要手改。重跑条件见脚本头部。 */\n"
            "@font-face {\n"
            f"  font-family: '{CSS_FAMILY}';\n"
            "  font-style: normal;\n"
            "  font-weight: 400;\n"
            "  font-display: swap;\n"
            "  src: url('./lxgw-subset.woff2') format('woff2');\n"
            "}\n"
        )
    return woff2, css


def coverage(woff2: str, site: set[int]) -> tuple[list[int], int]:
    from fontTools.ttLib import TTFont
    cmap = set(TTFont(woff2, lazy=True).getBestCmap())
    return sorted(site - cmap), len(cmap)


# ---------------------------------------------------------------- 清单
def meta_path() -> str:
    return os.path.join(OUT, "lxgw-subset.meta.json")


def load_meta() -> dict:
    try:
        with open(meta_path(), encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def write_meta(woff2: str, site: set[int], covered: set[int], version: str) -> None:
    with open(meta_path(), "w", encoding="utf-8") as f:
        json.dump({
            "fontVersion": version,
            "bytes": os.path.getsize(woff2),
            "sha256": hashlib.sha256(open(woff2, "rb").read()).hexdigest(),
            "siteCodepoints": sorted(site),
            "coveredCodepoints": sorted(covered),
        }, f, indent=0, ensure_ascii=False)
        f.write("\n")


def show(cps: list[int]) -> str:
    return " ".join(
        f"U+{c:04X}" + (f"'{chr(c)}'" if chr(c).isprintable() and c > 0x20 else "")
        for c in cps[:40]
    )


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="只校验，有漂移则退出码 1")
    args = ap.parse_args()

    os.makedirs(CACHE, exist_ok=True)
    started = time.time()

    site, npages = site_codepoints()

    if args.check:
        return check(site, npages)

    extra = {c for lo, hi in EXTRA_RANGES for c in range(lo, hi + 1)}
    target = site | extra
    print(f"→ 页面 {npages} 个，站点码位 {len(site)}，+ 西文兜底后 {len(target)}")

    faces = load_faces()
    if len(faces) != 97:
        print(f"! 上游分块数变了：{len(faces)}（预期 97）", file=sys.stderr)

    woff2, css = build(target, faces)
    from fontTools.ttLib import TTFont
    covered = set(TTFont(woff2, lazy=True).getBestCmap())
    missing = sorted(site - covered)
    size = os.path.getsize(woff2)
    digest = hashlib.sha256(open(woff2, "rb").read()).hexdigest()[:16]
    write_meta(woff2, site, covered, f"{PKG}@{VER}")

    print(f"\n生成 {os.path.relpath(woff2, REPO)}")
    print(f"  {size:,} B  sha256:{digest}  cmap {len(covered)} 码位  用时 {time.time() - started:.0f}s")
    print(f"  {os.path.relpath(css, REPO)}")
    print(f"  {os.path.relpath(meta_path(), REPO)}")
    if missing:
        print(f"\n! {len(missing)} 个站点字符源字体本来就没有（今天也回退，行为不变）：")
        print("  " + show(missing))
    return 0


def check(site: set[int], npages: int) -> int:
    """离线、秒级：比对清单与当前 public/ 的字符集。"""
    meta = load_meta()
    woff2 = os.path.join(OUT, "lxgw-subset.woff2")
    if not meta or not os.path.exists(woff2):
        print("✗ 还没有产物，先跑一次不带 --check 的版本")
        return 1
    if hashlib.sha256(open(woff2, "rb").read()).hexdigest() != meta["sha256"]:
        print("✗ woff2 与清单的 sha256 不符（被手改过？），重新生成")
        return 1

    before = set(meta["siteCodepoints"])
    covered = set(meta["coveredCodepoints"])
    added, removed = sorted(site - before), sorted(before - site)
    uncovered = [c for c in added if c not in covered]

    print(f"→ 页面 {npages} 个，站点码位 {len(site)}（生成时 {len(before)}）")
    if removed:
        print(f"· {len(removed)} 个字符已不再出现（可重跑以缩小字体）：{show(removed)}")
    if not uncovered:
        if added:
            print(f"✓ 新增 {len(added)} 个字符，但子集已覆盖，无需重跑：{show(added)}")
        print("✓ 无漂移")
        return 0
    print(f"✗ {len(uncovered)} 个新字符不在子集里，会回退成系统字体（字体混排）：")
    print("  " + show(uncovered))
    print("  重跑：python3 scripts/subset-font.py")
    return 1



if __name__ == "__main__":
    ensure_deterministic()
    ensure_venv()
    sys.exit(main())
