---
cover: 'https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307261038829.webp'
title: 本地部署免费的  GPT3.5 和 GPT4
abbrlink: 37336
date: 2023-04-22 10:28:59
tags: ChatGPT
categories: AI
---

| 名称       | 项目地址                           |
| :--------- | :--------------------------------- |
| gpt 4 free | https://github.com/xtekky/gpt4free |

## 官方介绍

> 去中心化 AI 产业，通过几个反向工程的 API（poe.com、phind.com、chat.openai.com 等）提供免费的 GPT-4/3.5 脚本。
## 在线访问

[https://chat.chatbot.sex/chat](https://chat.chatbot.sex/chat) 包括 gpt-4、网络访问和类似于 gpt-jailbreak 的 DAN 模型


![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307261038826.webp)


## 本地部署

### 下载代码包


打开 [xtekky/chatgpt-clone](https://github.com/xtekky/chatgpt-clone)

下载压缩包并解压


![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307261038823.webp)


### 创建虚拟环境
首先，打开终端，进入上面解压包所在文件夹，运行下面命令


```bash
python3 -m venv myenv
```


### 激活虚拟环境

```bash
source myenv/bin/activate
```

### 更新 pip

> 如果提示要更新

```bash
pip install --upgrade pip
```

### 安装 flask
(需富强)

```bash
 pip install flask
```

### 安装 requests
(需富强)

```bash
 pip install requests
```


### 运行脚本

```bash
python3 run.py
```


![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307261038824.webp)

***

打开 http://127.0.0.1:1337
(需富强)
![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307261038825.webp)

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307261038822.webp)

***

请且用且珍惜……

4 月 23 日更新：已撸坏，再观察吧……

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307261038827.webp)


## 安装 python3


您可以尝试重新安装 pip 3 以确保它已正确安装。在终端中输入以下命令以卸载旧版本的 pip 3：

```bash
sudo apt-get remove python3-pip
```

然后使用以下命令安装最新版本的 pip 3：

```bash
sudo apt-get update
sudo apt-get install python3-pip
```

如果 pip 3 已成功安装，您可以通过输入以下命令来验证它：

```bash
pip3 --version
```

如果您仍然无法找到 pip 3，请尝试使用以下命令手动安装它：

```bash
sudo apt-get install python3-setuptools
sudo easy_install3 pip
```



将手动安装 pip 3 并将其添加到系统路径中。您现在应该能够在终端中使用 pip 3 命令了。

1.  打开终端并输入以下命令：
    

```bash
    Which pip 3
```


    这将输出 pip 的安装路径，例如：


```bash
    /usr/local/bin/pip 3
```


2.  将 pip 的安装路径添加到系统的环境变量中。您可以通过编辑您的 bashrc 文件来实现这一点。在终端中输入以下命令：
    
    
```bash
Echo 'export PATH="/path/to/python/bin:$PATH"' >> ~/. Bashrc
```
注意，你需要将上述命令中的“/path/to/python/bin”替换为 Python 的实际安装路径。
    
    
3.  重新加载 bashrc 文件以使更改生效：
    

```bash
    Source ~/. Bashrc
```
