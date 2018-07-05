# encoding: utf-8
# !/usr/bin/env python

'''

@author: hekai

@license: (C) Copyright 2013-2017, kylinos.

@contact: hekai@kylinos.com.cn

@software: garner

@file: sample-1.1.2.py

@time: 2018/7/5 16:40

@desc:

'''
def sqrt(x):
	y = 1.0
	while (abs(y * y - x) > 1e-6):
		y = (y + x / y)/2
	return y

if __name__ == "__main__":
	val = 9
	print sqrt(val)