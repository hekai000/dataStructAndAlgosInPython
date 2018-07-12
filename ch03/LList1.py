# encoding: utf-8
# !/usr/bin/env python

'''

@author: hekai

@license: (C) Copyright 2013-2017, kylinos.

@contact: hekai@kylinos.com.cn

@software: garner

@file: 2-6类定义实例.py

@time: 2018/7/10 11:39

@desc:

'''
from LList import LList, LNode, LinkedListUnderflow


class LLlist1(LList):
	def __init__(self):
		LList.__init__(self)
		self._rear = None
	def prepend(self, elem):
		if self._head is None:
			self._head = LNode(elem, self._head)
			self._rear = self._head
		else:
			self._head = LNode(elem, self._head)

	def append(self, elem):
		if self._head is None:
			self._head = LNode(elem)
			self._rear = self._head
			return
		else:
			self._rear.next = LNode(elem)
			self._rear = self._rear.next


	def pop_last(self):
		if self._head is None:
			raise LinkedListUnderflow("in pop_last")
		p = self._head
		if p.next is None:
			e = p.elem
			self._head = None
			return e
		while p.next.next is not None:
			p = p.next
		e = p.next.elem
		p.next = None
		self._rear = p
		return e

if __name__ == "__main__":
	from random import randint
	mlist1 = LLlist1()
	mlist1.prepend(99)
	for i in range(11, 20):
		mlist1.append(randint(1, 20))
	mlist1.printall()

	for x in mlist1.filter(lambda y:y % 2 == 0):
		print x,