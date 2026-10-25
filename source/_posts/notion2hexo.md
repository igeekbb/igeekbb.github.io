---
cover: 'https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307281438361.webp'
title: 从 NotionNext 转战 Hexo 博客记录
abbrlink: 14504
date: 2023-07-28 11:44:49
tags: Hexo
categories: web
---

## 起因

 Geek 以前通过 [NotionNext](https://github.com/tangly1024/NotionNext) 搭建博客，Vercel 托管，可惜 NotionNext 目前优化得还不是很好 (虽然作者很努力在更新)，随即想换一个轻博客程序。

NotionNext 的性能测试：

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307281210227.webp)



## Hexo

在众多轻博客程序，看中了 [Hexo](https://hexo.io/index.html) ，主要是 **[butterfly](https://github.com/jerryc127/hexo-theme-butterfly)** 主题一眼缘，最后选择了 **Hexo** 。作为麻瓜 (非程序员)，发奋自学三天 (中途有放弃)，基本完成了 Hexo 搭建 + 部署 Github + 图片 CDN ( jsdelivr ) + CSS 微调，达成全套白嫖，Hexo 性能也是出奇的好，很是满意！

https://pagespeed.web.dev/ 测试

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307281224753.webp)

[Google Chrome](https://www.google.com/chrome/) 

Lighthouse 桌面设备测试

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307281235917.webp)

Lighthouse 移动设备测试

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307281614284.webp)

## 关于搭建 Hexo

关于搭建中踩真是踩了不少坑，这里记录一些遇见问题后 Google，也找到一些不错的 Hexo 教程网站，分享给大家，方便今后有需要搭建 Hexo 的朋友自取。

1. ### [Hexo 官方文档](https://hexo.io/zh-cn/docs/)（推荐）

2. ### [Markdown 简单世界](https://wizardforcel.gitbooks.io/markdown-simple-world/content/0.html)（推荐）

3. ### [使用 Hexo 从 0 到 1 搭建个人博客详细教程](https://www.bmabk.com/index.php/post/82276.html)（推荐）

4. ### [Butterfly 主题安装文档](https://butterfly.js.org/)（Jerry）

   ![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307281258166.webp)

5. ### [Butterfly 主题美化教程](https://butterfly.zhheo.com/)

   ![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307281301275.webp)

6. ### [Hexo 中 Buttefly 最新教程总览 ](https://moonshuo.cn/posts/43310.html) (偷掉月亮的阿硕)

   ![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307281310713.webp)

7. ### [Butterfly 的魔改教程](https://meuicat.com/tags/Butterfly%E4%B8%BB%E9%A2%98/) （亦小封）

   ![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307281319996.webp)

8. ###  [Butterfly 主题功能介绍](https://xue65535.cn/2022/01/03/guide/Butterfly/) (一笔淡墨)

   ![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307281323656.webp)

## 域名购买

在 [Spaceship](https://www.spaceship.com/) 用促销代码 **`COM67 `** ，仅 1.79 刀购买到我心仪的 COM 域名，次年续费 8.98 刀，还能承受。

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307281326211.webp)



## 结语

在 GitHub Pages 上部署 Hexo ,本以为墙内无法访问，没想到目前也是可以正常打开，实属意外之喜，免费又稳定的方案，完美。当然如果算上域名花费，首年 12.8 元，以后 64 元/年（少喝几杯奶茶？）。

<font color=#FF000 >好了，既来之则安之，以后好好做有趣的内容输出。谢谢大家看到这里，目前未开通评论，目前我只有 [Twitter](https://x.com/geekbb)，有事可以上 X 交流。</font>
