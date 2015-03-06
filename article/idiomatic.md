Title: 转载: idiomatic.py
Date: 2015-3-5 10:54:30
Category: Python
Tags: pythonnic

## 背景

- 新年第一篇~ 写在正月十五元宵节! 新年快乐, 过了十五就过了年, 开始进入状态工作啦~
- PyConChina2014在北京没看到干货, 但是杭州 @施远敏 分享了一个适合于有些基础, 但是觉得不够Pythonnic的学者
- [原文PPT](https://docs.google.com/presentation/d/1Mer-SFLtELLtmS_QxLWbW1aEDX997JSN6eD3mCyV81k/edit?pli=1#slide=id.g475844c86_0369) 在google doc上
- 自己把这个PPT转成文章,记录下来
- 最后像作者致敬!

## Let's Go

### idiomatic python
顾名思义, 符合语言使用习惯的python代码
在我看来 idiomatic python == pythonnic

**目录**
- Idioms (风格, 所谓Python方言呗)
- Data Manipulation (数据操作)
- Control Flow (控制流)
- ‘itertools’ (python中的迭代器)
- Functional Python (python的功能)

**彩蛋**
打开python的CLI, 或者IPython, 输入```import this```
这就是Python的信仰啦~
The Zen of Python, by Tim Peters

```
# python
Python 2.7.6 (default, Nov 21 2013, 15:55:38) [GCC] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
>>> 
```

## No.1 Idioms

不在杭州现场....不知道speaker share了什么...粗略翻译了一下...orz

- An unwritten rule (不成文的约定)
- A common use-case (常见的用例)
- Usually make the code better in: (优化代码在以下方面)
  + Readability (可读性)
  + Speed (运行速度)
  + Resource usage (资源利用率)

## 数据操作

### Unpacking
可以理解为把多个值付给一个变量, 在用这个变量赋给多个变量

```
s = ('simon', 'shi', 066, 'simonshi@gmail.com')

# 一般青年
firstname = s[0]
lastname = s[1]
weight = s[2]
email = s[3]

# Python青年
firstname, lastname, weight, email = s
```

### swap value

记得谭浩强的C语言书上有这样一道题, 将a和b的值进行互换

```
# 一般青年
temp = a
a = b 
b = temp

# python青年
a,b = b,a

# 可能有些C青年看着不爽, 所以
a,b = (a,b)
```

### Don’t Underestimate
没看懂啥意思.....略....

### Concatenating Strings 

初学的时候经常会选择笨的办法实现需求, 但是有时候有更好的写法, 看起来更简单

```
fruits = ['cherry', 'coconut', 'blueberry', 'kiwi']

# 普通青年
# PS: 尼玛我一开始学习的时候经常这样做啊....
s = fruits[0]
for i in fruits[1:]:
    s += ', ' + f

# Python青年
print ', '.join(fruits)

```

### Looping over a collection

遍历的时候, 由于C语言的思想, for循环的时候经常使用数字标明当前元素是第几个

```
colors = ['red', 'green', 'blue', 'yellow']

# 一般青年
for i in range(len(colors)):
    print colors[i]

# Python青年
for color in colors:
    print color
```

### Looping backwards
反向遍历的时候, 初学会非常痛苦.....

```
# 一般青年
for color in reversed(colors):
    print color

# Python青年
for color in colors[::-1]:
    print color
```

### Looping with indices
遍历列表的索引

```
colors = ['red', 'green', 'blue', 'yellow']

# 一般青年
for i in range(len(colors)):
    print i, '-->', colors[i]

# python青年
for i, color in enumerate(colors):
    print i, '-->', color
```

### looping over a dictionary
遍历字典的key, value

```
codes = {'Xian': '29', 'Beijing':'10', 'Shanghai':'21'}
# 一般青年
for k in codes:
    print k, '-->', codes[k]

# Python 青年
for k, v in codes.items():
    print k, '-->', v

for k, v in codes.iteritems():
    print k, '-->', v
```

### ‘defaultdict’
如何使用 'defaultdict'

```
names = ['james', 'peter', 'simon', 'jack', 'john', 'lawrence']
# 期望得到
{8: ['lawrence'], 4: ['jack', 'john'], 5: ['james', 'peter', 'simon']}
```

**一般青年**
思考了很久写出了

```
groups = {}
for name in names:
    key = len(name)
    if key not in groups:
        groups[key] = []
    groups[key].append(name)
```

**Python 青年**

```
# 先用 ‘setdefault’ 来给字典赋默认值
groups = {}
for name in names:
    groups.setdefault(len(name), []).append(name)

# 用 ‘defaultdict’
from collections import defaultdict
groups = defaultdict(list)
for name in names:
    groups[len(name)].append(name)

```