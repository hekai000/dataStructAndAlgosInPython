# -*-coding: utf-8 -*-

'''

@author: hekai

@license: (C) Copyright 2013-2018

@contact: 675974119@qq.com

@software: garner

@file: DLList.py

@time: 2018/7/14 14:09

@desc:

'''
from LList1 import LLlist1, LinkedListUnderflow, LNode

class DLNode(LNode):
    def __init__(self, elem, prev=None, next_=None):
        LNode.__init__(self, elem, next_)
        self.prev = prev

class DLList(LLlist1):
    def __init__(self):
        LLlist1.__init__(self)

    def prepend(self, elem):
        p = DLNode(elem, None, self._head)
        if self._head is None:
            self._rear = p
            self._head = p
        else:
            p.next.prev = p
            self._head = p

    def append(self, elem):
        p = DLNode(elem, self._rear, None)
        if self._head is None:
            self._head = p
            self._rear = p
        else:
            p.prev.next = p
            self._rear = p

    def pop(self):
        if self._head is None:
            raise LinkedListUnderflow("in pop")
        e = self._head.elem
        self._head = self._head.next
        if self._head is not None:
            self._head.prev = None
        return e

    def pop_last(self):
        if self._head is None:
            raise LinkedListUnderflow("in pop_last")

        e = self._rear.elem
        self._rear = self._rear.prev
        if self._rear is None:
            self._head = None
        else:
            self._rear.next = None
        return e


if __name__ == "__main__":
    dlist1 = DLList()

    dlist1.prepend(1)
    dlist1.prepend(2)
    dlist1.append(3)
    dlist1.append(4)
    dlist1.printall()

    dlist1.pop()
    dlist1.printall()

    dlist1.pop_last()
    dlist1.printall()
