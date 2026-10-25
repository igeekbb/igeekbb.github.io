---
cover: 'https://cdn.jsdelivr.net/gh/geekbb/oss_img/202309272107101.webp'
title: macOS 14 Sonoma 博通网卡驱动支持
categories: 技术
tags: 黑苹果
abbrlink: 48950
date: 2023-09-27 21:04:14
updated: 2023-12-25 18:04:14
---

### macOS 14 Sonoma

众所周知，苹果 macOS 14 终于把大刀抡向博通无线网卡，**BCM94360 / BCM943602** 都无法在 Sonoma 驱动，目前的解决方案只有使用 **OpenCore Legacy Patcher**，可以完美驱动博通无线网卡，唯一缺点就是每次升级 OS 都需要**OpenCore Legacy Patcher**打补丁，下面是操作教程。

**OpenCore Legacy Patcher** 已经对 macOS Sonoma 有初步支持，原文 https://github.com/dortania/OpenCore-Legacy-Patcher/pull/1077

### OpenCore 设置

#### NVRAM-随机访问存储器设置

> 将系统完整性保护设为 0x0803、禁用 AMFI

- 在 NVRAM>Add>7C436110-AB2A-4BBB-A880-FE41995C9F82>csr-active-config 添加 `03080000`
- ~~NVRAM>Add>7C436110-AB2A-4BBB-A880-FE41995C9F82>boot-args 添加 `amfi=0x80`~~
- 不再推荐用上面的~~amfi=0x80~~，推荐使用 [AMFIPass.kext](https://github.com/dortania/OpenCore-Legacy-Patcher/blob/main/payloads/Kexts/Acidanthera/AMFIPass-v1.4.0-RELEASE.zip) ，改为添加`-amfipassbeta`参数

![](https://cdn.jsdelivr.net/gh/igeekbb/OSS@main//2023/202312251801204.webp)



#### Misc-其它设置

> 将安全启动模型设置为 Disabled

* Misc > Security > SecureBootModel > `Disabled`

#### Kernel-内核设置

按以下顺序注入三个 kext   (**<u>一定要按图设置，否则有卡白苹果的风险</u>**)

下载： **[IOSkywalk.kext](https://github.com/dortania/OpenCore-Legacy-Patcher/blob/e21efa975c0cf228cb36e81a974bc6b4c27c7807/payloads/Kexts/Wifi/IOSkywalkFamily-v1.0.0.zip)、[IO80211FamilyLegacy.kext](https://github.com/dortania/OpenCore-Legacy-Patcher/blob/e21efa975c0cf228cb36e81a974bc6b4c27c7807/payloads/Kexts/Wifi/IO80211FamilyLegacy-v1.0.0.zip)** 、 **[AMFIPass.kext](https://github.com/dortania/OpenCore-Legacy-Patcher/blob/main/payloads/Kexts/Acidanthera/AMFIPass-v1.4.0-RELEASE.zip)** （右边下载原始文件）

* OSkywalk.kext
* O80211FamilyLegacy.kext
* O80211FamilyLegacy.kext(AirPortBrcmNIC)
*  AMFIPass.kext
* **最小内核设置为 23.0.0**

![](https://cdn.jsdelivr.net/gh/igeekbb/OSS@main//2023/202312251804234.webp)

阻止`com.apple.iokit.IOSkywalkFamily`加载 (**<u>一定要按图设置，否则有卡白苹果的风险</u>**)

* **最小内核设置为 23.0.0**
* **Strategy(策略) 设置为 Exclude(阻止)**

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202309272130168.webp)

#### 以上设置好后重启电脑

----



### OpenCore Legacy Patcher 设置

OpenCore Legacy Patcher [下载](https://bit.ly/3ZAH0ve)

* 点 Post-Install Root Patch

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202309272136489.webp)

* Start Root Patching 

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202309272138408.webp)

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202309272139664.webp)

#### 以上设置好后重启电脑

---

### 搞定

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202309272140309.webp)

且玩且珍惜~~

---

### 番外 博通网卡速率问题

早在 macOS 13 我就发现，博通部分网卡，虽然免驱，但是链接后速率很低（350Mbps 以下），刚开始以为是无线路由问题，后来才知道需要调整所属地区代码。

* 下载 [AirportBrcmFixup.kext](https://github.com/acidanthera/AirportBrcmFixup/tags)

* 放入 Kernel-内核设置，最大内核按图设置。（注意加载顺序） 

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202309281337152.webp) 

* NVRAM-随机访问存储器设置 boot-args 添加 `-brcmfxbeta brcmfx-country=HK` 地区设置成香港

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202309281346642.webp)

* 保存重启搞定

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202309281347552.png)
