---
cover: 'https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307251354228.webp'
title: 分享 ChatGPT 自用 Prompt 区别于网络上大多数烂套路
tags: [ChatGPT,Prompt]
categories: AI
abbrlink: 30577
date: 2023-04-10 19:36:12
---

**吾自己所用之 Prompt，与今世之甚多俗套有区别，实乃倾尽心思所编，愿其能助大家于事业成就之路（章法不一，而定期有更新）**

## 单词查询

> {英语单词查询解释}

```bash
请对Text以表格返回：
项目|结果
翻译成英文
国际音标
词性
词形
中文解释
词根词缀
例句1(英-中)
例句2
例句3
Text: """{{}}"""
```

![](https://cloudflare-ipfs.com/ipfs/bafkreiarzugkshqfkk4nzieutghxk2aze64mkuat4tdzprlq32yodhvdpu)

---

## 英文例句

> {查询中/英词汇，返回 3 个例句附中文}

```bash
请对Text以表格返回：
项目|结果
英文
例句1(英-中)
例句2(英-中)
例句3(英-中)
Text: """{{}}"""
```

![](https://cloudflare-ipfs.com/ipfs/bafkreicermbghs54w3njx3mspw4jd3whoo4rjqfbs5e6ddutx2cj7eilki)

---

## 汉字查询

> {查询汉字的拼音组词解释}

```bash
请对Text以表格返回：
项目|结果
拼音
组词
汉字解释
例句
Text: """{{}}"""
```

![](https://cloudflare-ipfs.com/ipfs/bafkreifk3k23otoylokiyyhlhtot7c4byq37klltgsxozhmxdvzuvo5kju)

---

## 中英互译

> {自动翻译目标语言}

```bash
translates  EN/CN,answer only.
Text:"""{{}}"""
```

![](https://cloudflare-ipfs.com/ipfs/bafkreiatyzux3ecz3g74aimatzsvrveq432fbaysdtey4agod2vgxxgiqe)

---

## 古文解释

> {自动翻译目标语言}

```bash
请对Text以表格返回：
项目|结果
拼音
现代解释
例句
Text: """{{}}"""
```

![](https://cloudflare-ipfs.com/ipfs/bafybeiginadrvksulfqsa2lt2pioc7kc5pb2w3zga5llkz5rctyxdswysq)

---

## 语言优化

> {用简洁的语言整理这一段话，增加逻辑性，去掉错别字}

```bash
请改进Text的拼写、语法、清晰、简洁和整体可读性，同时分解长句，减少重复。只返回更正版本，避免解释。
Text:"""{{}}"""
```

![](https://cloudflare-ipfs.com/ipfs/bafybeidndw5sj5apalwbskmj6qnge3ek2nkiv4slatq35socyutww5il5a)

---

## Excel 函数生成器

> {根据描述生成函数}

```bash
将Text指令返回指定的excel函数：
项目|结果
Excel函数
精简描述
Text:"""{{}}"""
```

![](https://cloudflare-ipfs.com/ipfs/bafybeidk4dzk2cem5egtwifxpvbhbzll6o335t4qetqm3ypee6xsipa2hq)

---

## 生成标题

> {复制/粘贴您的页面内容并询问}
> [配合 [Chatbot-ui](https://github.com/mckaywrigley/chatbot-ui)使用，实现多变量 Prompt]

`生成{{生成几个}}个独特的标题标签，最多 60 个字符，用于Text。它们应该描述性并包含术语"{{包含术语}}"： Text:"""{{内容}}"""`

![](https://cloudflare-ipfs.com/ipfs/bafybeigxase52oxwjux5hvdfpzsonbfcn6pmjdauhtwdx3w4yrdawhpwfe)
