---
cover: 'https://cdn.jsdelivr.net/gh/geekbb/oss_img/202307260856765.webp'
title: 小白如何安装 Docker&Compose
tags: Docker
categories: 技术
abbrlink: 25175
date: 2023-04-20 08:54:43
---


{% quot el:h2 安装 Docker %}


{% hashtag Debian为例 color:yellow %}

```bash 更新软件包、安装 wget 和 vim 工具
apt-get update && apt-get install -y wget vim
```



```bash 下载并安装 Docker
wget -qO- get.docker.com | bash

```



```bash 显示 Docker 版本
docker -v
```



```bash 设置开机启动
systemctl enable docker
```


{% quot el:h2 安装 Docker-Compose %}


```bash 更新包列表
sudo apt update
```


```bash 安装 Docker Compose 依赖
sudo apt install curl
```


<!--使用以下命令从 Docker 官方网站下载最新版本的 Docker Compose 二进制文件：-->

```bash 下载 Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```



```bash 添加执行权限
sudo chmod +x /usr/local/bin/docker-compose
```

```bash 验证安装
docker-compose --version
```

如果成功安装，将显示 Docker Compose 的版本信息。



---


{% quot el:h2 卸载 Docker %}


```bash
Sudo apt-get purge docker-ce docker-ce-cli containerd. Io
```


```bash
Sudo rm -rf /var/lib/docker
Sudo rm -rf /var/lib/containerd
```

{% quot el:h2 Docker 常用命令 %}
| 命令                                                | 描述                                   |
| :-------------------------------------------------- | -------------------------------------- |
| `docker run`                                        | 运行一个容器                           |
| `docker build`                                      | 构建一个镜像                           |
| `docker pull`                                       | 拉取一个镜像                           |
| `docker push`                                       | 推送一个镜像到仓库                     |
| `docker images`                                     | 列出本地所有的镜像                     |
| `docker ps`                                         | 列出正在运行的容器                     |
| `docker stop`                                       | 停止一个或多个容器                     |
| `docker rm`                                         | 删除一个或多个容器                     |
| `docker rmi`                                        | 删除一个或多个镜像                     |
| `docker exec`                                       | 在容器中执行命令                       |
| `docker stop $(docker ps -a -q)`                    | 停止所有容器                           |
| `docker rm $(docker ps -a -q)`                      | {% mark 删除所有容器 color:red %}                        |
| `docker image prune -a`                             | 删除未使用的镜像                       |
| `docker volume prune`                               | 删除未使用的卷                         |
| `docker network prune`                              | 删除未使用的网络                       |
| `docker system prune`                               | 删除停止的容器、未使用的镜像、卷和网络 |
| `docker rmi $(docker images -f "dangling=true" -q)` | 清理无标签的镜像                       |
| `docker container prune`                            | 清理停止的容器                         |
| `docker system prune -a --volumes`                  | 清理不再使用的数据                     |
| `docker image prune -a -f`                          | 强制清理                               |
|                                                     |                                        |
