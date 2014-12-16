Title: 用Pelican搭建自己的博客（一）环境的搭建
Date: 2014-12-15 16:15:03
Category: 技术
Tags: python

作为一个A Pythoner want to be Pythonic想要搭建一个自己博客，之前想要采取使用Django-CMS来搭建看了很多其他人写的源码之后开始动手自己写，但是发现自己时间不够充足，导致经常跳票写好了后台，又要配置数据库，总不能完全照搬人家的博客源码过来吧。所以经过了Django-CMS写了4个版本后，博客的进度被搁置了，知道有一天查找资料发现博主[cold's world](http://www.linuxzen.com/shi-yong-pelicanda-zao-jing-tai-bo-ke.html)的博客，深表感谢。重新燃起搭建的欲望，结果2天共计8小时完成搭建。所以记录下来分享一下。

有任何疑问可以留言或者邮箱联系我。

## 环境
### 硬件环境
Digitalocean 10刀服务器 Ubuntu 64位

之前很多人推荐这个还有Linode，两家都是SSD的服务器
感觉对于普通个人用户Digitalocean的5刀或者10刀还不错。
Linode没用过也不好评价，但是最低配和Digitalocean价格差不多。
PS：另外还部署了Shadowsocks，目前就几个人用，如果需要的可以联系我 ;-)

### 软件环境
#### Python 
- virtualenvwrapper
- Pelican
- MarkDown
- fabric

#### Linux
- bashshell
- crontab
- git

#### 其他
- disqus
- google analytics
- gumby

## 折腾
Python环境都是Ubuntu里面准备好的，所以不需要再自己安装，如果需要
```$ apt-get install python```
### virtualenvwrapper
virtualenvwrapper来安装Python的虚拟环境，一开始我是使用virtualenv来建立，但是发现创建的环境可以随便放，这样环境多了不易于自己维护，后来发现了virtualenvwrapper
```
# 如果有pip使用
$ pip install virtualenvwrapper

# 没有使用easy_install
$ easy_install virtualenvwrapper
```
安装完成后需要找到 ```virtualenvwrapper.sh```这个脚本，一般默认安装在
```/usr/bin/virtualenvwrapper.sh```
如果没有找到尝试看看
```
$ ls /usr/sbin/
$ ls /usr/local/bin/
$ ls /usr/local/sbin/
```
这个根据系统的环境变量不同可能有所不同
找到之后用source 添加到当前终端环境中
```
source /your/path/virtualenvwrapper.sh
```
建议省去每次都需要自己添加的麻烦，把这个命令添加到```.bashrc ```中
```
$ vim /home/(User)/.bashrc
# 如果是root用户
$ vim /root/.bashrc
```
然后重新连接一个SSH终端，这个时候会出现两个新的命令```mkvirtualenv```和```workon```
这两个命令分别是创建一个Python虚拟环境，和切换到某个Python虚拟环境
```
# 创建一个名为blog的python虚拟环境
$ mkvirtualenv blog

# 之后自动切换到虚拟环境中
(blog)$ 

# 退出虚拟环境
(blog)$ deactivate
$ 

# 使用workon进入或者切换环境
$ workon blog
(blog)$ 
(blog)$ workon other
(other)$ 
```

### 安装Pelican
以下工作环境都要先切换到指定的虚拟环境中

#### 使用github源码安装
```
$ git clone https://github.com/getpelican/pelican.git
$ cd pelican
$ python setup.py install
```
前提是你在系统里面装过了git命令，有的系统默认是没有git这个命令的
```
$ apt-get install git
```

### 使用pip安装
```
$ pip install pelican markdown
```
markdown是用来生成博客文章的，如果没有装，后面生成静态博客的时候md的文件会不能解析，无法生成html

### 开始搭建pelican博客
```
$ cd /your/path/blog/
$ pelican-quickstart
> Where do you want to create your new web site? [.]   # 生成在当前目录 
> What will be the title of this web site? title       # 博客的标题
> Who will be the author of this web site? author      # 博客的坐着
> What will be the default language of this web site? [en] zh #网站的默认语言 zh表示中文
> Do you want to specify a URL prefix? e.g., http://example.com   (Y/n) 
> What is your URL prefix? (see above example; no trailing slash) www.example.com # 输入自己的域名
# 以下都默认就好，需要的话自己改
> Do you want to enable article pagination? (Y/n) 
> How many articles per page do you want? [10] 
> Do you want to generate a Fabfile/Makefile to automate generation and publishing? (Y/n) 
> Do you want an auto-reload & simpleHTTP script to assist with theme and site development? (Y/n) 
> Do you want to upload your website using FTP? (y/N) 
> Do you want to upload your website using SSH? (y/N) 
> Do you want to upload your website using Dropbox? (y/N) 
> Do you want to upload your website using S3? (y/N) 
> Do you want to upload your website using Rackspace Cloud Files? (y/N) 
> Do you want to upload your website using GitHub Pages? (y/N) 
```
然后回答一系列问题之后，你的目录下会生成2个目录和4个文件
```
.
├── output             // 生成静态html的发布目录
├── content            // 发布文章的目录，存放md，rst文件
├── Makefile           // 生成html的makefile文件
├── develop_server.sh  // 本地测试服务启动脚本
├── fabfile.py         // fabric自动化任务工具
├── pelicanconf.py     // pelican的配置文件
└── publishconf.py     // make publish用的配置文件
```

至此博客的环境已经搭建完成，下一步就是测试发布博客和服务配置

