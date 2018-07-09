# 2.2 Python的类

## 本节内容

1. 利用class实现ADT

### 有理数类

1. 类定义机制用于定义程序中需要的类型，定义好的一个类就像一个系统内部类型，可以产生该类的对象，实例对象具有这个类所描述的
行为
2. 有理数类

```
class Rational0:
	def __init__(self, num, den=1):
		self.num = num
		self.den = den
	def plus(self, another):
		den =self.den * another.den
		num = self.num * another.den + self.den * another.num
		return Rational0(num, den)
	def print(self):
		print(str(self.num) + "/" + str(self.den))
```

### 非实例方法(静态方法)

1. 不依赖类的对象
2. 类的实现需要使用的一种辅助功能，局部使用
3. 加修饰符@staticmethod

### Python中特殊方法名 

```
object.__add__(self, other)
object.__sub__(self, other)
object.__mul__(self, other)
object.__truediv__(self, other)
object.__floordiv__(self, other)
object.__mod__(self, other)
object.__pow__(self, other[, modulo])
```

### truediv 和 floordiv

```
>>> from __future__ import division
>>> 5//3
1
>>> 5/3
1.6666666666666667
```
1. // 为truediv， 只有```from __future__ import division```才生效， 否则跟floordiv一样
2. / 为floordiv， 求商，取整

### 完整Rational类
[Rational类] (https://github.com/hekai000/dataStructAndAlgosInPython/blob/master/ch02/2-2Rational.py)
