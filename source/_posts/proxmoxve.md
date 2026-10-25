---
cover: 'https://cdn.jsdelivr.net/gh/igeekbb/OSS@main//2023/202312201417139.webp'
title: Proxmoxve 安装手记 - All in One
date: 2023-11-29 13:39:23
categories: 技术
tags: 
  - Proxmoxve
  - 虚拟机
---

![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202312181117241.webp)



{% tabs active:1 align:center %}

<!-- tab 硬件配置 -->
{% checkbox checked:true CPU: I5 10500T ES版(QSRL) 6核12线程 %}
{% checkbox checked:true 内存: 16G+16G %}
{% checkbox checked:true 主板: MAG B460M MORTAR %}
{% checkbox checked:true 机械硬盘: WD30000FYYZS(3TB) * 3 %}
{% checkbox checked:true 固态硬盘: SN770(500G) 系统盘 %}
{% checkbox checked:true PCI网卡: intel 82576  %}
{% checkbox checked:true 机箱: N1 %}

<!-- tab 文件下载 -->
|  名称   |   地址 |  名称   |   地址 |
|  ----  | ----  |  ----  | ----  |
| Proxmox  | [下载](https://www.proxmox.com/en/downloads) |PveTools|[下载](https://github.com/ivanhao/pvetools)|
| Ventoy  | [下载](https://www.ventoy.net/cn/download.html) |OpenWrt|[下载](https://github.com/geekbb/OpenWrt/releases/tag/X86_64)
|Rufus|[下载](https://rufus.ie/zh/)|集客网关|[下载](http://file.cnrouter.com/index.php/Index/index.html?model_id=&device_type_id=2)|
|Debian|[下载](https://www.debian.org/)|TrueNAS|[下载](https://www.truenas.com/truenas-scale/)|
{% endtabs %}


{% quot  el:h2 PVE 安装 %}


{% quot 特别引用 icon:default %}

{% button 2022版通用型PVE_AIO服务器布局教程（上） https://www.youtube.com/watch?v=Mg4v5trSM9A/ icon:solar:planet-bold-duotone %}

{% button 通用PVE集成软路由，KODI，基于LXC的Docker服务教程 https://gitee.com/spoto/PVE_Generic_AIO/ icon:solar:planet-bold-duotone %}


### PVE 换源

```bash PVE换国内源
wget https://mirrors.ustc.edu.cn/proxmox/debian/proxmox-release-bullseye.gpg -O /etc/apt/trusted.gpg.d/proxmox-release-bullseye.gpg
echo "#deb https://enterprise.proxmox.com/debian/pve bullseye pve-enterprise" > /etc/apt/sources.list.d/pve-enterprise.list
echo "deb https://mirrors.ustc.edu.cn/proxmox/debian/pve bullseye pve-no-subscription" > /etc/apt/sources.list.d/pve-no-subscription.list
```

```bash Debian换源
mv /etc/apt/sources.list /etc/apt/sources.list.bk
nano /etc/apt/sources.list
```


```bash Sources.list加入源
deb http://mirrors.ustc.edu.cn/debian stable main contrib non-free
# deb-src http://mirrors.ustc.edu.cn/debian stable main contrib non-free
deb http://mirrors.ustc.edu.cn/debian stable-updates main contrib non-free
# deb-src http://mirrors.ustc.edu.cn/debian stable-updates main contrib non-free
# deb http://mirrors.ustc.edu.cn/debian stable-proposed-updates main contrib non-free
# deb-src http://mirrors.ustc.edu.cn/debian stable-proposed-updates main contrib non-free
```


```sh 更新
apt update
apt upgrade -y
```
。

```bash 列出系统中所有包含字符串“eth”的 PCI 设备，通常是网卡。
lspci | grep -i 'eth'
```
### 打开硬件直通

```bash 编辑Grub
nano /etc/default/grub
```

```bash 注释原条目，并增加开启参数
GRUB_CMDLINE_LINUX_DEFAULT="quiet intel_iommu=on"
或
GRUB_CMDLINE_LINUX_DEFAULT="quiet intel_iommu=on pcie_acs_override=downstream"
```

```bash 更新 grub
update-grub
```
### 开启核显 GVT-g

查询网址 https://ark.intel.com
```bash 支持 Intel Broadwell (5代) - Comet Lake (10代) 

lspci  -vs 00:02.0

输出
i915-GVTg_V5_1  # Video memory: <512MB, 2048MB>, resolution: up to 1920x1200
i915-GVTg_V5_2  # Video memory: <256MB, 1024MB>, resolution: up to 1920x1200
i915-GVTg_V5_4  # Video memory: <128MB, 512MB>, resolution: up to 1920x1200
i915-GVTg_V5_8  # Video memory: <64MB, 384MB>, resolution: up to 1024x768
```

```bash 编辑 etc/default/grub
GRUB_CMDLINE_LINUX_DEFAULT="quiet intel_iommu=on iommu=pt i915.enable_gvt=1"
```
![](https://img.igeekbb.com/blog-img/2024/10/202410291037313.webp)

```bash 编辑 etc/modules
nano /etc/modules
```
在最后添加 `kvmgt`
![](https://img.igeekbb.com/blog-img/2024/10/202410291042892.png)

依次执行以下命令:
```bash 
update-grub
```
```bash 
update-initramfs -u -k all
```

```bash  重启宿主机
reboot
```
添加核显到虚拟机
![](https://img.igeekbb.com/blog-img/2024/10/202410291047424.webp)

虚拟机显卡驱动下载

[**intel-7th-10th-gen-processor-graphics-windows**](https://www.intel.com/content/www/us/en/download/776137/intel-7th-10th-gen-processor-graphics-windows.html)

搞定🎉
![](https://img.igeekbb.com/blog-img/2024/10/202410291053273.webp)

{% quot el:h2 创建虚拟机 (OpenWrt) %}
### 下载 OpenWrt 
{% button 定制OpenWrt固件 https://openwrt.ai/ icon:solar:planet-bold-duotone %}


上传镜像
![](https://cdn.jsdelivr.net/gh/igeekbb/OSS@main/2023/202312210907137.webp)
根据自己需要新建虚拟机

```bash 在 PVE 下 `Shell` 输入
nano /etc/pve/qemu-server/[虚拟机编号].conf
```
将后面改为 `cache=unsafe`
![](https://cdn.jsdelivr.net/gh/igeekbb/OSS@main/2023/202312210935966.webp)

添加 PCI 网卡
![](https://cdn.jsdelivr.net/gh/igeekbb/OSS@main/2023/202312210914680.webp)

{% quot el:h2 创建 CT (Docker) %}


### 下载模板、创建 `特权\LXC`
{% gallery layout:grid aspect_ratio:original size:xl %}
![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202312181054136.webp)
![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202312181057163.webp)

勾选(嵌套：NFS：SMB/CIFS：FUSE：)
![](https://cdn.jsdelivr.net/gh/geekbb/oss_img/202312181123734.webp)
{% endgallery %}


```bash CT 模板换源
cp /usr/share/perl5/PVE/APLInfo.pm /usr/share/perl5/PVE/APLInfo.pm_back
sed -i 's|http://download.proxmox.com|https://mirrors.tuna.tsinghua.edu.cn/proxmox|g' /usr/share/perl5/PVE/APLInfo.pm
```

```bash 重启服务
systemctl restart pvedaemon.service
```
```bash 开启SSH登录
nano /etc/ssh/sshd_config
```
Port 22 去掉前面 # 号
PermitRootLogin 改为 yes 

![](https://cdn.jsdelivr.net/gh/igeekbb/OSS@main/2024/202409051016024.png)

{% quot el:h2 为容器加入 GPU 核显 %}

参考 {% button 司波图/通用PVE AIO安装教程  https://gitee.com/spoto/PVE_Generic_AIO/tree/master/1%E3%80%81%E5%88%9B%E5%BB%BA%E5%9F%BA%E4%BA%8ELXC%E7%9A%84Docker%E5%AE%B9%E5%99%A8_%EF%BC%88%E6%9C%AA%E5%AE%8C%E6%88%90%EF%BC%89/ icon:solar:planet-bold-duotone %}

```bash 部分显卡可能需要更新内核才能找到渲染器
nano /etc/pve/lxc/[CT_ID].conf
```

```bash
lxc.cgroup2.devices.allow: c 226:0 rwm
lxc.cgroup2.devices.allow: c 226:128 rwm
lxc.cgroup2.devices.allow: c 29:0 rwm
lxc.mount.entry: /dev/dri dev/dri none bind,optional,create=dir
lxc.mount.entry: /dev/fb0 dev/fb0 none bind,optional,create=file
lxc.apparmor.profile: unconfined
```
{% quot el:h2 挂载NAS目录(SMB) %}


```bash 安装  cifs-utils 软件包，该软件包提供了用于与 CIFS 协议兼容的网络共享进行交互的工具
apt install cifs-utils -y
```


```bash 新建共享目录(nas_share)
mkdir /mnt/nas_share
```

```bash 创建密码文件
nano ~/.smbcredentials
```


```bash 设置 SMB 登录用户名&密码
username=用户名
password=密码
```


```bash 修改自动挂载文件
nano /etc/fstab
```



```bash 设置文件挂载位置 "/mnt/nas_share"
//$smb_server/share /mnt/nas_share cifs credentials=/root/.smbcredentials,iocharset=utf8 0 0
```





{% quot el:h2 Docker 安装 %}


参考: {% button 小白如何安装 Docker https://igeekbb.github.io/2023/04/20/DockerCompose/ icon:https://api.iconify.design/solar:link-circle-bold-duotone.svg %}


### <span class="label label-info">Clouddrive2</span>


安装前请检查 <strong><span class="label label-success"><a href="https://hub.docker.com/r/cloudnas/clouddrive2-unstable">项目官网</a></span></strong> 最新配置  



```bash 使用 fuse3 挂载云存储，启用 MountFlags
mkdir -p /etc/systemd/system/docker.service.d/
cat <<EOF > /etc/systemd/system/docker.service.d/clear_mount_propagation_flags.conf
[Service]
MountFlags=shared
EOF
systemctl restart docker.service
```

```bash
cd /mnt
```

```bash
mount --make-shared  /
```


```bash 服务目录"/mnt/clouddrive2"
 docker run -d \
  --name clouddrive2 \
  --restart unless-stopped \
  --env CLOUDDRIVE_HOME=/Config \
  -v /mnt/clouddrive2/CloudNAS:/CloudNAS:shared \
  -v /mnt/clouddrive2/Config:/Config \
  -p 19798:19798 \
 --privileged \
 --device /dev/fuse:/dev/fuse \
 cloudnas/clouddrive2-unstable
```

### Emby 开心版


安装前请检查 <strong><span class="label label-success"><a href="https://hub.docker.com/r/lovechen/embyserver">项目官网</a></span></strong> 最新配置   


```bash
docker run \
 --network=bridge \
 -p '8096:8096' \
 -p '8920:8920' \
 -v /data/emby:/config \
 -v /mnt/clouddrive2/CloudNAS/:/data \
 -e TZ="Asia/Shanghai" \
 --device /dev/dri:/dev/dri \
 -e UID=0 \
 -e GID=0 \
 -e GIDLIST=0 \
 --restart always \
 --name emby \
 -d lovechen/embyserver:latest
```


### Portainer 汉化版


安装前请检查 [hashtag 项目官网](https://hub.docker.com/r/6053537/portainer-ce)  最新配置   


```bash 一键安装
docker run -d --restart=always --name="portainer" -p 9000:9000 -v /var/run/docker.sock:/var/run/docker.sock 6053537/portainer-ce
```

### navidrome

```bash compose.yaml
version: "3.3"
services:
  navidrome:
    container_name: navidrome
    restart: unless-stopped
    user: root
    volumes:
      - /mnt/clouddrive2/CloudNAS/阿里云盘Open/音乐:/music
      - /opt/stacks/navidrome/data:/data
    ports:
      - 4533:4533
    environment:
      - ND_LOGLEVEL=info
    image: deluan/navidrome:latest
networks: {}
```
### wallos

```bash compose.yaml
version: "3.0"
services:
  wallos:
    container_name: wallos
    image: bellamy/wallos:latest
    ports:
      - 8383:80/tcp
    environment:
      TZ: America/Toronto
    # Volumes store your data between container upgrades
    volumes:
      - ./db:/var/www/html/db
      - ./logos:/var/www/html/images/uploads/logos
    restart: unless-stopped
```
### metube
```bash compose.yaml
version: "3"
services:
  metube:
    image: ghcr.io/alexta69/metube
    container_name: metube
    restart: unless-stopped
    ports:
      - 8081:8081
    volumes:
      - /path/to/downloads:/downloads
```

---
更新中……





