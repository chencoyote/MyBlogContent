Title: ZeroMQ学习笔记（一）
Date: 2014-12-18 11:00:07
Category: 学习笔记
Tags: python,zeromq

## 啥是ZMQ
官方如是说
> ZMQ (以下 ZeroMQ 简称 ZMQ)是一个简单好用的传输层，像框架一样的一个 socket library，他使得 Socket 编程更加简单、简洁和性能更高。是一个消息处理队列库，可在多个线程、内核和主机盒之间弹性伸缩。ZMQ 的明确目标是“成为标准网络协议栈的一部分，之后进入 Linux 内核”。现在还未看到它们的成功。但是，它无疑是极具前景的、并且是人们更加需要的“传统”BSD 套接字之上的一层封装。ZMQ 让编写高性能网络应用程序极为简单和有趣。

传统的socket都是一问一答的模式，就是所谓的端到端通讯，A给B发送了一个消息，B回给A一个消息。

而ZMQ则定义了多种的通讯方式，既可以同步，也可以异步，比如原来的socket在ZMQ中被定义成“问答模式”

## 为啥用ZMQ

### 无图无真相

![复杂的通讯](https://github.com/imatix/zguide/raw/master/images/fig8.png)

请问传统socket怎么破 ?

### 哪来的这个需求

在一个复杂的系统当中，数据是以数据流的方式来进行处理的，也就是说一个原始数据经过一条流水线之后成为用户真正想要得到的数据，同时过程中这些数据还要被其他的功能所引用。

例如：
某网络扫描工具，我们只能提供一个域名

- 第一个处理这个域名的进程将这个域名映射成为```{"ip": "192.168.1.1", "domain": "www.example.com"}```
- 第二个进程根据根据第一个进程结果的ip进行c段扫描，这个时候数据成了```{"ip":["192.168.1.1","192.168.1.2",....],"domain":"www.example.com"}```
- 第三个进程根据第二个结果中的域名（domain）进行子域名探测，这个时候数据成了```{"ip":["192.168.1.1","192.168.1.2",....],"domain":["www.example.com","blog.example.com","news.exapmle.com",......]}```
- 第四个.....第五个......
- 最后我们把输入的单个域名经过一系列的扫描探测等等，返回一个存在漏洞的URL地址和漏洞类型

当然这个工具只是一个想法，没有实现，也不知道实现的价值，但是我们的项目一些单个进程的工具是有的，就是没有整合成为一个综合的工具
[传送门:InfoMap](https://github.com/kttzd/informap)

## ZMQ官方文档

[官文](http://zguide.zeromq.org/py:all)

**本文所有用的图片全部都来自官文**

这里分享的是一些学习心得，没有大段代码。

## 学习笔记之ZMQ通讯模型

### 问答模式（REQ-REP）
![req-rep](https://github.com/imatix/zguide/raw/master/images/fig2.png)
这个模式和传统Socket差不多，是阻塞状态的，客户端sand服务端recv，这个很简单没啥可说的。
学习过程中我尝试启动一个服务端，多个客户端进行发送消息，服务端在这个模式只能是单条处理，如果同时发送按照消息发送到的时间先后进行处理的，在没处理之前，所有的进程都处于阻塞状态。
**实例代码太多了，我就不往这里搬了**

### 发布订阅模式（PUB-SUB）

![pub-sub](https://github.com/imatix/zguide/raw/master/images/fig4.png)
这个可以称为ZMQ的经典模型了，是Socket不容易做到的。

- 首先PUB的进程建立一个socket的通讯文件描述符 可以是ip加端口的形式```tcp://127.0.0.1:1234```也可以是IPC格式```ipc:///tmp/pub.ipc```
- 然后SUB进程进行connect到PUB创建的通讯文件描述符，如果PUB进程有消息发送，所有的SUB进程将能够全部收到相当于广播。不能够指定PUB给某一个进程而其他进程收不到。
- **the subscriber will always miss the first messages that the publisher sends.** 非常重要的一点是当PUB进程在建立连接的过程中已经在发布消息，那么SUB将会错过十几到几十条消息不等（自己测试，非官方），所以如果在通讯过程中最好能够定下SUB进程的数量，尽量避免动态SUB或者短链接的方法。

### 后续还会继续填补

to be continue......;-)

