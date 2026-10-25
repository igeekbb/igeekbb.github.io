---
cover: 'https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307271640490.webp'
title: Docker 部署免费 GPT4-FreeGPT
tags:
  - Docker
  - ChatGPT
categories: AI
abbrlink: 28960
date: 2023-07-07 16:37:49
---

💡 [freegpt-webui](https://github.com/ramonvc/freegpt-webui)项目好像又行了，虽然不太稳定，免费的还要什么自行车。能用就行
https://github.com/ramonvc/freegpt-webui

> 使用 Docker 部署非常简单 (本地可用 OrbStack)



- 拉取镜像

```bash
docker pull ramonvc/freegpt-webui
```

- 启动

```bash
docker run -p 1338:1338 ramonvc/freegpt-webui
```

- 浏览器输入（本地）

```
http://127.0.0.1:1338` or `http://localhost:1338
```

> GPT-4 对话，我使用了`我爸爸妈妈结婚，为什么没有邀请我？` 来测试，还真是 GPT4，不过有时回答不太稳定

![Untitled](https://cdn.jsdelivr.net/gh/geekbb/oss_img@master/uPic/Untitled.png)

> 而 GPT3.5-turbo 0613 还是老样子

![Untitled (1)](https://cdn.jsdelivr.net/gh/geekbb/oss_img@master/uPic/Untitled%20(1).png)

<aside> 💡 最后：免费 GPT，对话受网络影响容易出错，有时需要多试几次，当成备用玩玩，足也。
</aside>
