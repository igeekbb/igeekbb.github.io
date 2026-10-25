---
cover: 'https://cdn.jsdelivr.net/gh/geekbb/oss_img/202309291131444.webp'
title: PassWall+MosDNS 分流设置
categories: 技术
tags:
  - VPS
  - DNS
abbrlink: 55333
date: 2023-09-29 10:28:03
---

**<u>声明</u>**：这次仅仅我个人经验，因多年没有折腾 DNS，凭借以往设置 SmartDNS 的经验，加上又学习 MosDNS 插件基本设置，本着简单、高效、不易出错的原则，舍弃 MosDNS+Adgurad Home+PassWall 复杂套娃，只使用 PassWall+MosDNS 实现秒开网页和 4K  (梯子给力)。如发现有误或更好的配置，欢迎大家上推交流 [twitter](https://x.com/geekbb/status/1707617265473257628?s=20)

2023.10.6 更新：

- MosDNS 更新到 V5.2.1  https://x.com/geekbb/status/1709549373317898667?s=20, GitHub, fab fa-github fa-fw fa-lg, GitHub 

- 将国内 DNS 服务器更换为 HTTPS
- DNS 服务器并发数改为 2
- 启用 DNS 广告过滤
- PassWall 勾选 ChinaDNS-NG

### 起因

前两天我 [Twitter](https://x.com/geekbb/status/1705860118452347383?s=20) 上推荐的 OpenWrt 固件中自带有一款 DNS 插件：[MosDNS](https://github.com/haiibo/OpenWrt)，在其官方  https://github.com/IrineSistiana/mosdns, GitHub, fab fa-github fa-fw fa-lg, GitHub  上显示是 2020 年 11 月推出第一版，现在已经迭代到 v5.2.1，我发现此 DNS 转发器设置比 SmartDNS 简单太多。想到不良林这两期【[再谈 DNS 泄漏](https://youtu.be/TOhF5RcTGiM?si=OwPsyWM6pdNw54Yh)】【[进阶•DNS 泄漏篇](https://youtu.be/fqREM6b25SY?si=VswEPtSfQQKy6mZg)】，在当时并没有引起我的重视，心想泄漏就泄漏，你能把我怎么样，我们就是追求极致网速体验。现在想想确实天真了 (承德) 。既然能够通过技术避免一些不必要的麻烦，为什么不更好的保护自己呢，那下面记录一下我的设置流程。

![不良林](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202309291118344.webp)



### MosDNS 设置

#### MosDNS 基本设置 - 基本选项

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202310061858121.webp)



#### MosDNS 基本设置 - 高级选项

* 如要启用 DNS 广告过滤，记得勾选最后一项

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202310061859569.webp)



### PassWall 设置

#### PassWall DNS

* 远程 DNS 填写 `127.0.0.1:5335`

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202310061859139.webp)



### OpenWrt DHCP 设置

#### DHCP/DNS 基本设置

* 查看 DNS 转发 是否为 `127.0.0.1#5335`（以上设置好后此处会自动变更，只需要核对。）

![DHCP/DNS](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202309291137850.webp)

---

### 验证

以上设置完成后，再查询你的 DNS 泄漏[https://ipleak.net/](https://ipleak.net/ ) 和 WebRTC 泄漏[https://browserleaks.com/webrtc](https://browserleaks.com/webrtc) 如果没有中国 DNS，就基本搞定了。**这只是最初阶入门玩法，要看高阶玩法和了解原理可参考不良林的几期 DNS 讲解视频。**

![DNS](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202309292030259.webp)
