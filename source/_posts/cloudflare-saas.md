---
cover: https://img.igeekbb.com/blog-img/2024/09/63c565a23edfdb0b6f7750dcb7563c40.webp
title: 利用优选 CNAME 域名提高网站访问速度 
categories: [技术] 
tags: [Cloudflare, 优选]
date: 2024-09-26 09:52:38
---

{% quot el:h2 引言 icon:hashtag %}

折腾 Cloudflare 给网站优选加速, 到达废寝忘食的地步, 起因是一个项目 [Enhanced-FaaS-in-China](https://github.com/xingpingcn/enhanced-FaaS-in-China) 号称可以提升部署在 Cloudflare、Vercel 或 Netlify 网页在中国的访问速度和稳定性. 项目是很久前就分享了, 因为我的博客是放 GitHub Pages, 研究了一下这个项目好像不能给 GitHub 加速, 故作罢..... 但转念一想, 为什么不试试把博客放 Vercel 加速看看效果呢, 反正是 Hexo 博客, 直接从 Vercel 拉 GitHub 就搞定. 套上项目给的 vercel-cname 地址 `vercel-cname.xingpingcn.top` 加速效果已经是相当给力了. 不知道大家有没有感受到...


{% image https://img.igeekbb.com/blog-img/2024/09/09085ec5f8c588725093f49b121da22a.webp  ratio:2724/2524 %}
{% image https://img.igeekbb.com/blog-img/2024/09/202409291355755.webp  ratio:1730/1537 %}


{% quot el:h2 教程 icon:hashtag %}

好, 直接上教程, 分三类加速, 因为有点绕 (我是各种坑踩了一遍, 网上的视频教程也绕到姥姥家了). 我尽量说得简单一些, 希望大家能看懂.

### 1. Vercel 网站加速 {% mark 域名一个 color:green %}

##### **第一步** 

也是最简单实现的方式, 以 `ChatGPTNextWeb` 项目为例, 在 Vercel 部署好后添加托管在 Cloudflare 的域名. 这里我就添加 `ggk.10kg.us.kg` 域名:

{% image https://img.igeekbb.com/blog-img/2024/09/202409292129563.webp  ratio:2758/1850 %}

---

##### **第二步** 

按照上图提示, 到 Cloudflare 域名管理页面, 将 `ggk.10kg.us.kg` **CNAME** 地址指向 `cname.vercel-dns.com` 等待解析和 SSL 证书申请(不要开始小云朵).

{% image https://img.igeekbb.com/blog-img/2024/09/202409301039936.webp  ratio:2356/1310 %}

回到 Vercel 项目一定要等 {% mark ✅两个勾 color:blue %} 打上
{% image https://img.igeekbb.com/blog-img/2024/09/202409301042868.webp  ratio:2682/1428 %}

---

##### **第三步** 
再回到 Cloudflare 域名管理将 `ggk.10kg.us.kg`  **CNAME** 地址指向优选域名, 保存搞定. 🎉
{% copy vercel-cname.xingpingcn.top prefix:CNAME优选 %}
{% image https://img.igeekbb.com/blog-img/2024/09/202409301044231.webp  ratio:2344/888 %}

现在使用 `https://ggk.10kg.us.kg` 访问 ChatGPTNextWeb 就用优选线路访问. 非高峰 1s 以内.
{% image https://img.igeekbb.com/blog-img/2024/09/202409301045442.webp  ratio:2732/1580 %}

---

#### 2. VPS 网站加速 {% mark 域名两个 color:green %}

  给部署在 VPS 上的网站套优选稍微复杂些, 需要开通 Cloudflar saas (免费). 过程虽然有些绕, 我坚信多踩几个坑就爬出来了. 这张图看不懂就别看了, 画完我也不知道画的是个啥玩意儿, 我们简单点直接上手操作.
{% image https://img.igeekbb.com/blog-img/2024/09/202409301045330.webp  ratio:2470/1500 %}


##### **第一步** 

准备两个域名分别托管在不同的运营商,这里以 Cloudflar & DNSPod 为例:

{% checkbox checked:true geek.AAA.com-托管在 Cloudflar %}
{% checkbox checked:true geek.BBB.com-托管在 DNSPod %}

记住 {% mark geek.AAA.com color:orange %} 作为回源域名, {% mark geek.BBB.com color:purple %} 作为访问域名. 开干🤜🤛!

来到 Cloudflar 管理的域名 {% mark AAA.com color:orange %} 左边 SSL/TLS -> 自定义主机名 绑定信用卡开通 Cloudflare for SaaS 功能, 扣款 0.00 元.

{% image https://img.igeekbb.com/blog-img/2024/09/202409301046914.webp  ratio:2556/1902 %}

开通后来到 DNS 设置, 将二级域名 {% mark geek.AAA.com color:orange %} 指向你的 VPS 服务IP, 并开启小云朵.
{% image https://img.igeekbb.com/blog-img/2024/09/202409301046275.webp  ratio:2136/1180 %}

---

##### **第二步** 

最重要的步骤来了, 回到刚才开通的 Cloudflare for SaaS 页面, 将二级域名 {% mark geek.AAA.com color:orange %} 添加进回退源地址, 等待**回退源状态**变成：{% mark 有效 color:green %}

{% image https://img.igeekbb.com/blog-img/2024/09/202409301047809.png  ratio:2432/1192 %}

##### **第三步**

自定义主机名 -> 添加自定义主机名, 将托管在 DNSPod 的 {% mark geek.BBB.com color:purple %} 添加进自定义主机

{% image https://img.igeekbb.com/blog-img/2024/09/202409301047776.png  ratio:2364/1478 %}

需要验证 {% mark geek.BBB.com color:purple %}  TXT 记录, 在 DNSPod 域名管理里添加自己的验证信息.

{% image https://img.igeekbb.com/blog-img/2024/09/202409301047031.webp  ratio:2334/1546 %}

添加上图所示的 TXT 记录,再加一条 {% mark geek.BBB.com color:purple %} **CNAME** 指向 {% mark geek.AAA.com color:orange %} 例:
{% image https://img.igeekbb.com/blog-img/2024/09/202409301049763.webp  ratio:2048/1076 %}

等待两个 {% mark 有效 color:green %} 出现后再住下操作
{% image https://img.igeekbb.com/blog-img/2024/09/202409301049997.webp  ratio:1876/947 %}

1/ SSL/TLS -> 概述 -> SSL/TLS 加密 -> 设置为 {% mark 完全（严格） color:green %}
{% image https://img.igeekbb.com/blog-img/2024/09/202409301050401.webp  ratio:2348/1076 %}

2/SSL/TLS -> 边缘证书 -> 始终使用 HTTPS -> ✅勾选
{% image https://img.igeekbb.com/blog-img/2024/09/202409301050740.webp  ratio:2270/1120 %}

打开托管在 DNSPod 的 {% mark geek.BBB.com color:purple %}  应该可以访问你部署在 VPS 服务网站啦.

##### **第四步**

好! 最后重要一步**加优选**, 进入 DNSPod 域名管理, 将刚刚 {% mark geek.BBB.com color:purple %} **CNAME** 指向改为 [Enhanced-FaaS-in-China](https://github.com/xingpingcn/enhanced-FaaS-in-China) 项目的优选地址:`cf-cname.xingpingcn.top` 大功告成 🎉
{% image https://img.igeekbb.com/blog-img/2024/09/202409301056360.webp  ratio:2048/1076 %} 

---

#### 3. VPS 网站加速 {% mark 域名一个 color:green %}

其实就是项目作者对于[一个域名](https://github.com/xingpingcn/enhanced-FaaS-in-China/blob/main/docs/how2use-SaaS-for-CF/how2use-SaaS-for-CF.md#%E9%9C%80%E8%A6%81%E4%BB%80%E4%B9%88)的思路, 我实践了, 是可行的! (操作起来更复杂一些)

{% image https://img.igeekbb.com/blog-img/2024/09/202409301057777.webp  ratio:1840/672 %} 

还是两个域名管理运营商 Cloudflare 和 DNSPod, 域名只要一个  **AAA.com** 托管在 Cloudflare. 

将它的二级域名 {% mark geek.AAA.com color:orange %} NS 记录指向 DNSPod 管理, 当然也需要验证 TXT, 我放张图, 大概就是这意思. 验证通过后就可以在 DNSPod 管理 {% mark geek.AAA.com color:orange %} 域名了,而 **AAA.com** 又可以在 Cloudflare 生成二级域名作为回源域名使用. 后面设置方法就和 VPS 网站加速 {% mark 域名两个 color:green %} 一样...

{% image https://img.igeekbb.com/blog-img/2024/09/202409301057274.webp  ratio:2232/752 %} 

多踩坑不害怕, 坑踩不多不足以记牢, 不明白的问 GPT 老师, 祝大家网站成功起飞 🎊

附相关资源:
1. enhanced-FaaS-in-China https://github.com/xingpingcn/enhanced-FaaS-in-China
2. Vercel托管站点提速小技巧 https://blog.001315.xyz/p/55
3. CloudFlare优选域名 https://www.182682.xyz/page/cloudflare/cname.html
4. WEB 速度测试 https://www.itdog.cn/http/
5. WEB 速度测试 https://www.boce.com/
6. 阿里云网络拨测工具 https://boce.aliyun.com/detect/http


经过我实测, 以下服务商优选域名比较稳定, 大家自行选用. 
| 服务商        | 优选域名                         | 官网                                                         |
|------------|------------------------------|------------------------------------------------------------|
| CloudFlare | cf-cname.xingpingcn.top      | [官网](https://github.com/xingpingcn/enhanced-FaaS-in-China) |
| CloudFlare | cdn.2020111.xyz              | [官网](https://blog.2020111.xyz)                             |
| CloudFlare | cnamefuckxxs.yuchen.icu      | [官网](https://cnamefuckxxs.yuchen.icu)                      |
| Vercel     | vercel-cname.xingpingcn.top  | [官网](https://github.com/xingpingcn/enhanced-FaaS-in-China) |
| Vercel     | vercel.001315.xyz            | [官网](https://blog.001315.xyz/p/55)                         |
| netlify    | netlify-cname.xingpingcn.top | [官网](https://github.com/xingpingcn/enhanced-FaaS-in-China) |
