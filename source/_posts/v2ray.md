---
cover: 'https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307270934510.webp'
title: 个人搭梯过墙备忘录
tags: [v2ray,VPS]
categories: 技术
abbrlink: 6799
date: 2023-05-14 09:35:29
---

### 搭梯过墙三步走

一台 VPS


![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307270934511.webp)

#### 重装系统 (DD)




```bash [Linux 一键网络重装系统傻瓜版](https://www.939.me/1969.html)
wget -N --no-check-certificate "https://raw.githubusercontent.com/chiakge/installNET/master/Install.sh"
chmod +x Install.sh
./Install.sh
```

- 安装 Debian11 系统 -2-3


![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307270934512.webp)

***

```bash 更新系统&一键安装 curl wget 
apt update -y  && apt upgrade -y && apt install -y curl wget sudo
```


#### 安装 BBR 网络加速脚本


```bash [最新内核 BBR 脚本卸载内核版本](https://github.com/ylx2016/Linux-NetSpeed/)
wget -O tcp.sh "https://github.com/ylx2016/Linux-NetSpeed/raw/master/tcp.sh" && chmod +x tcp.sh && ./tcp.sh
```

- 安装 BBR 原版内核 -1-11
- 安装 BBRplus 新版内核 -5-19


![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307270934513.webp)

***
#### 安装代理


```bash [VLESS (TCP_Vision、Reality、gRPC 八合一共存脚本](https://github.com/mack-a/v2ray-agent)
wget -P /root -N --no-check-certificate "https://raw.githubusercontent.com/mack-a/v2ray-agent/master/install.sh" && chmod 700 /root/install.sh && /root/install.sh
```

[八合一一键脚本，快速搭建教程](https://www.v2ray-agent.com/archives/1682491479771)

- VLESS+TLS_Vision+TCP[推荐〕
- VLESS+Realityt+uTLSt+Vision[推荐〕



2-1-07

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307270934514.webp)


***

多说无益
