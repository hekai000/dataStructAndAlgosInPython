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
def josephus_A(n, k, m):
	people = list(range(1, n+1))
	i = k - 1
	for num in range(n):
		count = 0
		while count < m:
			if people[i] > 0:
				count += 1
			if count == m:
				print people[i],
				people[i] = 0
			i = (i+1) % n
		if num < n - 1:
			print ", ",
		else:
			print ""
	return

if __name__ == "__main__":
	josephus_A(10, 2, 7)