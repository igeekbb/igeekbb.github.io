---
cover: 'https://cdn.jsdelivr.net/gh/geekbb/oss_img/202308081333001.webp'
title: 稳定三年的斐讯 K2T 三台 KVR 组网方案
categories: [技术] 
tags: [硬件, DIY]
abbrlink: 29101
date: 2023-08-08 13:31:44
---

## 起因

早在 19 年，看了“司波图“的《[斐讯 K2T 无线路由 KVR 组网实战](https://www.youtube.com/watch?v=mfo3M1zL1Ss&t=103s&ab_channel=%E5%8F%B8%E6%B3%A2%E5%9B%BE)》，高通 Soc 方案，QCA9886 无线芯片。作为垃圾佬中的性价比之王，种草了斐讯 K2T，当时 K2T 还是矿难产品，各大二手平台充斥着物美价廉的 K2T，随即入手两台斐讯 K2T+ 新三路由器给家里组网。



![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202308081341812.webp)



## K2T 刷机

记得 2019 年购买时还是斐讯原装系统，需要自己刷 breed，也是在“[恩山论坛 K2T 版块](https://www.right.com.cn/forum/forum.php?mod=forumdisplay&fid=158&filter=typeid&typeid=19)”找到刷机教程搞定，现在购买的基本都刷好 OpenWRT 或集客 AC 了，自然也刷好了 breed。在这三年的使用中，发现新三路由器 (Newifi3) 刷集客固件组网还是没有 K2T 稳定，AP 管理时常掉线（网未断）。就在前两天刷 PDD 又看到了 K2T，价格居然降下来了，70 元入手一台，把三路由器 (Newifi3) 替换，组成 K2T 三台 KVR，爽歪歪。

### 进入 Breed

到货后直接戳住 'RESET' 孔，上电开机，breed 后台是 192.168.1.1

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202308081414052.webp)



刷入集客官网下载的固件[GECOOS_K2T_QCA956X_7.1_2022022200.bin](http://file.cnrouter.com/index.php/Index/index.html?model_id=45&device_type_id=4) （无需注册，功能解锁）

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202308081417606.webp)

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202308081956778.webp)
![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202308081956779.webp)
![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202308081956780.webp)
![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202308081956781.webp)

## 接入集客 AP

重启后自动接入部署在 Unraid 的集客网关 AC

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202308082111904.webp)

配好默认模板，接入后自动套用 

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202308082111905.webp)
![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202308082111906.webp)



## 速度测试

这里借用司波图的图

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202308081435502.webp)

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202308081448001.webp)

## 结语

斐讯 K2T 无线路由做为家宽在 500M 以内，如果喜欢折腾和追求性价比，还是非常推荐。这两台在近四年的使用中，一直稳定运行，中途一只电源坏过一次，在 PDD 单补了一个电源大概在 30 元左右，成本已经很低了。

---

就在准备发布这篇博文的时候，PDD 购买的 K2T 电源就故障了，具体表现是每个 10 分钟就重启，已申请退款😂，马上重新在淘宝以 65 元下单。所以买矿难产品就是看人品，想买到全新基本不可能，好在另外两台一直稳定了近四年，已经值票价。来吧，垃圾佬就不要怕折腾。
