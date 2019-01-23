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

class LNode:
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_
class LStack():
    def __init__(self):
        self._top = None

    def is_empty(self):
        return self._top is None

    def top(self):
        if self._top is None:
            raise StackUnderflow("in SStack.top()")
        return self._top.elem

    def push(self, elem):
        self._top = LNode(elem, self._top)
    def pop(self):
        if self._top is None:
            raise StackUnderflow("in SStack.pop()")
        p = self._top
        self._top = p.next
        return p.elem
if __name__ == "__main__":
    st1 = LStack()
    st1.push(3)
    st1.push(5)
    while not st1.is_empty():
        print(st1.pop())