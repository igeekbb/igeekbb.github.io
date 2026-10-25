---
cover: 'https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307271009388.webp'
title: 用 Docker 将类 ChatGPT 官方服务部署到 OpenWrt 软路由
tags:
  - Docker
  - OpenWrt
  - ChatGPT
categories: AI
abbrlink: 18608
date: 2023-05-26 10:04:11
---

### 介绍

在生活和板砖奔波两地，ChatGPT 官网又经常抽风，碰巧两地都有软路由 OpenWrt，所以我将 ChatGPT 部署到软路由上。两地的网关都是 192.168.2.1，再把软路由上的 ChatGPT 加入 Google Chrome 收藏夹，这样就能随时在两地快速访问。

### 项目

这次使用的是[潘多拉 (Pandora)](https://github.com/pengzhile/pandora)，一个使用 Access Token 实现了网页版 ChatGPT 的开源项目。后端优化，绕过 Cloudflare，速度喜人。

| 项目             | 地址                                    |
| :--------------- | :-------------------------------------- |
| 潘多拉 (Pandora) | https://github.com/pengzhile/pandora    |
| Access Token     | http://chat.openai.com/api/auth/session |

`Access Token` 有效期 `14` 天，期间访问**不需要梯子**

### 部署
#### 安装 Docker
打开 OpenWrt 我使用的固件是 https://supes.top/ ，找到`系统`—`软件包`，点击更新列表

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307271009390.webp)

更新后分别安装：
1. luci-lib-jsonc

2. luci-lib-docker

3. luci-app-dockerman

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307271009391.webp)

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307271009392.webp)

安装完成后就可以在左栏找到 Docker

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307271009393.webp)

下面的操作建议在 SSH 完成，OpenWrt 上操作 Docker 真难用！

使用 SSH 工具连接 OpenWrt 网关 192.168.2.1，用户名和密码就是 OpenWrt 的用户名和密码。推荐工具  [electerm](https://github.com/electerm/electerm)

#### 拉取镜像

```bash
docker pull pengzhile/pandora
```

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307271009394.webp)

#### 运行镜像

```bash
docker run -e PANDORA_CLOUD=cloud -e PANDORA_SERVER=0.0.0.0:8899 -p 8899:8899 -d pengzhile/pandora
```

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307271009395.webp)

更多 Docker 环境变量请看： [pandora 环境变量](https://github.com/pengzhile/pandora/blob/master/doc/wiki.md#docker%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F)

#### 获取 Access Token

- 官方登录，然后访问 [这里](http://chat.openai.com/api/auth/session) 拿 `Access Token` 有效期 `14` 天

- 也可以直接用 OpenAI 帐号登录
打开 http://网关:8899/
我使用 `Access Token`
![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307271009396.webp)

搞定，使用 cloud 模式，和 ChatGPT 官网无异，聊天记录同步更新，比官网稳定快捷。

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307271009397.webp)


### 设置开机启动 (非必须)

- 使用/etc/rc.local 文件来执行自定义的启动脚本

- 找到`/etc/rc.local`文件

- 在文件的末尾添加以下内容


```bash
#!/bin/sh
/etc/init.d/dockerd restart # 重启Docker服务
sleep 10 # 等待10秒，确保Docker服务已启动 docker start my_container # 启动Docker容器
```

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307271009398.webp)

把上面的 docker start `my_container` 替换成 openwrt Docker 里的容器 ID 比如我的是 `3c3ab7807401`
docker start `3c3ab7807401`

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307271009399.webp)
- 保存并关闭文件。

授予`/etc/rc.local`文件执行权限：


```bash
chmod +x /etc/rc.local
```

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307271009400.webp)
