---
cover: https://cdn.jsdelivr.net/gh/igeekbb/OSS@main/2024/202409182216498.webp
title: Debian 我的常用一键脚本
categories: [技术] 
tags: [VPS, 脚本]
date: 2024-09-18 18:56:08
---
{% quot el:h3 引言 icon:hashtag %}

{% box color:cyan %}
记录一下我最常用的 VPS 一键脚本
可能有安全隐患,仅供我个人使用.
{% endbox %}

#### 萌咖大佬一键DD脚本

```bash 更新
apt-get update
```

```bash 安装必备工具
apt-get install -y xz-utils openssl gawk file
```
```bash 全自动一键安装 debian 12
bash <(wget --no-check-certificate -qO- 'https://moeclub.org/attachment/LinuxShell/InstallNET.sh') -d 12 -v 64 -p 登录密码 -a
```
{% image https://cdn.jsdelivr.net/gh/igeekbb/OSS@main/2024/202409182005774.webp  ratio:1982/1308 %}

更多参考:https://github.com/Tasle/InstallNET

#### 一键更新系统
```bash
apt update -y && apt full-upgrade -y && apt autoremove -y && apt autoclean -y
```

```bash 查看 Debian 版本
cat /etc/debian_version
```

#### 一键安装 wget curl git
```bash
apt install sudo curl wget 
```
{% image https://cdn.jsdelivr.net/gh/igeekbb/OSS@main/2024/202409182008839.webp  ratio:1982/1308 %}

#### 一键替换最新内核 BBR (卸载内核版本)

```bash
wget -O tcp.sh "https://github.com/ylx2016/Linux-NetSpeed/raw/master/tcp.sh" && chmod +x tcp.sh && ./tcp.sh
```
{% image https://cdn.jsdelivr.net/gh/igeekbb/OSS@main/2024/202409182009299.webp  ratio:1982/1308 %}

我一般选择 BBRplus 5 -> 19
弹出提示选择 NO
{% image https://cdn.jsdelivr.net/gh/igeekbb/OSS@main/2024/202409182010178.webp  ratio:1982/1308 %}


#### 一键 IP 质量体检和解锁检测

```bash
bash <(curl -Ls IP.Check.Place)
```
{% image https://cdn.jsdelivr.net/gh/igeekbb/OSS@main/2024/202409182012209.webp  ratio:1982/2110 %}

#### 融合怪
```bash
curl -L https://gitlab.com/spiritysdx/za/-/raw/main/ecs.sh -o ecs.sh && chmod +x ecs.sh && bash ecs.sh
```
{% image https://cdn.jsdelivr.net/gh/igeekbb/OSS@main/2024/202409182013971.webp  ratio:1982/1378 %}

{% image https://cdn.jsdelivr.net/gh/igeekbb/OSS@main/2024/202409182013234.webp  ratio:1982/2110 %}



#### 科技lion脚本工具箱
```bash
bash <(curl -sL kejilion.sh)
```
{% blockquote %}
我一般选择
13 -> 2 修改登录密码
13 -> 6 修改SSH连接端口
13 -> 12 修改虚拟内存大小
13 -> 15 系统时区调整
13 -> 22 fail2banSSH防御程序
13 -> 26 修复OpenSSH高危漏洞（岫源）
{% endblockquote %}

{% image https://cdn.jsdelivr.net/gh/igeekbb/OSS@main/2024/202409182014075.webp  ratio:1982/1594 %}

参考资料 [2024年最全面VPS调优教程](https://www.youtube.com/watch?v=OR73PNaJmbk)

#### 安全设置
##### 修改 SSH 远程登录端口 22
```bash
nano /etc/ssh/sshd_config
```
{% image https://img.igeekbb.com/blog-img/2024/10/202410301417649.webp  ratio:2220/1478 %}

保存 ctrl+o + 回车，退出 ctrl+x
##### 建立非 root 的新用户
```bash
adduser vpsadmin
```
{% image https://img.igeekbb.com/blog-img/2024/10/202410301420575.gif  ratio:839/644 %}

##### 安装 sudo 功能
```bash
apt update && apt install sudo
```
##### 加入 sudo 名单
```bash
visudo
```

```bash 在 User Privilege Specification 下加入
vpsadmin ALL=(ALL) NOPASSWD: ALL
```

{% image https://img.igeekbb.com/blog-img/2024/10/202410301422496.gif  ratio:839/644 %}

##### 禁用 root 用户登录
```bash
nano /etc/ssh/sshd_config
```
找到 `PermitRootLogin Yes` 这一项，然后把它后面的设定值改为`no`即可。

##### 重启 ssh 服务
```bash
systemctl restart ssh
```
##### 快捷设置用户密码
```bash
echo "vpsadmin:new_password" | sudo chpasswd
```
##### 修改为仅允许密钥登录
```bash
sudo nano /etc/ssh/sshd_config
```
修改
PasswordAuthentication no # 不允许密码登录
PubkeyAuthentication yes# 允许密钥登录

最后执行
```bash
sudo systemctl restart sshd
```
* [参考资料](https://u2u.us.kg/cloud-security)
#### 安装 Docker
https://igeekbb.com/2023/04/20/DockerCompose/