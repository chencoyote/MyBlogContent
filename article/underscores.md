Title: Python中的下划线
Date: 2015-3-19 11:24:39
Category: Python
Tags: pythonnic


## 原文
码农周刊推送 个人翻译
原文在 --> [Underscores in Python By SHAHRIAR TAJBAKHSH](http://shahriar.svbtle.com/underscores-in-python)

## 正文

本文讨论`_`(下划线) 这个货在Python中的作用, 因为在Python中有很多时候都有使用`_`的毛病

### 单个的下划线

最典型的有三种情况:

1. **在解释器中**: 用`_`命名的目的是为了存放在交互式解释器中最后执行的结果, 首先会被标准的CPython解释器解释, 然后才是其他的

```Python
>>> _
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name '_' is not defined
>>> 42
>>> _
42
>>> 'alright!' if _ else ':('
'alright!'
>>> _
'alright!'
```

PS: 仔细观察, `_` 原来的值是42, 但是在`if-else`之后变成了 `alright!`

2. **作为变量名**: 有一些过去的观点认为, `_`被当做_废弃_的变量名. 按照惯例, 这种写法会让之后的人读你代码的时候知道这个变量已经被占用不能被使用.
比如, 在一个循环中没有价值的循环计数器

```Python
n = 42
for _ in range(n):
    do_something()
```

PS: 其实作者想说的意思就是, 这货就是来存放一些没意义的东西, 但是你还在代码中需要使用, 并且后续的代码也不会在去用的这个变量.

3. **i18n(所谓的国际化)**: 偶尔也可能看到`_`被当做一个函数来用. 实际上这个函数名是用来将国际化的语言和本地语言进行查找. 其实这个创意是也是根据C语言的习惯来的.
比如你阅读[Django documentation for translation](https://docs.djangoproject.com/en/dev/topics/i18n/translation/), 你可以看到

```Python
from django.utils.translation import ugettext as _
from django.http import HttpResponse

def my_view(request):
    output = _("Welcome to my site.")
    return HttpResponse(output)
```

PS: 特地把`gettext` 给 `as` 成 `_` 我也是醉了, 其实就是一些约定俗成, 方便阅读代码的时候一眼就知道在干啥.

### 变量名前的单下划线(e.g. `_shahriar`)

变量名前面的单下划线一般会被程序猿习惯的理解成"私有". 这也是一种为了方便后人(或者你自己)阅读你的代码的时候知道, 以`_`开头的变量是为内部所用. 像[Python文档](https://docs.python.org/3.4/tutorial/classes.html#tut-private)中有说:

> a name prefixed with an underscore (e.g. _spam) should be treated as a non-public part of the API (whether it is a function, a method or a data member). It should be considered an implementation detail and subject to change without notice.

> 一个前缀为下划线的变量名, 应该理解为不公有的API (或者一个函数, 一个方法, 一个成员变量). 这应该被认为是一个被履行的细节且在没有任何声明的时候不能改变.

作者的PS: 
> 我这里说的 _一种习惯_ , 是因为在解释器中实际上还有另外的意思.如果 `from <module/package> import *`, 如果没有以`_`开始的没用的module's/package也会被`__all__`这货给全部包含进来. 详情查看[importing * in Python](http://shahriar.svbtle.com/importing-star-in-python)

PS: 其实作者想说的谁就是, 如果你不把没用的东西用`_`作为前缀, 当你`import *`的时候会把这些没用的也给包含进来消耗资源.

### 变量名前的双下划线(e.g. `__shahriar`)

在变量名前用`__`(通常是在方法前面)这个并不算是一种习俗. 它在解释器中有一些特殊的含义. Python 重编了一些名字(Name mangling 也有叫名字粉碎, 我也不知道该怎么叫, 暂且叫重命名吧)为了避免和子类的名字发生冲突. 比如[Python文档](https://docs.python.org/3.4/tutorial/classes.html#tut-private)中提到

> Any identifier of the form __spam (at least two leading underscores, at most one trailing underscore) is textually replaced with _classname__spam, where classname is the current class name with leading underscore(s) stripped

> 每个类似于`__spam` (至少两个下划线前缀,至多一个后缀下划线) 都被替换成为了类似 `_classname__spam` 其中 `classname`是当前类的名字

例:

```Python
>>> class A(object):
...     def _internal_use(self):
...         pass
...     def __method_name(self):
...         pass
... 
>>> dir(A())
['_A__method_name', ..., '_internal_use']
```

PS: 这里所说的就是等你在类里面 使用双下划线做前缀的时候, 在Python解释器中会默认的把它的原来的类名给加上

正如所料, `_internal_use` 没有被替换, 但是 `__method_name` 被重命名为 `_ClassName__method_name`. 如果现在你创建一个A的子类B, 你可以很轻松的重写A的 `__method_name` 方法

```Python
>>> class B(A):
...     def __method_name(self):
...         pass
... 
>>> dir(B())
['_A__method_name', '_B__method_name', ..., '_internal_use']
```

其实这样做的目的就相当于 Java 中的 `final` 关键字或者C++中的正常(非虚)函数

### 前后都有两个下划线的变量名 (e.g. `__init__`)

这是Python中的特殊函数[Special method names](https://docs.python.org/3.4/reference/datamodel.html#specialnames), 这在很久以前就是一个习惯, 这种方法不会和用户定义的发生冲突, 然后你可以对他们进行调用和重写, 比如当你写一个类的时候, 你就经常会重写`__init__` 方法

没人会阻止你自己去写这种命名方式的方法(但是, 尽量别这么做):

```Python
>>> class C(object):
...     def __mine__(self):
...         pass
...
>>> dir(C)
... [..., '__mine__', ...]
```

最好的方法避免这种命名方式, 就是不用!





