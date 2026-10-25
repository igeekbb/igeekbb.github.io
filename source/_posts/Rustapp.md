---
cover: 'https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307261323791.webp'
title: 用 Rust 命令行一键打包网页生成桌面 App
tags: App
categories: web
abbrlink: 14042
date: 2023-04-23 13:23:42
---

| 名称 | 项目地址                     |
| :--- | :--------------------------- |
| Pake | https://github.com/tw93/Pake |

> 支持 Mac / Windows / Linux，关于 [常用包下载](https://github.com/tw93/Pake/blob/master/README_CN.md#%E5%B8%B8%E7%94%A8%E5%8C%85%E4%B8%8B%E8%BD%BD)、[命令行一键打包](https://github.com/tw93/Pake/blob/master/README_CN.md#%E5%91%BD%E4%BB%A4%E8%A1%8C%E4%B8%80%E9%94%AE%E6%89%93%E5%8C%85)、[定制开发](https://github.com/tw93/Pake/blob/master/README_CN.md#%E5%AE%9A%E5%88%B6%E5%BC%80%E5%8F%91) 可见下面文档，也欢迎去 [讨论区](https://github.com/tw93/Pake/discussions) 交流。

## **特征**

```
🎐 相比传统的 Electron 套壳打包，要小将近 20 倍，5M 上下。
🚀 Pake 的底层使用的 Rust Tauri 框架，性能体验较 JS 框架要轻快不少，内存小很多。
📦 不是单纯打包，实现了快捷键的透传、沉浸式的窗口、拖动、样式改写、去广告、产品的极简风格定制。
👻 只是一个很简单的小玩具，用 Rust 替代之前套壳网页打包的老思路，其实 PWA 也很好。
```

---
## **打包 xLog 个人主页**


### **创建虚拟环境：**

```python
python3 -m venv myenv
```


### **激活虚拟环境：**


```python
source myenv/bin/activate
```


### **使用 npm 进行安装**

```bash
npm install -g pake-cli
```

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307261323792.webp)


### **查找 Pake 安装路径**

```bash
npm bin -g
```


![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307261323793.webp)



### **编辑配置文件**

```bash
nano ~/.bash_profile
```


### **添加 PATH 环境变量**


>  在文件末尾添加以下行：(地址可能不一)

```bash
export PATH=$PATH:/Users/geek/.npm-packages/bin
```

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307261323794.webp)


按下 `Ctrl` 键和 `X` 键，然后 `Y`，保存退出。

### **重新加载 Bash 配置文件**
```bash
source ~/.bash_profile
```

### **生成桌面应用** 

>  就用我的 xLog 主页小试 (第一次运行很慢，后面就好了)



```bash
pake https://x.geekbb.ml --name Geek --transparent
```

`*如遇见 rustc 错误请看最后`

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307261323795.webp)

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307261323796.webp)

### **效果图**

`GIF加载中……`
![](https://gcore.jsdelivr.net/gh/geekbb/oss_img@master/202307261323797.gif)


***

不过默认图标也是醉了，随便找一个 JPG 转 ICNS 网站

👉[JPG 转 ICNS - 在线转换图像文件 (aconvert.com)](https://www.aconvert.com/cn/image/jpg-to-icns/)

> -   MacOS 下必须为 `.icns`
> -   Windows 下必须为 `.ico`
> -   Linux 下必须为 `.png`

### **换默认图标**

后面加：`--icon <path>`


```bash
pake https://x.geekbb.ml --name Geek --transparent --icon /Users/geek/Documents/123/Geek.icns
```


![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307261323798.webp)

---

## **打包 [Chatbot UI](https://x.geekbb.ml/Github-Chatbot-ui)**

> [Chatbot UI 部署在本地](https://x.geekbb.ml/Github-Chatbot-ui)，正好可以打包，免得每次输入网址

```bash
pake http://192.168.2.100:3000 --name Chatbot --transparent --icon /Users/geek/Documents/123/chatgpt.icns
```

### **效果图**

`GIF加载中……`
![](https://gcore.jsdelivr.net/gh/geekbb/oss_img@master/202307261323799.gif)

***

> 如果遇见 zsh: command not found: rustc 错误👇

* 打开终端并依次执行以下命令：


```bash
curl --proto '=https' --tlsv 1.2 -sSf https://sh.rustup.rs | sh
```

* 打开终端，输入以下命令打开终端的配置文件：

```bash
nano ~/.zshrc
```
* 在打开的文件末尾添加以下代码：
```bash
export PATH="$HOME/.cargo/bin:$PATH"
```
1.  这个命令将 `$HOME/.cargo/bin` 添加到 PATH 环境变量中。
    
2.  按下 `Control + X`，然后按下 `Y` 保存更改并退出。
    
3.  输入以下命令更新终端的配置文件：
```bash
source ~/.zshrc
```

***
