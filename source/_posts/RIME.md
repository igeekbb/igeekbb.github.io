---
cover: 'https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307261436635.webp'
title: 从 macOS 到 iPhone 全面拥抱 RIME 输入法
tags: App 输入法
categories: web
abbrlink: 17265
date: 2023-04-29 14:40:13
---

> 中州韵输入法引擎是由佛振编写的开源中文输入法，目前项目网站、源代码均托管在 GitHub。基于同一个核心架构，该输入法分为三个官方发行版：Linux 发行版中州韵、Windows 发行版小狼毫、macOS 发行版鼠须管。--- [维基百科](https://zh.wikipedia.org/zh-cn/%E4%B8%AD%E5%B7%9E%E9%9F%BB%E8%BC%B8%E5%85%A5%E6%B3%95%E5%BC%95%E6%93%8E)
## 我的看法

### 初始
我是一名五笔输入法使用者，大约在 16 年接触到了中州韵输入法引擎，当时使用的是 Windows 发行版小狼毫。相比于搜狗输入法，这种输入法没有设置界面，全凭用户通过修改用户文件夹或程序文件夹里的 YAML 配置文件来客制化自己的输入法，在当时绝对是一股清流。后来，像大多数人一样，由于找不到各种功能的配置文件，入门即放弃。几年后，我断断续续地使用过，但总是感觉不得要领。
### 转机
直到最近，我看到一篇博文《[Rime Squirrel 鼠须管输入法配置详解](https://ssnhd.com/2022/01/06/rime/)》，通读过才算正真了解了 RIME 输入法，就是博主的这张图彻底解决了我找不到各种配置文件目录的问题，我真心建议想用好 RIME 输入法的朋友仔细看看这篇博文，你一定会从中得到很多收获。


![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307261436637.webp)


* 随即磨拳擦掌再次开始安装使用

## 入门到资深

### macOS 安装

> macOS 安装[鼠须管](https://rime.im/)，Windows 安装[小狼毫](https://github.com/rime/weasel)

如果你是单独使用拼音&五笔，大可用博文中的[配置](https://github.com/ssnhd/rime/archive/refs/heads/master.zip)懒人包，覆盖自已配置即可，不必折腾


### 五笔拼音混输

如果你是五笔拼音混输使用者，那你可以使用我的[配置](https://github.com/geekbb/-RIME-geek/archive/refs/heads/main.zip)文件覆盖使用，修改如下：


```
📝default.custom.yaml👇
* 五笔拼音混输设置为默认方案
* 候选词数量 10
📝pinyin_simp.schema.yaml👇
* 模糊音纠错全开 (南方人福音)
📝squirrel.custom.yaml👇
* 后选字改为竖排
* 字体设置为霞鹜文楷 
* 候选字大小设置为28(更适合4K屏幕)
* 集成皮肤N套（首推微信键盘皮肤“深浅”色）
📝installation.yaml👇
* 同步至 iCloud （文件夹RimeSync）
📝wubi86_jidian_pinyin.schema.yaml👇
*四码上屏。四码唯一时，自动上屏(影响拼音组字)
```
* 同步 iCloud 请打开 installation.yaml 将倒数二行 geek 改为你的 Mac 管理员名称“/Users/<font color="#ff0000">geek</font>/Library/Mobi……”
* 霞鹜文楷字体下载 https://github.com/lxgw/LxgwWenKai


### 皮肤效果

> 首选皮肤"微信键盘皮肤"，香不香！


![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307261436636.webp)

 

> 另外几套皮肤 (借用博主的图)

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307261436638.webp)

### 词库管理推荐
> 管理 #Rime #五笔 词库的工具，可添加、删除、批量导入外部词条、批量生成指定版本的五笔编码，支持 macOS Windows Ubuntu 多个平台

[五笔码表助手 for Rime](https://github.com/KyleBing/wubi-dict-editor)


![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307261436639.webp)

可以看到，拼音词库是 65116，五笔词库是 89271，还不够造吗？，有了这个词库工具，自己造吧
![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307261436640.webp)


* 这不比微信输入法强？顺嘴一提，为了您的隐私，真心不建议国内用户安装微信输入法。

### iPhone 安装
| 项目                | 地址                                                         |
| :------------------ | :----------------------------------------------------------- |
| <div>仓输入法</div> | https://github.com/imfuxiao/Hamster                          |
| App Store           | https://apps.apple.com/cn/app/%E4%BB%93%E8%BE%93%E5%85%A5%E6%B3%95/id6446617683?itsct=apps_box_badge&itscg=30200 |

> **仓输入法** 经过几次迭代，已经很完备了，推荐使用。

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307261436641.webp)


### iPhone 拼音方案

> 只推荐[雾凇拼音](https://github.com/iDvel/rime-ice)，将[雾凇拼音](https://github.com/iDvel/rime-ice)打包下载解压重命名为 Rime



![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307261436642.webp)


### 输入方案上传


> 打开网页，将原来的 Rime 方案删除，上传雾凇拼音包，注意文件夹还是要命名为 Rime 


![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307261436643.webp)

> 选择雾凇拼音，然后重新部署即可。


![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307261436644.webp)


> 切记不要打开配色方案，相信我，用自带的主题，又快又简洁！

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307261436645.webp)


* 模糊音请修改 `rime_ice.schema.yaml` 文件

***

## 结语

这篇文章适用于那些既会打五笔，但又忘记某些字根需要拼音辅助的朋友。希望这篇文章能对你们有所帮助， (没错，说的就是我！)
