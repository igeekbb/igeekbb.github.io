---
cover: 'https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307251500739.webp'
title: 快速获取 SSL 泛二级域名证书-acme.sh
tags:
  - 域名证书
  - SSL
categories: 技术
abbrlink: 2501
date: 2023-04-15 15:02:25
---

{% quot el:h3  使用工具 icon:hashtag %}

| 名称       | 地址                                       |
| ---------- | ------------------------------------------ |
| acme.sh    | https://github.com/acmesh-official/acme.sh |
| Cloudflare | https://www.cloudflare.com/zh-cn/          |

***


{% note color:yellow 注意事项 以下操作都是基于将域名的 NS 记录改成 Cloudlflare 的 NS，并由 Cloudflare 托管。 %}




{% quot el:h3 手动 DNS 验证方式  icon:hashtag %}

#### 一、安装 acme.sh

{% checkbox color:green checked:true 普打开 SSH 输入以下命令安装 acme.sh（注：最后<span style="color:red">Email</span>地址改成你注册 Cloudflare 的邮箱） %}

```bash
curl https://get.acme.sh | sh -s email=my@example.com
```
![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307251500740.webp)

---
#### 二、运行脚本手动验证 DNS
{% checkbox color:green checked:true 就以我 <span style="color:red">198406.xyz</span> 来申请泛二级域名 (*.198406.xyz)SSL 证书，下面代码改成你自己的域名。 %}
```bash
acme.sh --issue --dns -d "*.198406.xyz" --yes-I-know-dns-manual-mode-enough-go-ahead-please
```
![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307251500741.webp)

{% checkbox symbol:minus color:yellow checked:true <span style="color:red">记录</span>上面的 Domain 和 TXT value 的所有值（<span style="color:yellow">黄色</span>字体部分） %}


---

#### 三、Cloudflare 添加 TXT 解析

{% checkbox color:green checked:true 在 Cloudflare 管理域名添加 TXT 解析 %}

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307251500742.webp)
{% checkbox symbol:minus color:yellow checked:true 等待 1 min 生效后 %}

---

#### 四、运行申请脚本
{% checkbox color:green checked:true （记得改成你自己的<span style="color:red">域名</span>） %}
```bash
acme.sh --renew --dns -d "*.198406.xyz" --yes-I-know-dns-manual-mode-enough-go-ahead-please
```
![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307251500743.webp)

{% checkbox symbol:minus color:yellow checked:true 成功申请到*.198406.xyz 泛二级域名证书 %}

---

#### 五、域名证书安全处理

{% checkbox color:green checked:true 将 pem 域名文件保存到/root/cert/(改域名，文件目录要先建好) %}
```bash
acme.sh --install-cert -d "*.198406.xyz" \ 
--key-file       /root/cert/key.pem  \
--fullchain-file /root/cert/cert.pem \
--reloadcmd     "service nginx force-reload"
```

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307251500744.webp)

---

搞定
![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307251500745.webp)
