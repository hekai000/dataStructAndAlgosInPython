# 2.3 类的定义与使用

## 主要作用

1. 表示数据类型，创建这个类的实例
2. 确定一个名字空间，位于类体的定义都局部于这个类体

## 类对象及其使用

1. 两种操作：属性访问和实例化

## 静态方法和类方法

1. 静态方法：@staticmethod 可以通过类名或值为实例对象的变量，通过属性引用的方式调用
2. 类方法： @classmethod 必须有一个表示其调用类的参数，通常为cls。通常用类方法实现与本类所有对象相关的操作。

## 类定义的作用域

1. 在类里定义的名字具有局部作用域；如果需要在类定义之外使用，采用基于类名字的属性引用方式。
2. 如果需要在类中的函数定义中引用这个类的属性，一定要基于类名的属性引用方式。
```
class Countable:
	counter = 0
	def __init__(self):
		Countable.counter += 1
	@classmethod
	def get_count(cls):
		return Countable.counter
```

## 私有变量

1. 以一个下划线开头的名字作为实例对象内部的东西，永远不从对象的外部去访问它们
2. 一个属性以两个下划线开头，不以两个下划线结尾的，在类之外采用属性访问方式无法找到，因为python会将这种形式的名字改名
3. 前后都有两个下划线的属性，具有特殊的意义

## 继承

### 继承的作用

1. 基于已有类定义新类，复用已有代码和功能，减少定义新类的工作量
2. 定义一组类的继承关系，更好的组织程序

### 替换原理

1. B是基类，C是B的派生类
2. 在要求使用B的实例对象的上下文中使用B的派生类C的实例对象

### 派生类语法

```
class <classname>(BaseClass,...):
	<statements>
```

### issubclass(cls1, cls2)

可以检查cls2是否是cls1的直接或间接基类

### 派生类__init__常见形式

```
class DerivedClass(BaseClass):
	def __init__(self,...):
		BaseClass.__init__(self,...)
```

### 方法查找

1. 动态约束

基于方法调用是根据self所表示的实例对象类型去确定调用方法

2. 代码实例

```
class B:
	def f(self):
		self.g()
	def g(self):
		print "B.g called"

class C(B):
	def g(self):
		print "C.g called"
		
y = C()
y.f() # print C.g called
```

### super函数

1. 作用:要求从这个类的基类开始做属性检索

2. 两种形式

a. super().m(...) python解释器会从这个类的基类开始，按照属性检索规则去查找函数m
b. super(C, obj).m(...) 从指定的类C的基类开始查找函数属性m，并且obj是C的实例，找到m后，obj作为self实参