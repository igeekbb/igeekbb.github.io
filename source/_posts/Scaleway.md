---
cover: 'https://cdn.jsdelivr.net/gh/geekbb/oss_img/202310061935260.webp'
title: 欧洲 Scaleway 年付 40RMB VPS IPV6 搭梯评测
categories: 技术
tags:
  - VPS
  - IPV6
abbrlink: 24626
date: 2023-10-06 19:13:09
---

`#2023年10月9日更新`

`法国巴黎1C1G10GB <融合怪测试>`

`SSH改密码登录`

### 起因

故事开始于：

- 《[Scaleway 星辰 40 元 1 年 1C1G10G 的 IPV6 小鸡](https://hupan.li/1442.html)》 
- 《[Scaleway 星辰 IPV6 小鸡的各种抠门进阶玩法](https://hupan.li/1469.html)》
- 《[Scaleway 超低价小鸡开机教程](https://www.wrnxr.cn/1945.html)》

 1C1G10G 100M 带宽 无限流量 荷兰阿姆斯特丹小鸡到手 (建议严格参考上面教程使用脚本开机)

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202310061938971.webp)

### 为 Scaleway 纯 IPV6 添加 IPV4（WARP）

- 使用 [Fscarmen/warp](https://gitlab.com/fscarmen/warp#warp-go-%E8%BF%90%E8%A1%8C%E8%84%9A%E6%9C%AC)  warp-go 脚本添加 IPV4 支持，方便访问 IPV4 内容。

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202310061953605.webp)

### 开启 BBR

- 不用折腾内核了 (我给你们避坑了)，直接开启原生 BBR (Debian 12)
- 同时适用于 ipv4/ipv6

```bash
echo "net.core.default_qdisc=fq" >> /etc/sysctl.conf
echo "net.ipv4.tcp_congestion_control=bbr" >> /etc/sysctl.conf
```

- 生效

```bash
sysctl -p
```

- 验证 (如果有 bbr 说明已开启)

```bash
sysctl net.ipv4.tcp_available_congestion_control
```

### SSH 改密码登录

```bash
#修改密码
passwd
#修改sshd_config配置文件
vim /etc/ssh/sshd_config
#找到以下选项把#去掉改成yes保存
PermitRootLogin yes
PubkeyAuthentication yes
PasswordAuthentication yes
#重启sshd
service sshd restart
```

---

### 跑分测试

#### 小鸡概况 + 国际组测速

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202310061944990.webp)

#### 国内组测速 1（荷兰）

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202310061945343.webp)

#### 国内组测速 1（法国巴黎节点）

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202310142112875.png)

#### 国内组测速 2

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202310061948128.webp)

- 这明显已超过 100M 带宽

### 搭建梯子 Vless_Reality + Hysteria2 并存

#### 八合一脚本

- 使用 [mack-a 一键脚本](https://www.v2ray-agent.com/archives/1682491479771) 5-1 【[图片参考](https://www.v2ray-agent.com/upload/wk/reality_install-nyfr.jpg)】

#### Hysteria2

- 部署 [Hysteria2](https://www.igeekbb.com/2023/09/18/hysteria/#%E9%83%A8%E7%BD%B2-Hysteria2)

### 不同协议测速

#### speed.cloudflare.com

##### vless_reality_vision

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202310062008947.webp)

##### vless_reality_grpc

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202310062009828.webp)

##### Hysteria2

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202310062010123.webp)

---

#### fast.com

##### vless_reality_vision

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202310062013055.png)

##### vless_reality_grpc

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202310062015092.webp)

##### Hysteria2

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202310062016362.webp)

#### YouTubu

##### vless_reality_grpc 和 vless_reality_vision

- 1080P 勉强观看，懒得截图了

##### Hysteria2

- 全体起立！这是 100M ?

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202310062017878.webp)

---

#### iPhone+ 小火箭全局

- 上传速度被南方联通焊死，请忽略。

##### vless_reality_grpc

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202310062052948.webp)

##### vless_reality_vision

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202310062054341.webp)

##### Hysteria2

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202310062055569.webp)

---

### 总结

- 一定要有 IPV6 环境，可参考《[不良林](https://youtu.be/dQ1AMXAiEJk?si=NPbCWG7G1ugZVfa5)》《[韩风 Talk](https://youtu.be/xj3bJRPzr8Y?si=F6koC_jMmseLEGR2)》IPV6 开通教程
- 可建梯子，vless_reality_grpc 和 vless_reality_vision 协议勉强可用，Hysteria2 直接起飞。
- Hysteria2 由于被运营商阻断或限速严重，需使用端口跳跃，可参考《[对抗 QoS 阻断&限速 Hysteria2 端口跳跃设置](https://www.igeekbb.com/2023/09/22/Hysteria2Port/)》注：需将 iptables 命令替换为 ip6tables。
- ~~IPV6 端口跳跃无法使用~~  已有大佬点拨搞定【[参考](https://github.com/apernet/hysteria/issues/629)】(Scaleway 对使用 Hysteria2/UDP 态度未知，有被封风险)
- 40RMB 一年 100M 带宽无限流量小鸡，套上 WARP 可玩性很高，确实值得折腾。我跑两个轻 Docker/备用梯子，很满足。
- 以上链接整理全了，基本上可以说是入手 Scaleway 的懒人包，折腾挂了就删机重开，大家玩得开心。

---

### 法国巴黎 1C1G10GB 测试

 短链：
    http://paste.spiritlhl.net/u/yqTG2D.txt

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202310091913245.png)

