Title: linxu终端烦人的ctrl+s
Date: 2015-2-6 10:21:20
Category: Linux
Tags: linxu个性化

## 问题

最近折腾了一下终端的个性化定制, 以及vim定制, 并且管理了自己的Dotfile

但是遇到一个烦人的问题, 快捷键里面有个`ctrl+a`经常被我给按成`ctrl+s`, 频率还不低

`ctrl+s`这个键组合在linux里面是`锁定屏幕显示` 搜了一下很多小白都遇到这个锁定屏幕之后不知所措

然后只好关掉终端重新打开. 网上也有解决方案就是按下`ctrl + q` 就能恢复.

## 思考

这个`ctrl+s` 的功能到底谁会用啊....同样的按键`ScrollLock`完全能用啊, 再按一下又恢复了嘛

所以考虑关掉这个该死的按键, 但是壮哉我大百度是不会给出解决方案的, 还得问我**大表哥**

- `ctrl+s` 会像终端发起一个`XOFF` 的信号
- `stty` linux是设置终端属性的命令

## 方案

`man stty` 查看man手册
> [-]ixoff
>    enable sending of start/stop characters
> [-]ixon
>    enable XON/XOFF flow control

所以只需要输入`stty ixoff -ixon`__'-'代表禁用__ 

再按下`ctrl+s` 是不是不会假死了;-)

当然会转换成`(i-search)':` 这个玩意目前还没有很好的解决方法...欢迎告诉我..