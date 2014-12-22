Title: linxu终端烦人的"哔哔"声
Date: 2014-12-13
Category: Linux
Tags: linxu个性化

### 问题
不知道有多少人跟我遇到过同样的问题, 因为本人使用linux非常的懒, 已经习惯性的使用'TAB'来补全路径或者命令
但是使用TAB就会遇到一个问题, 就是如果你的输入的命令或者路径是错误的, 这个是后你按'TAB' 终端工具就会一直发出
'哔哔哔哔'的声音, 而我又是一个APM(手速, 玩过RTS类游戏的人都知道)比较多的, 所以经常在使用shell的时候关掉了声音
最近终于找到了解决方法.

一般Linux都适用, Mac OS 有待测试

### 解决

#### .bashrc
如果知道这个文件的作用的同学应该都懂, 在这个里面需要添加一行

```
$ vim $HOME/.bashrc
# 添加
INPUTRC=${HOME}/.inputrc  
```

#### .inputrc
再来说说这个文件, inputrc是用来做键盘按键映射的, 通过这个文件可以制作自己喜欢的 key-binding
关于 key-binding这个问题, 感兴趣的可以自己搜索, 因为一般很少用得上, 我们这里用上的是```bell-style```

之前已经在```bashrc```中添加了inputrc的环境变量, 接下来只需要在inputrc中添加```set bell-style none```就可以关掉声音了

最后只需要重新连接终端, 世界就安静了!~

bell-style的可取值是: **none**, **visible**, **audible**, 每个值的意义感兴趣可以深入研究一下.
