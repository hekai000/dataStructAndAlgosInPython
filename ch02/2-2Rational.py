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
	# 求最大公因子的算法(辗转相除法)
	#1.a÷b ，令r为所得余数（0≤r＜b）。若r=0，算法结束；b即为答案。
	#2.互换：置a←b，b←r，并返回第一步。
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


	def __eq__(self, another):
		return self._num * another.den() == self._den * another.num()

	def __lt__(self, another):
		return self._num * another.den() < self._den * another.num()

	def __str__(self):
		return str(self._num) + "/" + str(self._den)

five = Rational(5)
x = Rational(3, 5)
x.print2()
print x

y = five + x * Rational(5, 17)
if y < Rational(123, 11):
	print "y lt 123 11"

t = type(five)
if isinstance(five, Rational):
	print "five is Rational type"
else:
	print "five is not Rational type"