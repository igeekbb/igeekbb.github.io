---
cover: 'https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307251955034.webp'
title: Amazing-QR 只需四步制作一个炫酷二维码
tags: 二维码
categories: 技术
abbrlink: 26781
date: 2023-04-18 19:25:39
---

| 标题       | 项目地址                           |
| ---------- | ---------------------------------- |
| Amazing-QR | https://github.com/x-hw/amazing-qr |



* Amazing QR，是一款开源的 Python 应用程序，用于生成炫酷的二维码图像和动态 GIF 图片
  > 可生成普通二维码、带图片的艺术二维码（黑白与彩色）、动态二维码（黑白与彩色）

<p class="flex">
  <img src="https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307251959955.gif" alt="图片描述" width="200" height="200" />
  <img src="https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307251959957.gif" alt="图片描述" width="200" height="200" />
    <img src="https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307251959958.gif" alt="图片描述" width="200" height="200" />
        <img src="https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307251959959.gif" alt="图片描述" width="200" height="200" />  
  <img src="https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307251959794.gif" alt="图片描述" width="200" height="200" />



![6](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307251958362.webp)

![7](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307251958469.webp)

---
### 安装
#### 生成普通 QR 码
##### 使用虚拟环境 (推荐)
> 在虚拟环境中安装并运行 amzqr，可以确保使用的是正确的 Python 解释器和模块安装路径。

首先，打开终端，创建一个新的虚拟环境：


```
python3 -m venv myenv
```
![8](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307251958785.webp)

##### 激活虚拟环境：

```
source myenv/bin/activate
```
![9](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307251958003.webp)

##### 使用 pip 安装 amzqr

```
pip install amzqr
```
![1-1](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307251954475.webp)

##### 命令运行 `amzqr`

```
amzqr https://github.com
```

![11](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307251958190.webp)

🎉完成！

`/Users/geek/qrcode.png`

![12](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307251958993.webp)


----

#### 成生艺术二维码
##### 黑白图片
> 参数-p 用来将 QR 二维码图像与一张同目录下的图片相结合，产生一张黑白图片。我是将头像放入 qr 文件夹
```
amzqr https://x.geekbb.ml -p /Users/geek/qr/qr.jpg
```
![13](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307251958001.webp)

##### 彩色图片
> 加上参数 -c 可以使产生的图片由黑白变为彩色的。

```
amzqr https://x.geekbb.ml -p /Users/geek/qr/qr.jpg -c -con 1.5 -bri 1.6
```
* 参数-con 用以调节图片的对比度，1.0 表示原始图片，更小的值表示更低对比度，更大反之。默认为 1.0。
* 参数 -bri 用来调节图片的亮度，其余用法和取值与 -con 相同。
  

![14](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307251959449.webp)

##### GIF 图片

```
amzqr https://x.geekbb.ml -p /Users/geek/qr/qr.gif -c -con 1.5 -bri 1.6
```
![15](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307251959794.gif)

---
