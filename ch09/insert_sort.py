# encoding: utf-8
# !/usr/bin/env python

'''

@author: hekai

@license: (C) Copyright 2013-2017, kylinos.

@contact: hekai@kylinos.com.cn

@software: garner

@file: insert_sort.py

@time: 2019/2/26 16:38

@desc:

'''
from record import record
import random


def insert_sort(lst):
    for i in range(1, len(lst)):
        x = lst[i]
        j = i
        while j > 0 and lst[j-1].key > x.key:
            lst[j] = lst[j-1]
            j -= 1
        lst[j] = x


def insert_sort_1(lst):
    for i in range(1, len(lst)):
        tmp = lst[i]
        j = i
        while j - 1 >= 0 and lst[j-1].key > tmp.key:
            lst[j] = lst[j-1]
            j -= 1
        lst[j] = tmp
    return
if __name__ == "__main__":
    size = 20
    lst = []
    keys = []
    for i in range(size):
        key = random.randint(1, 100)
        val = random.choice("tomorrow")
        lst.append(record(key, val))
        keys.append(key)

    print str(keys)

    insert_sort_1(lst)
    for i in lst:
        print str(i.key),
