Title: leetcode刷算法开坑
Date: 2015-3-24 15:34:36
Category: 学习笔记
Tags: python, algorithms

## 前言

[LeetCode OJ](https://leetcode.com/problemset/algorithms/)

[我的git库](https://github.com/chencoyote/pyleetcode)

## 背景

由于最近被鄙视竟然不会算法就敢写代码, 算法-数据结构-面向对象全都不懂, 你敢说你是程序员?

被打倒终究要爬起来!

通过学习,  来刷LeetCode的算法

## 正文

PS: 我是倒序做的.... 内容有参考网络, 但是自己是经过思考的

### No. 191 Number of 1 Bits

数出`1 bits` 有多少个

> Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the [Hamming weight](http://en.wikipedia.org/wiki/Hamming_weight)).

For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, so the function should return 3.

- 数出一个2进制数中的1的个数, 也叫`汉明权重`
- 例如:
   - 32位的2进制整数`11` 的二进制表示为`00000000000000000000000000001011`
   - 应当返回值为3

读懂题之后, 看原文中给的维基百科连接, 仔细读了一下, 给出了很多种解法, 

先说我的解法:
简单粗暴, 用`% 2`的做法来验证每一位是不是1

```python
 def hammingWeight(n):                                                           
     s = 0                                                                       
     while n is not 0:                                                           
         if n % 2 == 1:                                                          
            s += 1                                                               
         print "n: ", n                                                          
         n /= 2                                                                  
         # n = n >> 1                                                            
     return s                                                                    
 q = 0x10111011011 # count 8 1-bits
 hammingWeight(q)
```

其中`n /= 2` 和 `n = n >> 1`的效果是一样的
用时`45 ms`

再来看看wiki中的版本

> 其做法是采用这样的思想，类似归并的做法。对于相邻的两位，先计算这两位的1的个数(最大是2)，比如对于32位的数来说，分成 16组，**每组计算的是相邻两位的1的个数和**，并且将这个和用新得到的数的两位表示(2位可以最大表示4，所以可以存得下这个和，和此时最大为2)；然后对相邻四位进行操作，计算每两位两位的和（这样操作后其实是计算了原来32位数的相邻四位的1的个数）；这样依次类推，对于32位的数来说，只要操作到将其相邻16位的1的个数相加就可以得到其包含的1的个数了。

我的理解就是说, 
1. 先分成16组, 那么在与操作`0x3333333333333333`的时候, 就相当于统计出这16组中的第一位是`1`的个数, 然后用`>>`操作来位移之后, 统计出16组中第二位是`1`的个数
2. 两次之和就是16组中1的个数, 但是现在这16组并不能直接统计出结果, _但是你要是自己数的话, 已经知道了, 要这样做一开始就自己数了, 现在不是让计算机数嘛_
3. 然后把统计出的结果二分为8组, 