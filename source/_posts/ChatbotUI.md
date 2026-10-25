---
cover: 'https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307251450612.webp'
title: 小白如何把 Chatbot UI 部署在本地
categories: AI
tags:
  - ChatGPT
  - Docker
abbrlink: 38531
date: 2023-04-14 14:43:00
---

**余所介紹之[Chatbot UI](https://geekbb.xlog.app/Github-ChatGPT-SP1#chatbot-ui)昔日已有所涉及，今乃吾之 ChatGPT 網頁端之主力也。吾素用 Github 之專案主頁所薦之一鍵部署於 Vercel，然近日 Vercel，或有日益眾多之使用者，令頁面載入漸見遲緩，影響體驗。欲观其能否部署於己之 VPS 或本地，故特記錄吾之部署過程。**

| 名称       | 地址                                       |
| ---------- | ------------------------------------------ |
| Chatbot UI | https://github.com/mckaywrigley/chatbot-ui |

---
### VPS 部署 (未完)
* 首先我按照项目说明在 VPS 安装好各类依赖和环境，运行

```
 docker build -t chatgpt-ui .
```
* 然后整个世界安静了，为我的小白行径自罚一杯

<table>
  <tr>
    <td style="width:50%;">
      <img src="https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307251450636.webp" style="width:100%">
    </td>
    <td style="width:50%;">
      <img src="https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307251450649.webp" style="width:100%">
    </td>
  </tr>
</table>



*待我搞台更强悍的 VPS?😅

---
### 本地部署
| 名称   | 配置           |
| ------ | -------------- |
| Mac OS | Ventura 13.3.1 |
| Docker | version 23.0.3 |

#### 打开终端
> 自行 ChatGPT 安装好 Docker，我的 Docker 项目都是放在"文稿"文件夹里，即:/Users/geek/Documents/docker


##### 终端进入 docker 文件夹

```
   cd /Users/geek/Documents/docker 
```

##### 克隆 chatbot-ui 项目到本地
```
git clone https://github.com/mckaywrigley/chatbot-ui.git
```
##### 进入 chatbot-ui 文件夹

```
 cd chatbot-ui 
```

##### 执行以下命令构建 Docker 镜像：
```
docker build -t chatbot-ui .
```
* 构建成功会出现如下提示：*如果失败就问 ChatGPT😂

>  => [production 8/8] COPY --from=build /app/next-i18next.config.js ./next  0.0s
>   => exporting to image                                                    10.3s
>   => => exporting layers                                                   10.3s
>   => => writing image sha256:bdc155462ef83c399e49a925fab840.0s
>   => => naming to docker.io/library/chatbot-ui

##### 运行 Docker 
* 将 xxxxxxxx 替换为你的 OpenAI API

```
docker run -e OPENAI_API_KEY=xxxxxxxx -p 3000:3000 chatbot-ui
```

---
* 要将 docker 容器从前台模式更改为后台模式，请使用以下命令：

```
docker run -d -e OPENAI_API_KEY=xxxxxxxx -p 3000:3000 chatbot-ui
```
* 在此命令中，我们添加了一个 -d 标志，它表示分离模式。这将使 Docker 容器在后台运行，而不是前台运行。

---

* 另外，如果您需要给容器命名，可以使用 --name 标志指定一个名称，例如：

```
docker run -d --name my-container -e OPENAI_API_KEY=xxxxxxxx -p 3000:3000 chatbot-ui
```
* 这将为容器命名为 my-container。

---
#### 打开浏览器 (搞定)🎉
```
http://127.0.0.1:3000/
```
![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307251450595.webp)

> 注：我用的是软路由白名单上网，国内环境使用，还请自行研究[chatgptProxyAPI](https://github.com/x-dr/chatgptProxyAPI)
