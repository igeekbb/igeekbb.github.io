---
cover: 'https://cdn.jsdelivr.net/gh/geekbb/oss_img/202309222023685.webp'
title: 对抗 QoS 阻断&限速 Hysteria2 端口跳跃设置
categories: 技术
tags: VPS
abbrlink: 47180
date: 2023-09-22 09:08:41
---

```bash
#2023年10月9日更新
- 增加IPV6设置
```



### UDP 限速

三大运营商对 UDP 的阻断&限速肯定是存在的，至少有 QoS 限制，刚开始还以为南方联通比较宽容，没想都是一丘之貉，我遇见的是阻断，具体表现为“`连续下载或跑大流量3分钟左右，就直接阻断，大概再过几分钟又恢复连接`“，这些限制一般只是单个端口。本篇博文就来说说如何设置 Hysteria2 端口跳跃，以对抗运营商的阻断和限速。

----

### 搭建 Hysteria 2

关于 Hysteria2 节点的搭建，可以参考上一期《[Hysteria2 & VLESS-gRPC-uTLS-REALITY 对比测试](https://www.igeekbb.com/2023/09/18/hysteria/#%E9%83%A8%E7%BD%B2-Hysteria2)》

----

### 配合 Iptables 实现端口跳跃

按照 Hysteria 官网的说法，Hysteria 服务端并不能同时监听多个端口，因此不能在服务器端使用上面的格式作为监听地址。**建议配合 iptables 的 DNAT 将端口转发到服务器的监听端口。** [[来源]](https://v2.hysteria.network/zh/docs/advanced/Port-Hopping/)

下面就以我的 Hysteria 2 来演示：端口 5353 端口跳跃 20000-50000

#### 安装 iptables-persistent

{% codeblock %}
apt install iptables-persistent
{% endcodeblock %}

一直 YES&ENTER

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202309222024823.webp)

#### IPV4 设置

##### 清空默认规则&自定义规则

{% codeblock %}
iptables -F
{% endcodeblock %}

{% codeblock %}
iptables -X
{% endcodeblock %}



{% codeblock 允许本地访问 %}
iptables -A INPUT -i lo -j ACCEPT
{% endcodeblock %}


```bash 允许本地访问
iptables -A INPUT -p tcp --dport 22 -j ACCEPT
```



```bash 开放 HTTP / HTTPS 端口
iptables -A INPUT -p tcp --dport 80 -j ACCEPT
```

```bash
iptables -A INPUT -p tcp --dport 443 -j ACCEPT
```



```bash 开放 UDP 端口（5353 替换为自己 Hysteria 的监听端口）
iptables -A INPUT -p udp --dport 5353 -j ACCEPT
```


```bash 开放 UDP 端口跳跃范围（端口范围为 20000-50000）
iptables -A INPUT -p udp --dport 20000:50000 -j ACCEPT
```



```bash 允许接受本机请求之后的返回数据
iptables -A INPUT -m state --state RELATED,ESTABLISHED -j ACCEPT
```



```bash 其他入站一律禁止
iptables -P INPUT DROP
```



```bash 允许所有出站
iptables -P OUTPUT ACCEPT
```



```bash 查看开放的端口
iptables -L
```

##### 添加 NAT 规则 [[建议参考]](https://github.com/apernet/hysteria/issues/629)



```bash 将匹配到的 UDP 数据包的目标端口在 20000 到 50000 之间的数据包，重定向到本地服务器的 5353 端口
iptables -t nat -A PREROUTING -p udp --dport 20000:50000 -j DNAT --to-destination :5353
```



```bash 查看 NAT 规则
iptables -t nat -nL --line
```

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202309241107255.webp)

#### IPV6 设置


```bash 清空默认规则&自定义规则
ip6tables -F
```

```bash
ip6tables -X
```



```bash 允许本地访问
ip6tables -A INPUT -i lo -j ACCEPT
```



```bash 开放 SSH 端口（默认 22）
ip6tables -A INPUT -p tcp --dport 22 -j ACCEPT
```



```bash 开放 HTTP / HTTPS 端口
ip6tables -A INPUT -p tcp --dport 80 -j ACCEPT
```

```bash
ip6tables -A INPUT -p tcp --dport 443 -j ACCEPT
```



```bash 开放 UDP 端口（5353 替换为自己 Hysteria 的监听端口）
ip6tables -A INPUT -p udp --dport 5353 -j ACCEPT
```


```bash 开放 UDP 端口跳跃范围（端口范围为 20000-50000）
ip6tables -A INPUT -p udp --dport 20000:50000 -j ACCEPT
```


```bash 允许接受本机请求之后的返回数据
ip6tables -A INPUT -m state --state RELATED,ESTABLISHED -j ACCEPT
```

```bash 其他入站一律禁止
ip6tables -P INPUT DROP
```



```bash 允许所有出站
ip6tables -P OUTPUT ACCEPT
```



```bash 查看开放的端口
ip6tables -L
```

##### 添加 NAT 规则 [[建议参考]](https://github.com/apernet/hysteria/issues/629)


```bash 将匹配到的 UDP 数据包的目标端口在 20000 到 50000 之间的数据包，重定向到本地服务器的 5353 端口
ip6tables -t nat -A PREROUTING -p udp --dport 20000:50000 -j DNAT --to-destination :5353
```



```bash 查看 NAT 规则
ip6tables -t nat -nL --line
```



```bash 保存 iptables 规则
netfilter-persistent save
```

> 如果你填写错误，可以使用以下命令删除 iptables 规则

####  删除 iptables 规则


```bash 删除指定的 NAT 规则：
iptables -t nat -D PREROUTING <行号>
```

```bash 删除所有 NAT 规则：
iptables -t nat -F
```

{% codeblock %}
# 删除所有规则 
sudo ip6tables -F 

# 删除 INPUT 链中的所有规则 
sudo ip6tables -F INPUT 

# 删除 INPUT 链中的第一个规则 
sudo ip6tables -D INPUT 1 

# 禁用 INPUT 链中的第一个规则 
sudo ip6tables -I INPUT 1 -j DROP
{% endcodeblock %}



---

### Hysteria2 服务器配置文件


{% codeblock lang:yaml 自备域名版 %}
cat << EOF > /etc/hysteria/config.yaml
listen: :5353 #监听端口

#使用 CA 证书
acme:
  domains:
    - www.igeekbb.com #你的域名，需要先解析到服务器 ip
  email: geek@gmail.com

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
{% endcodeblock %}

---

{% codeblock 生成自签证书 %}
openssl req -x509 -nodes -newkey ec:<(openssl ecparam -name prime256v1) -keyout /etc/hysteria/server.key -out /etc/hysteria/server.crt -subj "/CN=bing.com" -days 36500 && sudo chown hysteria /etc/hysteria/server.key && sudo chown hysteria /etc/hysteria/server.crt
{% endcodeblock %}

```yaml 无域名自签版
cat << EOF > /etc/hysteria/config.yaml
listen: :5353 #监听端口

#使用 CA 证书
#acme:
#  domains:
#    - www.igeekbb.com #你的域名，需要先解析到服务器 ip
#  email: geek@gmail.com

#使用自签证书
tls:
  cert: /etc/hysteria/server.crt
  key: /etc/hysteria/server.key

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

---

这里展示 PassWall 客户端的填法

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202309222032643.webp)



---

> 以下是 Iptables 卸载步骤

### 卸载 Iptables


```bash 停止 iptables 服务
sudo systemctl stop iptables
```


```bash 禁用 iptables 服务
sudo systemctl disable iptables
```


##### Debian 系统

```bash 卸载 iptables 软件包
sudo apt-get remove iptables
```

##### CentOS 系统

```bash 卸载 iptables 软件包
sudo yum remove iptables
```


```bash 删除 iptables 配置文件&规则
sudo rm -r /etc/iptables/
```

```bash
sudo iptables -F
sudo iptables -X
```

---

资料参考：https://github.com/TinrLin/sing-box_-tutorial/tree/main/Hysteria2
