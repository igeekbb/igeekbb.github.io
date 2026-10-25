---
cover: https://cdn.jsdelivr.net/gh/igeekbb/OSS@main/2024/202404161605065.webp
title: $35/年 搬瓦工DC9传家宝 融合怪脚本跑分
date: 2024-04-16 15:50:11
tags: [VPS]
categories: [技术] 
---





{% poetry The DC9 Plan VPS 配置信息 footer:其实我更喜欢低延迟
 %}
- 硬盘：15 GB SSD
- 内存：768 MB
- CPU：1 核
- 流量：750 GB/月
- 带宽：1.5Gbps
{% endpoetry %}

{% tabs active:2 align:center %}

<!-- tab 图片版 -->
{% image https://cdn.jsdelivr.net/gh/igeekbb/OSS@main/2024/202404161438643.webp  ratio:2194/8202 %}

<!-- tab 文字版 -->
```
测评频道: https://t.me/vps_reviews                    
版本：2024.03.26
更新日志：VPS融合怪测试(集百家之长)                       
---------------------基础信息查询--感谢所有开源项目---------------------
 CPU 型号          : QEMU Virtual CPU version (cpu64-rhel6)
 CPU 核心数        : 1
 CPU 频率          : 2599.998 MHz
 CPU 缓存          : L1: 32.00 KB / L2: 4.00 MB / L3: 16.00 MB
 硬盘空间          : 945.89 MiB / 14240.99 MiB
 启动盘路径        : /dev/sda1
 内存              : 195.48 MiB / 736.76 MiB
 Swap              : 0 KiB / 783.00 MiB
 系统在线时间      : 0 days, 0 hour 38 min
 负载              : 0.47, 0.13, 0.04
 系统              : Debian GNU/Linux 12 (bookworm) (x86_64)
 AES-NI指令集      : ✔ Enabled
 VM-x/AMD-V支持    : ❌ Disabled
 架构              : x86_64 (64 Bit)
 内核              : 6.7.9-bbrplus
 TCP加速方式       : bbrplus
 虚拟化架构        : KVM
 NAT类型           : Full Cone
 IPV4 ASN          : AS25820 IT7 Networks Inc
 IPV4 位置         : Los Angeles / California / US
----------------------CPU测试--通过sysbench测试-------------------------
 -> CPU 测试中 (Fast Mode, 1-Pass @ 5sec)
 1 线程测试(单核)得分: 		544 Scores
---------------------内存测试--感谢lemonbench开源-----------------------
 -> 内存测试 Test (Fast Mode, 1-Pass @ 5sec)
 单线程读测试:		10089.90 MB/s
 单线程写测试:		10426.02 MB/s
------------------磁盘dd读写测试--感谢lemonbench开源--------------------
 -> 磁盘IO测试中 (4K Block/1M Block, Direct Mode)
 测试操作		写速度					读速度
 100MB-4K Block		8.6 MB/s (2095 IOPS, 12.22s)		10.2 MB/s (2478 IOPS, 10.33s)
 1GB-1M Block		346 MB/s (330 IOPS, 3.03s)		661 MB/s (630 IOPS, 1.59s)
---------------------磁盘fio读写测试--感谢yabs开源----------------------
Block Size | 4k            (IOPS) | 64k           (IOPS)
  ------   | ---            ----  | ----           ---- 
Read       | 30.32 MB/s    (7.5k) | 283.22 MB/s   (4.4k)
Write      | 30.34 MB/s    (7.5k) | 284.71 MB/s   (4.4k)
Total      | 60.67 MB/s   (15.1k) | 567.94 MB/s   (8.8k)
           |                      |                     
Block Size | 512k          (IOPS) | 1m            (IOPS)
  ------   | ---            ----  | ----           ---- 
Read       | 525.43 MB/s   (1.0k) | 761.56 MB/s    (743)
Write      | 553.34 MB/s   (1.0k) | 812.28 MB/s    (793)
Total      | 1.07 GB/s     (2.1k) | 1.57 GB/s     (1.5k)
---------------------流媒体解锁--感谢sjlleo开源-------------------------
以下测试的解锁地区是准确的，但是不是完整解锁的判断可能有误，这方面仅作参考使用
----------------Youtube----------------
[IPv4]
连接方式: Youtube Video Server
视频缓存节点地域: 美国  洛杉机(LAX17S56)
Youtube识别地域: 无信息(null)
----------------Netflix----------------
[IPv4]
您的出口IP可以使用Netflix，但仅可看Netflix自制剧
NF所识别的IP地域信息：美国
[IPv6]
您的网络可能没有正常配置IPv6，或者没有IPv6网络接入
---------------DisneyPlus---------------
[IPv4]
当前IPv4出口解锁DisneyPlus
区域：美国区
解锁Youtube，Netflix，DisneyPlus上面和下面进行比较，不同之处自行判断
----------------流媒体解锁--感谢RegionRestrictionCheck开源--------------
 以下为IPV4网络测试，若无IPV4网络则无输出
============[ Multination ]============
 Dazn:					Yes (Region: US)
 HotStar:				No
 Disney+:				No
 Netflix:				Originals Only
 YouTube Premium:			Yes
 Amazon Prime Video:			Yes (Region: US)
 TVBAnywhere+:				Yes
 iQyi Oversea Region:			US
 Viu.com:				No
 YouTube CDN:				Los Angeles, CA 
 Netflix Preferred CDN:			Los Angeles, CA  
 Spotify Registration:			Yes (Region: US)
 Steam Currency:			USD
 ChatGPT:				Only Available with Web Browser
 Bing Region:				US
 Instagram Licensed Audio:		->
 Instagram Licensed Audio:		Yes
=======================================
 以下为IPV6网络测试，若无IPV6网络则无输出
---------------TikTok解锁--感谢lmc999的源脚本及fscarmen PR--------------
 Tiktok Region:		【US】
-------------------欺诈分数以及IP质量检测--本脚本原创-------------------
数据仅作参考，不代表100%准确，如果和实际情况不一致请手动查询多个数据库比对
以下为各数据库编号，输出结果后将自带数据库来源对应的编号
ipinfo数据库  ① | scamalytics数据库 ②  | virustotal数据库  ③ | abuseipdb数据库 ④  | ip2location数据库   ⑤
ip-api数据库  ⑥ | ipwhois数据库     ⑦  | ipregistry数据库  ⑧ | ipdata数据库    ⑨  | ipgeolocation数据库 ⑩
ipapiis数据库 ⑪ | ipapicom数据库    ⑫  | abstractapi数据库 ⑬ | ipqualityscore数据库 ⑭ 
欺诈分数(越低越好): 0⑤  abuse得分(越低越好): 0⑤  0.0026 (Low)⑪  威胁等级: low②  
IP类型: 
  使用类型(usage_type):hosting①  Data Center/Web Hosting/Transit⑤  hosting⑧  hosting⑨  hosting⑪  
  公司类型(company_type):hosting①  business⑧  business⑪  
  云服务提供商(cloud_provider):  Yes⑧ 
  数据中心(datacenter):  Yes⑥ ⑨ ⑪ 
  移动网络(mobile):  No⑥ ⑪ 
  代理(proxy):  No① ②   Yes⑥ ⑦ ⑧ ⑨ ⑪ ⑫ 
  VPN(vpn):  No① ②   Yes⑦ ⑧ ⑪ 
  TOR(tor):  No① ② ⑦ ⑧ ⑨ ⑪ ⑫ 
  TOR出口(tor_exit):  No⑧ 
  搜索引擎机器人(search_engine_robot):② 
  匿名代理(anonymous):  Yes⑦ ⑧   No⑨ 
  攻击方(attacker):  No⑧ ⑨ 
  滥用者(abuser):  No⑧ ⑨ ⑪ 
  威胁(threat):  No⑧ ⑨ 
  iCloud中继(icloud_relay):  No① ⑧ ⑨ 
  未分配IP(bogon):  No⑧ ⑨ ⑪ 
Google搜索可行性：YES
----------------三网回程--感谢zhanghanyun/backtrace开源-----------------
国家: US 城市: Los Angeles 服务商: AS25820 IT7 Networks Inc
北京电信 219.141.136.12  电信CN2 [优质线路]           
北京联通 202.106.50.1    电信CN2 [优质线路]           
北京移动 221.179.155.161 电信CN2 [优质线路]           
上海电信 202.96.209.133  电信CN2 [优质线路]           
上海联通 210.22.97.1     电信CN2 [优质线路]           
上海移动 211.136.112.200 电信CN2 [优质线路]           
广州电信 58.60.188.222   电信CN2 [优质线路]           
广州联通 210.21.196.6    电信CN2 [优质线路]           
广州移动 120.196.165.24  电信CN2 [优质线路]           
成都电信 61.139.2.69     电信CN2 [优质线路]           
成都联通 119.6.6.6       电信CN2 [优质线路]           
成都移动 211.137.96.205  电信CN2 [优质线路]           
---------------------回程路由--感谢fscarmen开源及PR---------------------
依次测试电信/联通/移动经过的地区及线路，核心程序来自ipip.net或nexttrace，请知悉!
广州电信 58.60.188.222
13.48 ms  *  局域网
11.09 ms  AS4134  美国, 加利福尼亚州, 洛杉矶, chinatelecom.com.cn, 电信
144.92 ms  *  中国, 广东, 广州, chinatelecom.com.cn, 电信
159.59 ms  *  中国, 广东, 深圳, chinatelecom.com.cn, 电信
158.85 ms  AS4134  中国, 广东, 深圳, chinatelecom.com.cn, 电信
152.69 ms  AS4134  中国, 广东, 深圳, chinatelecom.com.cn, 电信
广州联通 210.21.196.6
118.12 ms  *  局域网
0.72 ms  AS4134  美国, 加利福尼亚州, 洛杉矶, chinatelecom.com.cn, 电信
147.23 ms  *  中国, 广东, 广州, chinatelecom.com.cn, 电信
154.31 ms  AS4837  中国, 广东, 广州, chinaunicom.com, 联通
165.78 ms  AS4837  中国, 广东, 广州, chinaunicom.com, 联通
172.68 ms  AS17816  中国, 广东, 广州, chinaunicom.com, 联通
356.36 ms  AS17623  中国, 广东, 深圳, chinaunicom.com, 联通
194.71 ms  AS17623  中国, 广东, 深圳, chinaunicom.com, 联通
广州移动 120.196.165.24
38.10 ms  *  局域网
0.85 ms  AS4134  美国, 加利福尼亚州, 洛杉矶, chinatelecom.com.cn, 电信
146.18 ms  *  中国, 广东, 广州, chinatelecom.com.cn, 电信
157.37 ms  *  中国, 广东, 广州, chinatelecom.com.cn, 电信
160.30 ms  *  中国, 广东, 广州, chinatelecom.com.cn, 电信
184.93 ms  AS9808  中国, 广东, 广州, chinamobile.com, 移动
186.55 ms  AS9808  中国, 广东, 广州, chinamobile.com, 移动
184.78 ms  AS56040  中国, 广东, 深圳, chinamobile.com, 移动
--------------------自动更新测速节点列表--本脚本原创--------------------
位置		 上传速度	 下载速度	 延迟	  丢包率
Speedtest.net	 3149.66 Mbps	 3318.04 Mbps	 0.39	  0.0%
洛杉矶		 777.06 Mbps	 915.15 Mbps	 1.19	  0.0%
日本东京	 484.11 Mbps	 1318.05 Mbps	 125.18	  0.4%
联通上海5G	 12.61 Mbps	 13.44 Mbps	 151.69	  0.0%
联通天津5G	 1049.94 Mbps	 219.76 Mbps	 159.77	  NULL
电信Zhenjiang5G	 539.77 Mbps	 337.57 Mbps	 145.52	  NULL
移动Beijing	 870.76 Mbps	 338.43 Mbps	 166.92	  NULL
------------------------------------------------------------------------
 总共花费      : 7 分 53 秒
 时间          : Tue Apr 16 02:23:36 EDT 2024
------------------------------------------------------------------------
```
{% endtabs %}
