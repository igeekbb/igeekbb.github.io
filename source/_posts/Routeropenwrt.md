---
cover: 'https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307271019414.webp'
title: 124 元实现最佳性价比双千兆软路由 OpenWrt
tags:
  - OpenWrt
  - 软路由
categories: 技术
abbrlink: 24592
date: 2023-05-30 10:52:31
---

> 本文所有配件均来至二手闲鱼，无任何推广成份，只是技术分享



![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307271019416.webp)

### 购入
这台我家云是我在 2020 年在闲鱼上以 85 元购得的。当时卖家已经刷好了 omv，我打算将其用作一个轻量级 NAS。随着片片越来越多，一个硬盘的 NAS 空间已经捉襟见肘，慢慢就搁置仓库。

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307271019417.webp)

没想到三年过去了，价格居然没有多大变化，相比 N1 R2S 那个炒得老高的溢价，不知道好多少倍


### 软路由需求
最近有一个使用软路由的场景需求，要求不高，我决定从仓库里拿出我家云刷成 OpenWrt, 此外，它还有一个 USB 3.0 接口，于是我在闲鱼上以 39 元收购了一个绿联 USB 千兆网卡，实现了双千兆软路由，真正的最佳性价比

总价 85+39=124 元，还要什么自行车。
### 硬件配置

CPU RK3328  eMMC 8G 的储存空间  1G 内存

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307271019418.webp)

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307271019419.webp)

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307271019420.webp)

做一个软路由足够了，平时还跑一两个 docker 也是没有问题

### 关于刷机

刷机视频在 YouTube 和 B 站有一大把，大家可以参考，只是额外需要用双 USB 公头刷机，建议大家不要单独购买 (节省成本到极致)，直接和我一样，随便找两根四芯 USB 充电线，自己接上就 OK。

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307271019421.webp)

### 固件选择

#### 高大全就选恩山论坛的 flippy  +

集成 N 多功能，USB 网卡驱动也无优

https://www.right.com.cn/forum/forum.php?mod=viewthread&tid=4076037&highlight=%E6%88%91%E5%AE%B6%E4%BA%91

电报群下载地址，我家云固件的英文叫 `L1pro`

https://t.me/openwrt_flippy

---

#### 自己制定 OpenWrt 固件 supes

https://supes.top/ 

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307271019422.webp)

需要什么功能自己选，免费只支持 5 个，不过已经够用了，集成了 https://op.supes.top/packages/aarch64_cortex-a53 软件仓库，后期可以在 OpenWrt 里面自行安装

### 后记

我家云相关介绍文章除了在恩山论坛，<什么值得买>里面也有，所以大家想了解得更详细，更多的玩法，可以搜索看看。现在它做为一个合格的过墙的软路由，性能已是绰绰有余。
![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307271019423.webp)
![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307271019424.webp)
![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307271019425.webp)
