Title: multiprocessing学习笔记
Date: 2014-12-19 16:52:53
Category: 学习笔记
Tags: python, multiprocessing

## multiprocessing
multiprocessing是Python 标准库中的多进程库, 由于Python不建议使用线程,所以尽可能的减少使用线程,如果需要建议使用 第三方库 futures来创建线程.

### 使用并发进程的好处
- 进程并发
- 充分利用多核优势
- 方便管理,可以接收Linux中的kill信号,根据信号进行安全退出
    + 之前使用一个python脚本,启动另一个进程的时候,如果想要完全脱离父进程,需要fork..fork..非常复杂
    + 通过multiprocessing创建的进程很容易就进行各种管理.

### multiprocessing创建并发进程

#### 创建简单并发进程

这种方式适用于那种单个功能,并且逻辑不复杂的进程

```Python
import multiprocessing 
import time

def add(a, b):
    while 1:
        print int(a) + int(b)
        time.sleep(1)

def pop(a, b):
    while 1:
        print a - b
        time.sleep(1)

def main():
    a = 10
    b = 1
    p1 = multiprocessing.Process(target=add,args=[a,b]);
    p2 = multiprocessing.Process(target=pop,args=[a,b]);
    p1.start()
    p2.start()
    print "p1 pid is %d" % p1.pid
    print "p2 pid is %d" % p2.pid

if __name__ == "__main__":
   main()
```
PS: 代码完全是为了实例实际谁计算会用并发进程

### 并发进程加队列实现进程通讯

这种方式可以使同一件事情拆分给多个进程去做,然后将结果返回到一个队列当中其他进程可以读取

这种方式可以应用到大量网络扫描时单进程扫描效率低的情况

```Python
# 这段代码米有测试过....直接写的...
import multiprocessing
import time

def scan(iplist, q):
    #  此处应为核心的扫描代码
    for ip in lplist:
        print "scanning %s" % ip
        res = do_some_scan(ip)
        
def get_res(q):
    while 1:
        print q.get()
        time.sleep(1)

def main():
    iplist = ["192.168.0.1","192.168.0.2","192.168.0.3","192.168.0.4",......]  # 这里可以自己处理
    proc_num = len(iplist)/10  # 假设ip 有50个一个进程扫10个,创建5个进程
    q = multiprocessing.Queue()
    t = 0
    for i in proc_num:
        p1 = multiprocessing.Process(target=scan,args=(iplist[t: t+10], q),);
        t = t + 10
        p1.start()
    q1 = multiprocessing.Process(target=get_res,args=(q),);
    q1.start()
```

### 通过继承Process类来定义进程

这种高级使用方法可以更加对象化的来定义一个Process对象,将一个Class作为一个进程类来使用

更好的是可以在里面定义一些接收信号退出的方法来优雅的退出进程.

```Python
import multiprocessing
import time
import signal

class Master(multiprocessing.Process):
    
    def __init__(self, args):
        # 在这个方法里面可以初始化一些变量
        super(Master,self).__init__()
        self.args = args
        self.needstop = False
        # 也可以对信号处理进行绑定
        signal.signal(signal.SIGTERM, self.handler_sigterm) # 处理终止信号
        signal.signal(signal.SIGQUIT, self.handler_sigquit) # 处理退出信号

    def handler_sigterm(self):
        self.needstop = True

    def handler_sigquit(self):
        # do someting
        self.needstop = True
    
    # 这个方法就是写核心功能的地方
    def run(self):

        print self.pid
        while not self.needstop:
            time.sleep(1)
            # do someting
            print "im working"

if __name__ == "__main__":
    master  = Master(args)
    master.start()
```
PS: 这里```run()```用到了while循环,突然想起之前遇到的一个问题,希望贴出来可以让大家借鉴

```Python
.....
while True:
    if a > 0:
        continue
    for i in range(10):
        a += a
    time.sleep(1)

.....
```
源代码记不清了,但是这个代码存在的问题就是其中第一个continue是没有sleep的,如果a到某一个时刻一直大于零,则会进入无挂起的死循环,CPU会被占满,这样就是无意间写出了一个bug, 示例代码可能比较短,不容易发现,如果代码比较长就会不容易发现这个bug,所以最好的方法就是,如果对于时间精度没有严格要求的代码的话,建议进入while循环先sleep, 这样避免了无意的资源浪费的.