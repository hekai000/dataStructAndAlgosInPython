# 3.1 线性表和表ADT

## 表ADT

```
ADT List:                           #表A抽象数据类型
	List(self)                      #表构造操作，创建一个新表
	is_empty(self)                  #判断self是否为一个空表
	len(self)                       #获得self长度
	prepend(self, elem)             #将elem插入表头
	append(self, elem)              #表尾插入elem
	insert(self, elem, i)           #将elem插入作为第i个元素
	del_first(self)                 #删除表首
	del_last(self)                  #删除表尾
	del(self, i)                    #删除self中第i个元素
	search(self, elem)              #查找self中elem的位置，未找到返回-1
	forall(self,op)                 #对表中每个元素执行op操作

```