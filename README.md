# igeekbb blog

Hexo 博客源码分支。

## 发布流程

```bash
npm install
npx hexo clean
npx hexo generate
```

构建产物在 `public/`。线上 `main` 分支由静态站点构成，发布时需要将 `public/` 的内容提交到 `main`。

本仓库当前还启用了 Cloudflare 前端托管，`main` 的变更会触发 Cloudflare 重新拉取站点内容。
