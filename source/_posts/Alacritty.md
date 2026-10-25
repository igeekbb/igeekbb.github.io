---
cover: 'https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307261410569.webp'
title: 给外观党换一个极简终端 Alacritty + 美化
tags: App
categories: web
abbrlink: 24064
date: 2023-04-26 14:07:37
---

## **简介**

> Alacritty 是一款 快速、跨平台的 OpenGL 终端仿真器，具有合理的默认设置，但允许进行广泛的配置。通过与其他应用程序集成，而不是重新实现它们的功能，它成功地提供了一组灵活的功能，并具有高性能。目前支持的平台包括 BSD、Linux、macOS 和 Windows。

| 名称      | github 地址                            |
| :-------- | :------------------------------------- |
| Alacritty | https://github.com/alacritty/alacritty |
| Homebrew安装 | `brew install alacritty` |





## **美化效果**

Alacritty (窗口)

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307261410570.webp)




Alacritty (图标)

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307261410571.webp)




***


### **美化字体&图标** 

* JetBrains Mono：面向开发人员的免费开源字体

| 名称      | 地址                               |
| :-------- | :--------------------------------- |
| jetbrains | https://www.jetbrains.com/lp/mono/ |
| 图标 | [点击下载](https://geek.4everland.store/Alacritty.icns) |
> mac 端在应用文件夹中找到` Alacritty.app` ，右键显示简介，然后将下载的 icns 文件拖动到左上角图标上，完成替换


![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307261410573.webp)

***




### **配置文件** 

#### **1、在线更新**

~在 Alacritty 运行下面的命令，重启即可。~
Alacritty 新版本现已改为 TOML 配置文件，需要转换成 TOML 格式

#### **2、替换配置文件**
- 替换 ~/.config/alacritty/alacritty.yml

| 名称      | 地址                                                   |
| :-------- | :----------------------------------------------------- |
| alacritty | [点击下载](https://geek.4everland.store/alacritty.yml) |

- 然后在 Alacritty 运行即可将YAML转换为 TOML 配置文件，重新生效。
```bash
alacritty migrate
```

#### **3、或者直接用我转好的 TOML 配置文件**
| 名称      | 地址                                                   |
| :-------- | :----------------------------------------------------- |
| TOML 格式 | [点击下载](https://geek.4everland.store/alacritty.toml) |
