# encoding: utf-8
# !/usr/bin/env python

'''

@author: hekai

@license: (C) Copyright 2013-2017, kylinos.

@contact: hekai@kylinos.com.cn

@software: garner

@file: selection_sort.py

@time: 2019/2/27 10:05

@desc:

'''

import random
from record import record


def radix_sort(lst, d):
    rlists = [[] for i in range(10)]

    llen = len(lst)

    for m in range(-1, -d-1, -1):
        for j in range(llen):
            rlists[lst[j].key[m]].append(lst[j])
        j = 0
        for i in range(10):
            tmp = rlists[i]
            for k in range(len(tmp)):
                lst[j] = tmp[k]
                j += 1
            del rlists[i][:]






if __name__ == "__main__":
    size = 5
    lst = []
    keys = []
    for i in range(size):
        key = (random.randint(0, 9), random.randint(0, 9), random.randint(0, 9))
        val = random.choice("tomorrow")
        lst.append(record(key, val))
        keys.append(key)

    print str(keys)

    radix_sort(lst, 3)
    for i in lst:
        print str(i.key),