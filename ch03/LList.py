# encoding: utf-8
# !/usr/bin/env python

'''

@author: hekai

@license: (C) Copyright 2013-2017, kylinos.

@contact: hekai@kylinos.com.cn

@software: garner

@file: LList.py

@time: 2018/7/10 11:39

@desc:

'''
class LinkedListUnderflow(ValueError):
	pass


class LNode:
	def __init__(self, elem, next_=None):
		self.elem = elem
		self.next = next_

class LList:
	def __init__(self):
		self._head = None
	def is_empty(self):
		return self._head is None
	def prepend(self, elem):
		self._head = LNode(elem, self._head)
	def pop(self):
		if self._head is None:
			raise LinkedListUnderflow("in pop")
		e = self._head.elem
		self._head = self._head.next
		return e
	def append(self, elem):
		if self._head is None:
			self._head = LNode(elem)
			return
		p = self._head
		while p.next is not None:
			p = p.next
		p.next = LNode(elem)

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
		return e

	def find(self, pred):
		p = self._head
		while p is not None:
			if pred(p.elem):
				return p.elem
			p = p.next

	def printall(self):
		p = self._head
		while p is not None:
			print p.elem,
			if p.next is not None:
				print ", ",
			p = p.next
		print "\n"

	def for_each(self, proc):
		p = self._head
		while p is not None:
			proc(p.elem)
			p = p.next

	def elements(self):
		p = self._head
		while p is not None:
			yield p.elem
			p = p.next

	def filter(self, pred):
		p = self._head
		while p is not None:
			if pred(p.elem):
				yield p.elem
			p = p.next

	def length(self):
		p, n = self._head, 0
		while p is not None:
			n += 1
			p = p.next
		return n

	def insert(self, elem, i=0):
		p = self._head
		if i == 0:
			self._head = LNode(elem, self._head)
			return
		elif i != 0 and self._head is None:
			raise LinkedListUnderflow("insert")
		elif self.length() < i or i < 0:
			raise LinkedListUnderflow("insert length error")
		else:
			pass
		while p is not None and (i - 1) > 0:
			i -= 1
			p = p.next
		p.next = LNode(elem, p.next)

	def reverse(self):
		p = None
		while self._head is not None:
			q = self._head
			self._head = q.next
			q.next = p
			p = q
		self._head = p

	def sort1(self):
		if self.is_empty():
			return
		crt = self._head.next
		while crt is not None:
			x = crt.elem
			p = self._head
			while p is not crt and p.elem <= x:
				p = p.next
			while p is not crt:
				y = p.elem
				p.elem = x
				x = y
				p = p.next
			crt.elem = x
			crt = crt.next


def myprint(elem):
	print elem,


# mlist1 = LList()
# for i in range(10):
# 	mlist1.prepend(i)
# for i in range(11, 20):
# 	mlist1.append(i)
# mlist1.printall()
#
# mlist1.for_each(myprint)
# print "\n"
# for x in mlist1.elements():
# 	print x,
if __name__ == "__main__":
	mlist2 = LList()
	mlist2.insert(3)
	mlist2.insert(4)
	mlist2.insert(5)
	mlist2.printall()
	mlist2.sort1()
	mlist2.printall()
	mlist2.reverse()
	mlist2.printall()