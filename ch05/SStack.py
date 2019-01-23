# encoding: utf-8
# !/usr/bin/env python

'''

@author: hekai

@license: (C) Copyright 2013-2017, kylinos.

@contact: hekai@kylinos.com.cn

@software: garner

@file: SStack.py.py

@time: 2019/1/22 14:17

@desc:

'''
class StackUnderflow(ValueError):
    pass
class SStack():
    def __init__(self):
        self._elems = []

    def is_empty(self):
        return self._elems == []
    def top(self):
        if self._elems == []:
            raise StackUnderflow("in SStack.top()")
        return self._elems[-1]
    def push(self, elem):
        self._elems.append(elem)
    def pop(self):
        if self._elems == []:
            raise StackUnderflow("in SStack.pop()")
        return self._elems.pop()

if __name__ == "__main__":
    st1 = SStack()
    st1.push(3)
    st1.push(5)
    while not st1.is_empty():
        print(st1.pop())