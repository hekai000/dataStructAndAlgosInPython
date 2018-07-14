# -*-coding: utf-8 -*-

'''

@author: hekai

@license: (C) Copyright 2013-2018

@contact: 675974119@qq.com

@software: garner

@file: LCList.py.py

@time: 2018/7/14 10:02

@desc:

'''
from LList import LNode, LinkedListUnderflow
class LCList:
    def __init__(self):
        self._rear = None

    def is_empty(self):
        return self._rear is None

    def prepend(self,elem):
        p = LNode(elem)
        if self._rear is None:
            p.next = p
            self._rear = p
        else:
            p.next = self._rear.next
            self._rear.next = p
    def append(self, elem):
        self.prepend(elem)
        self._rear = self._rear.next

    def pop(self):
        if self._rear is None:
            raise LinkedListUnderflow("in pop")
        p = self._rear.next

        if self._rear is p:
            self._rear = None
        else:
            self._rear.next = p.next
        return p.elem

    def printall(self):
        if self.is_empty():
            return

        p = self._rear.next
        while True:
            print p.elem
            if p is self._rear:
                break
            p = p.next

    def pop_last(self):
        if self.is_empty():
            raise LinkedListUnderflow("in pop_last")
        p = self._rear.next
        if p is self._rear:
            self._rear = None
            return p.elem
        else:
            e = self._rear.elem
            while True:
                if p.next is self._rear:
                    break
                p = p.next
            p.next = self._rear.next
            self._rear = p
            return e
if __name__ == "__main__":
    clist1 = LCList()
    clist1.append(1)
    clist1.append(2)
    clist1.append(3)
    clist1.append(4)
    clist1.printall()
    print clist1.pop_last()
    clist1.printall()
    print clist1.pop_last()
    clist1.printall()
    print clist1.pop_last()
    clist1.printall()
    print clist1.pop_last()
    clist1.printall()