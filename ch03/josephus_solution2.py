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
def josephus_B(n, k, m):
	people = list(range(1, n+1))
	num, i = n, k - 1
	for num in range(n, 0, -1):
		i = (i + m -1) % num
		print people.pop(i),
	return

if __name__ == "__main__":
	josephus_B(10, 2, 7)