Title: 用Pelican搭建自己的博客（二）发布博客
Date: 2014-12-15 16:15:03
Category: 技术
Tags: python

继续上一篇

## 本地发布
由于现在没有正式的在浏览器中访问过博客，所以我们需要现在本地测试成功之后再发布到正常使用的服务器上

### 第一篇博客
Pelican使用纯静态页面来发布文章, 创建好的目录下其实已经提供了很好的几个工具,我们先来看看都是干嘛的

```
.
├── output             
├── content            
├── Makefile           // 生成html的makefile文件
                       // 可以通过make html来将content中得内容发布到output
├── develop_server.sh  // 本地测试服务启动脚本
                       // 通过 ./develop_server.sh start 来生成html和启动本地web服务
├── fabfile.py         // fabric自动化任务工具
                       // 可以在这个文件里面定义一些方法来使用 fab 方法名来进行发布任务
                       // 如可以定义一个publish的方法执行本地命令 fab publish来发布文档
├── pelicanconf.py     
└── publishconf.py     
```

那么们先来写一篇文档,在content文件中创建```first.md```并且写一些markdown的内容进去

之后在content文件夹所在的目录使用 make html来生成静态界面,当生成之后,使用```ls ./output```查看output目录下看到

```
.
├── archives.html
├── author
├── authors.html
├── categories.html
├── category
├── di-yi-pian-bo-ke.html
├── index.html
├── pages
├── sitemap.xml
├── tag
├── tags.html
└── theme
```

由一个空的目录变成了一个包含html和js+css的你柜台页面目录

然后我们切换到output得目录中,使用Python自带的SimpleHTTPServer,来开启本地服务

```
python -m SimpleHTTPServer 80
```

接着用浏览器访问```http://IP``` 就可以看到博客的样子啦;-)

### To Be Continue

**下一篇我们将介绍如何把本地服务配置成为web服务可以让博客可以被访问啦**