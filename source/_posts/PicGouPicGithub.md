---
cover: 'https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307270945084.webp'
title: PicGo + uPic + Github 搭建免费图床
tags:
  - Github
  - 图床
categories: 技术
abbrlink: 1994
date: 2023-05-20 09:40:39
---

### 介绍

自从来到 xLog 就开始养成写博客的习惯，虽然 xLog 目前上传图片无限制也免费，但一直以来我使用的服务都养成了备份的习惯，也不怕跑路。对比了 Amazon S3 & Cloudflare R2，感兴趣的可以看看 [R2 vs S3](https://www.vantage.sh/blog/cloudflare-r2-aws-s3-comparison)，感觉 Cloudflare R2 性价比更高，还可以免费嫖 10 GB，但总怕背刺，我不考虑大陆 IP 访问问题，所以索性换成免费的 Github，要比稳定，谁能比过 Github？使用总之一句话："有备无患"。

### Github 图库

#### 新建仓库

注册好 Github 帐号，新建仓库，仓库名记住。

#### 新建 token

1/点击个人——“设置”

![CleanShot2023-05-20at10.35.21@2x](https://cdn.jsdelivr.net/gh/geekbb/oss_img@master/uPic/CleanShot%202023-05-20%20at%2010.35.21@2x.png)

2/左边最下面选择" <>Developer settings "

![3](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307270949561.webp)

3/选择令牌 Tokens (classic)——Generate new token (classic)

![4](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307270949172.webp)

4/备注选填，一定勾选 repo

![5](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307270949943.webp)

5/复制好 token

![6](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307270950127.webp)

以上，Github 图库仓库设置完成
***
### PicGo

#### 下载 PicGo

| 项目         | 地址                                          |
| :----------- | :-------------------------------------------- |
| PicGo Github | https://github.com/Molunerfinn/PicGo          |
| PicGo 下载   | https://github.com/Molunerfinn/PicGo/releases |


#### 设置 PicGo
打开 PicGo 设置，选择 Github 后编辑右边的配置文件

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307270951296.webp)

填入第一步记下的仓库名（格式是 userame/repo）和拷贝下来的 token，确定即可

![CleanShot2023-05-20at13.27.35@2x](https://cdn.jsdelivr.net/gh/geekbb/oss_img@master/uPic/CleanShot%202023-05-20%20at%2013.27.35@2x.png)
***
### uPic

#### 下载 uPic
| 项目              | 地址                                      |
| :---------------- | :---------------------------------------- |
| uPic&nbsp; Github | https://github.com/gee1k/uPic             |
| Homebrew          | brew install bigwig-club/brew/upic --cask |
| Github Download   | https://github.com/gee1k/uPic/releases    |

#### 配置 uPic

在设置中选择图床，左下脚 + "Github"

![CleanShot2023-05-20at13.43.20@2x](https://cdn.jsdelivr.net/gh/geekbb/oss_img@master/uPic/CleanShot%202023-05-20%20at%2013.43.20@2x.png)


> -   `用户名`: Github 用户名。例如：我的 Github 主页 [https://github.com/gee1k](https://github.com/gee1k)，我的用户名就是 `gee1k`
> -   `仓库名`: 需要储存上传文件的仓库名称。例如：我的仓库地址为 [https://github.com/gee1k/oss](https://github.com/gee1k/oss)，仓库名称就是`oss`
> -   `分支`: 分支名称，默认是`master`，如果是其他分支，就必须先创建好分支，才能上传
> -   `Token`: Github 的个人访问令牌（Personal access tokens）
> -   `域名`: 默认可不设置域名，会使用 Github 默认的访问地址。当你的仓库开启了 `pages` 功能，并配置好了自定义域名时，这里就可以使用你的自定义域名
> -    ---引用 https://blog.svend.cc/upic/tutorials/github/



保存即可

![CleanShot2023-05-20at13.44.50@2x](https://cdn.jsdelivr.net/gh/geekbb/oss_img@master/uPic/CleanShot%202023-05-20%20at%2013.44.50@2x.png)
#### jsDelivr 加速
需要 `jsdelivr` CDN 加速访问请勾选👇

链接将会变成

```
https://cdn.jsdelivr.net/gh/geekbb/oss_img@×***
```



![CleanShot2023-05-20at13.44.30@2x](https://cdn.jsdelivr.net/gh/geekbb/oss_img@master/uPic/CleanShot%202023-05-20%20at%2013.44.30@2x.png)
***
### Typora 

Typora 的配置更为简单，只要你配置好 PicGo，在 Typora 设置里选择 PicGo. app 即可

![CleanShot2023-05-20at13.55.06@2x](https://cdn.jsdelivr.net/gh/geekbb/oss_img@master/uPic/CleanShot%202023-05-20%20at%2013.55.06@2x.png)
