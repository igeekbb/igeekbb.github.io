---
cover: 'https://cdn.jsdelivr.net/gh/geekbb/oss_img/202310182205114.webp'
title: PassWall 负载均衡 HAProxy 保姆级设置
categories: 技术
tags:
  - OpenWrt
  - 负载均衡
abbrlink: 3
date: 2023-10-18 11:32:58
---

###  关于 HAProxy

PassWall 自带了一个负载均衡 [HAProxy](http://www.haproxy.org/) 功能，以前也折腾过，现在用也就轻车熟路了，目前使用 HAProxy 需要解决我两个痛点：

- 搬瓦工 500G 流量
- UDP 阻断严重

 OpenWrt 固件推荐 [Haiibo](https://github.com/haiibo/OpenWrt) ，对于爱折腾的人来说，都有非常稳定的表现。

###  HAProxy 设置

#### 开启 HAProxy

PassWall - 【**负载均衡**】- 开启负载均衡 

- 设置用户名

- 设置密码

- 添加节点 (协议、端口、密码等尽量保持一致)
- 负载比重、模式根据自己需求设置
- 保存&应用

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202310182251012.webp)

#### 进入 HAProxy

- 保存后进入界面 & 路由地址:1188
- 密码用户名就是刚设置的

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202310182255441.webp)

- 可以看到每个节点流量情况，说明已启动成功。

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202310182256897.webp)

#### 新建**负载均衡**节点

- 【**节点列表**】新建一个【Socks 负载均衡】如图
- 地址填 OpenWrt 路由地址
- 端口 1181
- 保存

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202310182258420.webp)

#### 套用负载均衡节点

- 回到 PassWall【基本设置】
- TCP 节点选择刚刚新建的【Socks 负载均衡】
- 【Socks 配置】也要新建一个【Socks 负载均衡】节点，端口 1081
- 保存并应用即可，进入 HAProxy 能看到流量在增加。

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202310182301962.webp)

- 也可以使用 PassWall 分流功能

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202310182307843.webp)

结束

---

###  Socks 套娃新玩法

折腾好上面，我发现就一个节点也可以做 Socks 套娃的玩法，见推 https://x.com/geekbb/status/1713820323274224118?s=20 一般来说我们使用 PassWall 会直接使用节点或分流使用节点，但是如果使用本地 Socks 节点套一层梯子节点，我发现是对 UDP 流量阻断情况有所减轻的，甚至更快，大家可以设置试试：

#### 设置

- 【**节点列表**】里新建一个  Socks 套娃，如图

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202310182228436.webp)

- 【**基本设置**】-【**Socks 配置**】如图：

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202310182230011.webp)

- 在 TCP 节点中选择  [ Socks 套娃] ，下面**Socks 配置**启用，Socks 节点选择你的梯子节点即可

下面上对比图

##### 直接使用节点

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202310182237476.webp)

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202310182243826.webp)

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202310182243279.webp)

##### 使用 Socks 套娃

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202310182246766.webp)

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202310182247226.webp)

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202310182248378.webp)

玩得愉快~
