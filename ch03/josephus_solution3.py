# encoding: utf-8
# !/usr/bin/env python

'''

@author: hekai

@license: (C) Copyright 2013-2017, kylinos.

@contact: hekai@kylinos.com.cn

@software: garner

@file: josephus_solution1.py

@time: 2018/9/4 15:51

@desc:

'''
from LCList import LCList
class Josephus(LCList):
	def turn(self, m):
		for i in range(m):
			self._rear = self._rear.next

	def __init__(self, n, k, m):
		LCList.__init__(self)
		for i in range(n):
			self.append(i+1)
		self.turn(k - 1)
		while not self.is_empty():
			self.turn(m - 1)
			print self.pop(),


if __name__ == "__main__":
	Josephus(10, 2, 7)