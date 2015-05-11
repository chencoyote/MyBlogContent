Title: Gitlab 本地部署笔记
Date: 2015-5-11 10:09:11
Category: 学习笔记
Tags: git


## 下载地址

```
# 地址被墙, 不过有种解决方法就是去改https为http可以下载, 但是速度很慢
https://downloads-packages.s3.amazonaws.com/centos-6.6/gitlab-ce-7.10.0~omnibus.2-1.x86_64.rpm
```

## 安装环境
- CentOS 6.5
- 虚拟机
- 需要外网

## 方法

- 源码编译安装
- rpm安装

### 源码编译安装

- 好处: 就是可以根据自己需要来定制一些实用的软件呢, 如数据库/Nginx之类的
- 坏处: 就是安装过程太复杂, 调试起来非常复杂

### rpm安装
- 好处: 啥都内置了, 4部就可以部署完成 (实测没有几个可以4部就能完美运行的)
- 坏处: 定制性差, 数据库等都只能靠配置, 而且如果修改为别的配置修改起来非常麻烦, 而且还有可能不成功

## 过程

**本人用的rpm安装的方式**

官方文档和别人的教程都写的非常详细, 没必要拿来从新写, 过程都是一样的

[官方文档 | gitlab.com](https://about.gitlab.com/downloads/)
[Hiufan | segmentfault.com](http://segmentfault.com/a/1190000002722631)


## 遇到的问题

这个才是重要的, 每个人遇到的问题几乎都不同, 所以查找问题原因很麻烦
不如把遇到的问题贴出来, 可以之后参考

1. ```gitlab-rake```: 这个玩意在我了解, 可能是用来初始数据库的, 我用到的如下
- ```gitlab-rake gitlab:setup``` 第一次没跑起来, 查看官方文档, 看到数据库要初始化, 尝试之后可以正常使用了
- ```gitlab-rake clear``` 故名意思, 直接清干净数据库信息, 但是服务器上的repo是不会一起清除的, 需要手动清除

2. 页面显示500错误: 查看日志, 使用先使用```gitlab-ctl status```查看状态, 如果进程出现问题是会一直重启的,所以可以使用 ```gitlab-ctl tail 进程名``` 来查看单个进程的日志, 如果tail后面没有进程名, 则显示全部进程的名称

3. nginx配置: nginx配置起来非常麻烦, 所以索性我就关掉了, 找到对应的配置文件修改一下就可以了

4. ```gitlab-ctl reconfigure```: 每次修改了 ```/etc/gitlab/gitlab.rb``` 这个配置文件之后都需要执行这个命令才可以生效, 他会自动重启服务的. 但是同样有个问题, 就是如果修改过nginx或者其他的内置的程序的配置文件, 执行这个就会被还原, 很麻烦.

5. 500错误 postgresql SSL off 错误

```
==> /var/log/gitlab/postgresql/current <==
2015-05-08_12:04:03.93789 FATAL:  no pg_hba.conf entry for host "127.0.0.1", user "gitlab", database "gitlabhq_production", SSL off
2015-05-08_12:04:03.94352 FATAL:  no pg_hba.conf entry for host "127.0.0.1", user "gitlab", database "gitlabhq_production", SSL off
```

找到该配置文件```/var/opt/gitlab/postgresql/data/pg_hba.conf``` 最下面一行

```
# TYPE  DATABASE    USER        CIDR-ADDRESS          METHOD

# "local" is for Unix domain socket connections only
local   all         all                               peer map=gitlab
```
修改最后一行为

```
host   all         all          0.0.0.0/0            trust
```

问题解决, 但是具体为啥, 请查看postgresql文档

**注意: 每次reconfigure之后, 该文件被还原, 需要重新修改**