# -*-coding: utf-8 -*-

'''

@author: hekai

@license: (C) Copyright 2013-2018

@contact: 675974119@qq.com

@software: garner

@file: DCList.py

@time: 2018/7/14 14:09

@desc:

'''
from LList1 import LinkedListUnderflow, LNode
from DLList import DLList
class DCNode(LNode):
	def __init__(self, elem, prev=None, next_=None):
		LNode.__init__(self, elem, next_)
		self.prev = prev

class DCList(DLList):
	def __init__(self):
		DLList.__init__(self)


	def prepend(self, elem):
		p = DCNode(elem, None, self._head)
		if self._head is None:
			self._rear = p
			self._head = p
			p.prev = p
		else:
			p.next.prev = p
			p.prev = self._rear
			self._head = p
			self._rear.next = p

	def append(self, elem):
		p = DCNode(elem, self._rear, None)
		if self._head is None:
			self._head = p
			self._rear = p
			p.next = p
		else:
			p.prev.next = p
			p.next = self._head
			self._rear = p
			self._head.prev = p


	def pop(self):
		if self._head is None:
			raise LinkedListUnderflow("in pop")
		e = self._head.elem
		self._head = self._head.next
		if self._head is not None:
			self._head.prev = self._rear
			self._rear.next = self._head
		return e

	def pop_last(self):
		if self._head is None:
			raise LinkedListUnderflow("in pop_last")

		e = self._rear.elem
		self._rear = self._rear.prev
		if self._rear is None:
			self._head = None
		else:
			self._rear.next = self._head
			self._head.prev = self._rear
		return e

	def printall(self):
		if self.is_empty():
			return

		p = self._rear.next
		while True:
			print p.elem
			if p is self._rear:
				break
			p = p.next


if __name__ == "__main__":
	dclist1 = DCList()

	dclist1.prepend(1)
	dclist1.prepend(2)
	dclist1.append(3)
	dclist1.append(4)
	dclist1.printall()
	print "***********"
	print dclist1.pop()
	dclist1.printall()
	print "***********"
	print dclist1.pop_last()
	dclist1.printall()
