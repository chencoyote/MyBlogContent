Title: multiprocessing 深度分析
Date: 2014-12-19 16:52:53
Category: 学习笔记
Tags: python, multiprocessing


[原文](http://pymotw.com/2/multiprocessing/basics.html)
Coyote翻译整理

## 正文
### multiprocessing 基本用法
最简单的在一个进程中启动多个进程的方法就是创建一个Process对象指定一个目标进程
然后调用start()方法启动.

```
import multiprocessing

def worker():
    """worker function"""
    print 'Worker'
    return

if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=worker)
        jobs.append(p)
        p.start()
```

执行代码, print出5个 `Worker`, 但是从这里是看不出他们的执行顺序的

```
$ python multiprocessing_simple.py

Worker
Worker
Worker
Worker
Worker
```

但是很多时候我们使用进程是需要传递一些参数来使进程能够正常工作的. 
与`threading`不同, 给`multiprocessing`的`Process`传递参数必须是能够用`pickle`序列化的.
下面这个例子也许能看出些有趣的东西

```
import multiprocessing

def worker(num):
    """thread worker function"""
    print 'Worker:', num
    return

if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i,))
        jobs.append(p)
        p.start()
```

每个进程都print了传递的整形参数

```
$ python multiprocessing_simpleargs.py

Worker: 0
Worker: 1
Worker: 2
Worker: 3
Worker: 4
```

### import目标功能(importable target function)

`threading`和`mutilprocessing`的一个不同就是`multiprocessing`可以在`__main__`的命名空间中执行.
如果使用这种新颖的方法来启动的话, 则子进程的功能需要从别的地方来import需要执行的功能. 
封装在`__main__`的核心代码部分如果在子进程运行,并不确定是否能够递归地运行在每个子进程的。
另一种方法是,从一个单独的脚本导入目标函数。

比如下面这个例子:

```
import multiprocessing
import multiprocessing_import_worker

if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=multiprocessing_import_worker.worker)
        jobs.append(p)
        p.start()
```

这里使用的核心代码在其他的模块中定义的:

```
def worker():
    """worker function"""
    print 'Worker'
    return
```

执行结果和第一个例子的结果相同

### 确定当前进程(Determining the Current Process)

单独传递一个参数给一个进程命名是不合理, 没必要的. 其实每个`Process`实例都有一个默认的名字, 而且这个名字在进程创建的时候是可以进行修改的. 给一个进程命名还是非常有用的, 可以很容易的找到你需要的进程, 尤其是在同时启动多个进程的时候.

```
import multiprocessing
import time

def worker():
    name = multiprocessing.current_process().name
    print name, 'Starting'
    time.sleep(2)
    print name, 'Exiting'

def my_service():
    name = multiprocessing.current_process().name
    print name, 'Starting'
    time.sleep(3)
    print name, 'Exiting'

if __name__ == '__main__':
    service = multiprocessing.Process(name='my_service', target=my_service)
    worker_1 = multiprocessing.Process(name='worker 1', target=worker)
    worker_2 = multiprocessing.Process(target=worker) # use default name

    worker_1.start()
    worker_2.start()
    service.start()
```

调试信息中每一行都输出了该进程的进程名称, 在进程名的输出那一列里面`Process-3`使用的是默认的进程名称, 虽然没有定义但是还是和`worker_1`一样有进程名称.

```
$ python multiprocessing_names.py

worker 1 Starting
worker 1 Exiting
Process-3 Starting
Process-3 Exiting
my_service Starting
my_service Exiting1
```

### 守护进程(Daemon Processes)

默认情况下子进程未退出的时候主进程是不会退出的. 但是很多时候我们需要在后台运行一个非阻塞模式的进程.
比如创建一个服务的时候就不能轻易的被其他进程打断, 或者在运行过程中业务中断但是数据不能丢失或者腐化(比如:给一个给服务端发送"心跳"的任务)

为了给一个进程标记成守护进程, 需要给`daemon`属性赋值为`True`或者`False`. 默认的创建进程的时候是非守护进程状态.所以修改`daemon`属性的值为`True`来开启守护进程模式.

```
import multiprocessing
import time
import sys

def daemon():
    p = multiprocessing.current_process()
    print 'Starting:', p.name, p.pid
    sys.stdout.flush()
    time.sleep(2)
    print 'Exiting :', p.name, p.pid
    sys.stdout.flush()

def non_daemon():
    p = multiprocessing.current_process()
    print 'Starting:', p.name, p.pid
    sys.stdout.flush()
    print 'Exiting :', p.name, p.pid
    sys.stdout.flush()

if __name__ == '__main__':
    d = multiprocessing.Process(name='daemon', target=daemon)
    d.daemon = True

    n = multiprocessing.Process(name='non-daemon', target=non_daemon)
    n.daemon = False

    d.start()
    time.sleep(1)
    n.start()
```

输出结果中没有包含守护进程print的`Exiting`消息. 从所有的非守护进程(包括主进程)退出之前开始计时, deamon进程sleep 2秒之后被唤醒.

```
$ python multiprocessing_daemon.py

Starting: daemon 13866
Starting: non-daemon 13867
Exiting : non-daemon 13867
```

守护进程应该在主进程退出之前自动退出, 否则会造成主进程退出, 守护进程一直运行. 你可以通过使用 `ps`命令来查看进程id 来确认那些程序是否都正常的运行.

## 等待进程结束(Waiting for Process) 

使用 `join()` 方法来等待进程运行结束

```
import multiprocessing
import time
import sys

def daemon():
    print 'Starting:', multiprocessing.current_process().name
    time.sleep(2)
    print 'Exiting :', multiprocessing.current_process().name

def non_daemon():
    print 'Starting:', multiprocessing.current_process().name
    print 'Exiting :', multiprocessing.current_process().name

if __name__ == '__main__':
    d = multiprocessing.Process(name='daemon', target=daemon)
    d.daemon = True

    n = multiprocessing.Process(name='non-daemon', target=non_daemon)
    n.daemon = False

    d.start()
    time.sleep(1)
    n.start()

    d.join()
    n.join()
```

执行了`join()` 方法之后, 主进程会等到守护进程运行结束再退出, 这次可以看到显示守护进程print的`Exiting`.

```
$ python multiprocessing_daemon_join.py

Starting: non-daemon
Exiting : non-daemon
Starting: daemon
Exiting : daemon
```

默认情况下, `join()`等待的时间是不定的. 所以可以给它传递一个超时时间的参数(可以直接传递一个表示等待多少秒的浮点型数字来启动超时时间). 如果子进程在超时时间内没有完成工作, 则直接退出.

```
import multiprocessing
import time
import sys

def daemon():
    print 'Starting:', multiprocessing.current_process().name
    time.sleep(2)
    print 'Exiting :', multiprocessing.current_process().name

def non_daemon():
    print 'Starting:', multiprocessing.current_process().name
    print 'Exiting :', multiprocessing.current_process().name

if __name__ == '__main__':
    d = multiprocessing.Process(name='daemon', target=daemon)
    d.daemon = True

    n = multiprocessing.Process(name='non-daemon', target=non_daemon)
    n.daemon = False

    d.start()
    n.start()

    d.join(1)
    print 'd.is_alive()', d.is_alive()
    n.join()
```

如果daemon程序内部的运行时间超出了设置的超时时间, 在`join()`之后程序会一直保持"alive"状态.

```
$ python multiprocessing_daemon_join_timeout.py

Starting: non-daemon
Exiting : non-daemon
d.is_alive() True
```

## 结束进程(Terminating Processes)

虽然正常情况下应该通过`signal`来结束进程, 如果一个进程挂起或者进入死锁状态, 就需要强制来杀死进程了. 调用进程对象的 `terminate()` 方法来结束所有的子进程.

```
import multiprocessing
import time

def slow_worker():
    print 'Starting worker'
    time.sleep(0.1)
    print 'Finished worker'

if __name__ == '__main__':
    p = multiprocessing.Process(target=slow_worker)
    print 'BEFORE:', p, p.is_alive()
    
    p.start()
    print 'DURING:', p, p.is_alive()
    
    p.terminate()
    print 'TERMINATED:', p, p.is_alive()

    p.join()
    print 'JOINED:', p, p.is_alive()
```

> **注意** 在结束进程之后需要调用`join()` 给后台一些反应时间来使进程结束, 而不是立即结束进程.

```
$ python multiprocessing_terminate.py

BEFORE: <Process(Process-1, initial)> False
DURING: <Process(Process-1, started)> True
TERMINATED: <Process(Process-1, started)> True
JOINED: <Process(Process-1, stopped[SIGTERM])> False
```

## 进程退出状态(Process Exit Status)

可以通过`exitcode` 来获取进程退出的退出状态
- `==0` 正常退出
- `> 0` 进程报错, 并且以该exitcode退出
- `< 0` 进程被使用结束信号杀掉, 该结束信号是 `-1 * exitcode`
```
import multiprocessing
import sys
import time

def exit_error():
    sys.exit(1)

def exit_ok():
    return

def return_value():
    return 1

def raises():
    raise RuntimeError('There was an error!')

def terminated():
    time.sleep(3)

if __name__ == '__main__':
    jobs = []
    for f in [exit_error, exit_ok, return_value, raises, terminated]:
        print 'Starting process for', f.func_name
        j = multiprocessing.Process(target=f, name=f.func_name)
        jobs.append(j)
        j.start()
        
    jobs[-1].terminate()

    for j in jobs:
        j.join()
        print '%s.exitcode = %s' % (j.name, j.exitcode)
```

进程抛出异常自动获取到`exitcode`为1

```
$ python multiprocessing_exitcode.py

Starting process for exit_error
Starting process for exit_ok
Starting process for return_value
Starting process for raises
Starting process for terminated
Process raises:
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python
2.7/multiprocessing/process.py", line 258, in _bootstrap
    self.run()
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python
2.7/multiprocessing/process.py", line 114, in run
    self._target(*self._args, **self._kwargs)
  File "multiprocessing_exitcode.py", line 24, in raises
    raise RuntimeError('There was an error!')
RuntimeError: There was an error!
exit_error.exitcode = 1
exit_ok.exitcode = 0
return_value.exitcode = 0
raises.exitcode = 1
terminated.exitcode = -15
```

## 子类进程(Subclassing Process)

最简单的方法启动一个进程就是使用target的方法来启动一个`Process`, 但是也可以通过子类的方式自定义进程子类.

```
import multiprocessing

class Worker(multiprocessing.Process):

    def run(self):
        print 'In %s' % self.name
        return

if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = Worker()
        jobs.append(p)
        p.start()
    for j in jobs:
        j.join()
```

继承出的子类, 应该重写`run()`方法来工作

```
$ python multiprocessing_subclass.py

In Worker-1
In Worker-2
In Worker-3
In Worker-4
In Worker-5
```

## PS
[原文链接](http://pymotw.com/2/multiprocessing/basics.html)
由**@Coyote**翻译, 转载需注明原文和翻译者
