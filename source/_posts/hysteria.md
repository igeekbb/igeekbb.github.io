---
cover: 'https://cdn.jsdelivr.net/gh/geekbb/oss_img/202309181955943.webp'
title: Hysteria2 & VLESS-gRPC-uTLS-REALITY 对比测试
categories: 技术
tags: VPS
abbrlink: 2601
date: 2023-09-18 19:40:33
---

### 起因

起因我在 9 月 13 日购买了 [搬瓦工 CN2 GIA 特别限量版](https://www.igeekbb.com/2023/09/14/bandwagonhost/)  年付 300 多元，香是确实香，但我没有注意月 500G 流量是双向计费，实际就是 250G，对于我来说是远远不够。随即和搬瓦工协商退款，经过几番邮件拉扯，搬瓦工表示虽然我满足 30 天内退款政策，但流量已使用超过 1/10，所以不给我退款。（上一篇评测时消耗了 100G）



![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202309181956806.webp)

### 加持 Oracle 甲骨文云

于是只能把我的真 • 传家宝 Oracle 甲骨文云日本拿出来当当备胎，鉴于甲骨文日本节点网络常年处于残废状态，完全不能使用。正好 不良林 最新一期视频 [使用 Hysteria2 歇斯底里来拯救垃圾 VPS](https://youtu.be/CXj-ID33MhU?si=7PMkMhJx__GumTre)，尝试一下看看能不能让甲骨文垃圾线路焕发第二春。

#### Oracle 甲骨文云日本→ 南方联通

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202309182008419.webp)

### 效果

部署完 Hysteria V2 后先来看一看效果：

{% checkbox checked:true 同一台 VPS(甲骨文日本) %}
{% checkbox checked:true 同一视频测速 %}
{% checkbox checked:true Hysteria2 & VLESS-gRPC-uTLS-REALITY 两种协议 %}
{% checkbox checked:true 两个时间段测试 %}

{% note color:cyan 2023年9月18日12:10测试 %}

{% quot VLESS-gRPC-uTLS-REALITY VS Hysteria2 %}

{% gallery layout:grid aspect_ratio:original size:xl %}
![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202309182018655.webp)
![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202309182018654.webp)
{% endgallery %}
---
{% note color:cyan 2023年9月18日12:1019:30晚高峰测试（十倍？？） %}


{% quot VLESS-gRPC-uTLS-REALITY VS Hysteria2 %}

{% gallery layout:grid aspect_ratio:original size:xl %}
![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202309182023452.webp)
![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202309182025229.webp)
![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202309182026782.webp)
![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202309182028601.webp)
![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202309182028676.webp)
![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202309182029055.webp)
{% endgallery %}


效果真是惊人，简直满血复活了！当搬瓦工备胎足也。

总结：有客户端条件的朋友可以直接上，垃圾线路 VPS 更是无需犹豫！

### 部署 [Hysteria2](https://v2.hysteria.network/zh/)

不良林 的视频教程已相当详细，按需操作即可

{% link https://www.youtube.com/watch?v=CXj-ID33MhU desc:true %}

下面把视频教程相关文档搬运过来方便大家



```bash 第一步 一键安装 Hysteria2
bash <(curl -fsSL https://get.hy2.sh/)
```



```bash 第二步 生成自签证书
openssl req -x509 -nodes -newkey ec:<(openssl ecparam -name prime256v1) -keyout /etc/hysteria/server.key -out /etc/hysteria/server.crt -subj "/CN=bing.com" -days 36500 && sudo chown hysteria /etc/hysteria/server.key && sudo chown hysteria /etc/hysteria/server.crt
```


```yaml 第三步 服务器配置文件
cat << EOF > /etc/hysteria/config.yaml
listen: :443 #监听端口

#使用 CA 证书
#acme:
#  domains:
#    - a.com #你的域名，需要先解析到服务器 ip
#  email: test@sharklasers.com

#使用自签证书
#tls:
#  cert: /etc/hysteria/server.crt
#  key: /etc/hysteria/server.key

auth:
  type: password
  password: 123456 #设置认证密码
  
masquerade:
  type: proxy
  proxy:
    url: https://bing.com #伪装网址
    rewriteHost: true
EOF
```



```bash 服务器相关指令
#启动Hysteria2
systemctl start hysteria-server.service
#重启Hysteria2
systemctl restart hysteria-server.service
#查看Hysteria2状态
systemctl status hysteria-server.service
#停止Hysteria2
systemctl stop hysteria-server.service
#设置开机自启
systemctl enable hysteria-server.service
#查看日志
journalctl -u hysteria-server.service
```



```bash 客户端配置文件
server: ip:443
auth: 123456

bandwidth:
  up: 20 mbps
  down: 100 mbps
  
tls:
  sni: a.com
  insecure: false #使用自签时需要改成true

socks5:
  listen: 127.0.0.1:1080
http:
  listen: 127.0.0.1:8080
```


```bash sing-box 配置文件 (Android/IOS)
{
  "dns": {
    "servers": [
      {
        "tag": "cf",
        "address": "https://1.1.1.1/dns-query"
      },
      {
        "tag": "local",
        "address": "223.5.5.5",
        "detour": "direct"
      },
      {
        "tag": "block",
        "address": "rcode://success"
      }
    ],
    "rules": [
      {
        "geosite": "category-ads-all",
        "server": "block",
        "disable_cache": true
      },
      {
        "outbound": "any",
        "server": "local"
      },
      {
        "geosite": "cn",
        "server": "local"
      }
    ],
    "strategy": "ipv4_only"
  },
  "inbounds": [
    {
      "type": "tun",
      "inet4_address": "172.19.0.1/30",
      "auto_route": true,
      "strict_route": false,
      "sniff": true
    }
  ],
  "outbounds": [
    {
      "type": "hysteria2",
      "tag": "proxy",
      "server": "ip",
      "server_port": 443,
      "up_mbps": 20,
      "down_mbps": 100,
      "password": "123456",
      "tls": {
        "enabled": true,
        "server_name": "a.com",
        "insecure": false
      }
    },
    {
      "type": "direct",
      "tag": "direct"
    },
    {
      "type": "block",
      "tag": "block"
    },
    {
      "type": "dns",
      "tag": "dns-out"
    }
  ],
  "route": {
    "rules": [
      {
        "protocol": "dns",
        "outbound": "dns-out"
      },
      {
        "geosite": "cn",
        "geoip": [
          "private",
          "cn"
        ],
        "outbound": "direct"
      },
      {
        "geosite": "category-ads-all",
        "outbound": "block"
      }
    ],
    "auto_detect_interface": true
  }
}
```

