---
cover: 'https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307270957792.webp'
title: 我把使用多年的哪吒监控换成了 ServerStatus-Rust
tags: [VPS, 监控]
categories: 技术
abbrlink: 8951
date: 2023-05-23 09:53:42
---

### 介绍
> 当使用一个东西太久，就会出现审美疲劳，[哪吒监控](https://nezha.wiki/)使用多年，倒是也没有掉过链子，搭建也方便，监控项目中规中矩，报警通知也很好配置，非常适合普通用户。不过生命在于折腾，我就喜欢不断尝试新的事物。


![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307270959977.webp)

很久以前就看中 ServerStatus 监控面板，感觉就是简洁过头，没有后台，对小白来说搭建也不是太友好，最近发现 Rust 版 ServerStatus 云探针，`ServerStatus` 威力加强版，保持轻量和简单部署，也支持显示三网 ping 值和丢包率，这样一来，也可以把部署的 smokeping 给删除了

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307282050843.avif)

### 搭建 ServerStatus-Rust

| 项目     | 主页                                     |
| :------- | :--------------------------------------- |
| Github   | https://github.com/zdz/ServerStatus-Rust |
| 说明文档 | https://doc.ssr.rs/                      |

#### 快速部署服务端 

```bash
mkdir -p /opt/ServerStatus && cd /opt/ServerStatus
```

```bash
wget --no-check-certificate -qO one-touch.sh ' https://raw.githubusercontent.com/zdz/ServerStatus-Rust/master/one-touch.sh '
bash -ex one-touch.sh
```

部署完毕，打开 http://127.0.0.1:8080/ 或 http://<你的IP>: 8080/

服务端配置文件在/opt/ServerStatus/config.toml, 可按需修改。参考：https://doc.ssr.rs/rapid_deploy/
***
#### 一键部署客户端

部署好你的 Server 后，请自行替换下面的 **`ssr.rs`** 为你的域名，我是使用 NginxProxyManager 反代了服务端 IP，顺便套上 ssl


不同的主机可以运行相同的命令注册到同一组

```bash
curl -sSLf "https://ssr.rs/i?pass=pp&gid=g1&alias=$ (hostname)" | bash
```


安装并启用 vnstat，细节参见 https://doc.ssr.rs/vnstat

```bash
curl -sSLf "https://ssr.rs/i?pass=pp&gid=g1&vnstat=1&alias=$ (hostname)" | bash
```

指定 month rotate 为 7 号

```bash
curl -sSLf "https://ssr.rs/i?pass=pp&gid=g1&vnstat=1&vnstat-mr=7&alias=$ (hostname)" | bash
```


指定位置 & 类型 (我一般用这个)

```bash
curl -sSLf "https://ssr.rs/i?pass=pp&gid=g1&alias=$ (hostname)&type=arm&loc=home" | bash
```


安装并将这台 vps 置顶显示

```bash
curl -sSLf "https://ssr.rs/i?pass=pp&gid=g1&weight=10000&alias=$ (hostname)" | bash
```


自定义 ping 地址

```bash
curl -sSLf "https://ssr.rs/i?pass=pp&gid=g1&alias=$ (hostname)&cm=cm. Abc. Com: 80" | bash
```


调试

```bash
curl -sSLf "https://ssr.rs/i?pass=pp&gid=g1&vnstat=0&alias=$ (hostname)" > ssr-client-init. Sh
Bash -x ssr-client-init. Sh
```
***
### ServerStatus 常用命令


```
# 启动
systemctl start stat_server
systemctl start stat_client

# 状态查看
systemctl status stat_server
systemctl status stat_client

# 使用以下命令开机自启
systemctl enable stat_server
systemctl enable stat_client

# 停止
systemctl stop stat_server
systemctl stop stat_client
```
![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307270959885.webp)

***
### Telegram 警告通知
https://doc.ssr.rs/notification/
```bash
# https://core.telegram.org/bots/api
# https://jinja.palletsprojects.com/en/3.0.x/templates/#if
[tgbot]
# 开关 true 打开
Enabled = false
bot_token = "<tg bot token>"
chat_id = "<chat id>"
# host 可用字段参见 payload. Rs 文件 HostStat 结构, {{host.xxx}} 为占位变量
# 例如 host. Name 可替换为 host. Alias，大家根据自己的喜好来编写通知消息
# {{ip_info.query}} 主机 ip,  {{sys_info.host_name}} 主机 hostname
title = "❗<b>Server Status</b>"
online_tpl =  " {{config.title}} \n😆 {{host.location}} {{host.name}} 主机恢复上线啦"
offline_tpl = " {{config.title}} \n😱 {{host.location}} {{host.name}} 主机已经掉线啦"

# Custom 模板置空则停用自定义告警，只保留上下线通知
Custom_tpl = """
{% if host. Memory_used / host. Memory_total > 0.5  %}
<pre>😲 {{host.name}} 主机内存使用率超 50%, 当前 {{ (100 * host.memory_used / host.memory_total) | round }} %  </pre>
{% endif %}

{% if host. Hdd_used / host. Hdd_total  > 0.5  %}
<pre>😲 {{host.name}} 主机硬盘使用率超 50%, 当前 {{ (100 * host.hdd_used / host.hdd_total) | round }} % </pre>
{% endif %}
"""
```
