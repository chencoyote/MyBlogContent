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

反向遍历的时候, 初学会非常痛苦.

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

# 用‘defaultdict’生成结果
from collections import defaultdict
groups = defaultdict(list)
for name in names:
    groups[len(name)].append(name)

```

### Comprehensions
列表解析

题目:_判断一个列表中的所有数字是否为奇数, 并且生成一个新的列表用True或False来标明_

**一般青年**

```
A, odd_or_even = [1, 1, 2, 3, 5, 8, 13, 21], []
for number in A:
    odd_or_even.append(isOdd(number))

# 结果
[True, True, False, True, True, False, True, True]
```

**Python 青年**

```
A = [1, 1, 2, 3, 5, 8, 13, 21]

[isOdd(a) for a in A]
[True, True, False, True, True, False, True, True]

# Or

[a for a in A if a%2 != 0]
[1, 1, 3, 5, 13, 21]
```

扩充理解

```
List: [a**2 for a in A]
[1, 1, 4, 9, 25, 64, 169, 441]

Set: {int(sqrt(a)) for a in A}
set([1, 2, 3, 4])

Dict: {a:a%3 for a in A if a%3}
{8: 2, 1: 1, 2: 2, 5: 2, 13: 1}
```

## 控制流

### Truthiness
判断真假, 也就是True 或 False

```
# 一般青年
if names != []:
…
if foo == True:
…

# Python 青年
if names:
…
if foo:
```

这里作者列了一些判断的时候都是False的常见形式
也就是说 用 ```if ... : ....``` 的时候判断都是False

- None
- False
- zero for numeric types  *数字0*
- empty sequence, e.g. [], tuple() *空序列,如:```[]```和```()```*
- empty dictionaries  *空字典*
- a value of 0 or False returned when either ```__len__``` or ```__non_zero__``` is called *当一些返回值为0或者False的方法或者类*
这里```__len__``` 返回0 应该很好理解
不好理解的是```_non_zero__```
举个栗子:

```
class A:
  def __non_zero__(self):  # 这里有一点是错误, 不知道是Py3还是啥, 我在py2.7版本中叫__nonzero__
    return False

if A():
   print "A is True"
else:
   print "A is False"

```

这里的意思是说, 判断A的这个类的布尔值, 可以通过```__nonzero__``` 这个方法来改变

### if-in

判断某个值是否在某个集合当中

```
# 一般青年
is_generic_color = False
if color == 'red' or color == 'green' or color == 'blue':
    is_generic_color = True



# Python青年
is_generic_color = color in ('red', 'green', 'blue')
```

### for-else

谁也没想到还有 ```for-else``` 的用法吧

```
ages = [42, 21, 18, 33, 19]

# 一般青年
are_all_adult = True
for age in ages:
    if age < 18:
        are_all_adult = False
        break

if are_all_adult:
    print 'All are adults!'
```

Python青年要来喽

```
ages = [42, 21, 18, 33, 19]

# Python青年
for age in ages:
    if age < 18:
        break
else: # 如果循环没有跳出则执行
    print 'All are adults!'
```

### Context Manager

上下文管理器

```
# 一般青年
f = open('data.csv')
try:
    data = f.read()
finally:
    f.close()

# Python 青年
with open('data.csv') as f:
    data = f.read()
```

## import itertools

这章讲的都是itertools的库中的方法, 所以默认前提是

```
from itertools import *
```

### Looping with two collections

遍历两个集合
示例中想要吧两个列表中的元素进行一一对应, 但是长度不同, 需要进行处理

```
colors = ['red', 'blue', 'green', 'yellow']
fruits = ['cherry', 'blueberry', 'kiwi']

# 一般青年
min_len = min(len(colors), len(fruits))
for i in range(min_len):
    print fruits[i], '-->', colors[i]

# Python 青年
for fruit, color in izip(fruits, colors):  # 此处的izip 是from itertools import izip
    print fruit, '-->', color
```

### Building Dictionaries

合并成为字典

```
# 要求
fruits = ['cherry', 'blueberry', 'kiwi', 'mango']
colors = ['red', 'blue', 'green', 'yellow']

# 合并成为
{'kiwi': 'green', 'cherry': 'red', 'mango': 'yellow', 'blueberry': 'blue'}

# 一般青年
pairs = {}
for fruit, color in izip(fruits, colors):
    pairs[fruit] = color

# PS:尼玛明明是刚才就是这么教的! 怎么变成一般青年了

# Python青年
pairs = dict(izip(fruits, colors))
# 草泥马奔腾....Python 就是总能用极简方式做事
```

### groupby

根据字母的多少进行分类

```
# 要求
names = ['james', 'peter', 'simon', 'jack', 'john', 'lawrence']
# 实现
{8: ['lawrence'], 4: ['jack', 'john'], 5: ['james', 'peter', 'simon']}

# 使用 itertools
{k:list(v) for k, v in groupby(names, len)}

# PS: 尼玛上面说的方法又被简化了....
```

### More

- chain([1,2,3], ['a','b'], [4]) ==> 1,2,3,'a','b',4
- repeat('A', 3) ==> 'A' 'A' 'A'
- cycle('ABCD') ==> A B C D A B C D ...
- compress('ABCDEF', [1,0,1,0,1,1]) ==> A C E F
- combinations/permutations/product
...

## Functional Python

说到这里就有些高大上了, 前面目录翻译的时候,没有想到那么多, 就翻译成了Python的功能,
到这里为止就看明白了, 原来是代表函数式编程的Python, 前面的也就不改了.

- Imperative programming (命令式编程: C/C++, Java)
- Declarative programming (声明式编程)
  - Functional programming (函数式编程: Lisp, Haskell, OCaml)
  - Logic programming (逻辑式编程: Prolog, Clojure)

> Functions are data, too. Can be passed through and manipulated like data.
> 函数也是数据. 它也可以像数据一样被传递和操纵

### partial

偏函数?! 这玩意是啥啊....

```
# 一般青年
def log(level, message):
    print "[{level}]: {msg}".format(level=level, msg=message)

def log_debug(message):
    log('debug', message)

def log_warn(message):
    log('warn', message)

def create_log_with_level(level):
    def log_with_level(message):
        log(level, message)
    return log_with_level

# construct functions like data
log_debug = create_log_with_level('debug')
log_warn = create_log_with_level('warn')

# 意思就是说
# 函数在执行时，要带上所有必要的参数进行调用。但是，有时参数可以在函数被调用之前提前获知。这种情况下，一个函数有一个或多个参数预先就能用上，以便函数能用更少的参数进行调用。

# Python青年
from functools import partial
# log 为上面定义过的那个函数
log_debug = partial(log, 'debug')
log_warn = partial(log, 'warn')
```

### Decorator

装饰器, 个人认为装饰器是Python中一个比较华丽的东西了, 如果用好了事半功倍, 如果用不好事倍功半

```
# 混合了业务逻辑和管理逻辑
def web_lookup(url, cache={}):
    if url not in cache:
        cache[url] = urllib.urlopen(url).read()
    return cache[url]

# 使用装饰器

@cache
def web_lookup(url):
    return urllib.urlopen(url).read()

from functools import wraps

def cache(func):
    saved = {}
    @wraps
    def new_func(*args):
        if args not in saved:
            saved[args] = func(*args)
        return saved[args]
    return new_func
```

### Combine

```
# imperative way
expr, res = '28++32+++32+39', 0
for token in expr.split('+'):
    if token:
        res += int(token)

# result of split
["28", "", "32", "", "", "32", "39"]

# functional way
res = sum(map(int, filter(bool, expr.split('+'))))

# step by step
["28", "", "32", "", "", "32", "39"]

filter(pred, seq) => [t for t in seq if pred(t)]
["28", "32", "32", "39"]

map(func, seq) => [func(t) for t in seq]
[28, 32, 32, 39]
```

这一节大概意思能看懂, 但是不能理解的非常透彻. 望请高手指点
主要核心思想体现在

```
res = sum(map(int, filter(bool, expr.split('+'))))
```

### Map

呐呐呐...这里开始解释上面用到的map啦

```
B = map(func, A)
┌───────┐     ┌─────────┐
│  a1   │ --> │ func(a1)│
│  a2   │ --> │ func(a2)│
│  a3   │ --> │ func(a3)│
│  an   │ --> │ func(an)│
└───────┘     └─────────┘
    A             B
```

也就是说 map的功能就是将A当做参数, 把A中的a1,a2,a3....an传递给func
结果集返回给B

### all

比for-else更加的传神, 23333

```
ages = [42, 21, 18, 33, 19]

# more expressive than using ‘for-else’
if all(map(lambda a:a>=18, ages)):
    print 'All are adults!'
```

### Fluent Interface

啥意思捏? O.O  上码

```
expr = '28++32+++32+39'
IterHelper(expr.split('+')).filter(bool).map(int).sum()
ages = [42, 21, 18, 33, 19]
IterHelper(ages).map(lambda x:x>=18).all()
```

还是不懂啊.....

```
class IterHelper(object):
    def __init__(self, iterable = []):
        self.iterable = iterable
 
    def dump(self):
        return list(self.iterable)
 
    def map(self, func):
        return IterHelper(itertools.imap(func, self.iterable))
 
    def filter(self, predicate):
        return IterHelper(itertools.ifilter(predicate, self.iterable))
 
    def sum(self):
        return sum(self.iterable)
 
    def all(self):
        return all(self.iterable)
```

哦哦, 原来如此, 作者是说可以写成```IterHelper(expr.split('+')).filter(bool).map(int).sum()```
这种形式的接口应该怎么写


## 结束语

> I have made this longer than usual because I have not had time to make it shorter.
> -- Blaise Pascal (1623-1662)

> 之所以写了这么长, 是因为我没有时间简化他
> -- 布莱士.帕斯卡

## Bigger than Bigger

把作者的这个玩意扔进ipython里

```
In [22]: ' '.join('{0:08b}'.format(ord(x)) for x in 'Bigger Than Bigger!')
Out[22]: '01000010 01101001 01100111 01100111 01100101 01110010 00100000 01010100 01101000 01100001 01101110 00100000 01000010 01101001 01100111 01100111 01100101 01110010 00100001'
```

哈哈, 是在说逼格儿嘛

## References
code like a pythonista: http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html
itertools: https://docs.python.org/2/library/itertools.html
functional python: http://ua.pycon.org/static/talks/kachayev
functools: https://docs.python.org/2/library/functools.html
pydash: http://pydash.readthedocs.org/en/latest/

## 感谢作者!!!