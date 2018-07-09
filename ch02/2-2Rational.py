# encoding: utf-8
# !/usr/bin/env python

'''

@author: hekai

@license: (C) Copyright 2013-2017, kylinos.

@contact: hekai@kylinos.com.cn

@software: garner

@file: 2-2Rational.py.py

@time: 2018/7/9 15:28

@desc:

'''
class Rational:
	@staticmethod
	def _gcd(m, n):
		if n == 0:
			m, n = n, m
		while m != 0:
			m, n = n % m, m
		return n

	def __init__(self, num, den=1):
		if not isinstance(num, int) or not isinstance(den, int):
			raise TypeError
		if den == 0:
			raise ZeroDivisionError
		sign = 1
		if num < 0:
			num, sign = -num, -sign
		if den < 0:
			den, sign = -den, -sign
		g = Rational._gcd(num, den)
		self._num = sign * (num//g)
		self._den = den // g

	def plus(self, another):
		den = self._den * another._den
		num = self._num * another._den + self._den * another._num
		return Rational(num, den)

	def print2(self):
		print str(self._num) + "/" + str(self._den)

	def num(self):
		return self._num

	def den(self):
		return self._den

	def __add__(self, another):
		den = self._den * another._den
		num = self._num * another._den + self._den * another._num
		return Rational(den, num)

	def __mul__(self, another):
		return Rational(self._num * another._num, self._den * another._den)

	def __floordiv__(self, another):
		if another._num == 0:
			raise ZeroDivisionError
		return Rational(self._num * another._den, self._den * another._num)

	def __sub__(self, another):
		den = self._den * another._den
		num = self._num * another._den - self._den * another._num
		return Rational(num, den)

a = Rational(-2, 8)
b = Rational(-7, 8)
c = a.plus(b)
d = a - b

d.print2()