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


def merge_sort(nums):
    slen, llen = 1, len(nums)
    templst = [None] * llen
    while slen < llen:
        merge_pass(nums, templst, llen, slen)
        slen *= 2
        merge_pass(templst, nums, llen, slen)
        slen *= 2


def merge_pass(lfrom, lto, llen, slen):
    i = 0
    while i + 2 * slen < llen:
        merge(lfrom, lto, i, i + slen, i + 2*slen)
        i += 2 * slen
    if i + slen < llen:
        merge(lfrom, lto, i, i + slen, llen)
    else:
        for j in range(i, llen):
            lto[j] = lfrom[j]


def merge(lfrom, lto, low, mid, high):
    i, j, k = low, mid, low
    while i < mid and j < high:
        if lfrom[i].key <= lfrom[j].key:
            lto[k] = lfrom[i]
            i += 1
        else:
            lto[k] = lfrom[j]
            j += 1
        k += 1
    while i < mid:
        lto[k] = lfrom[i]
        i += 1
        k += 1
    while j < high:
        lto[k] = lfrom[j]
        j += 1
        k += 1



if __name__ == "__main__":
    size = 5
    lst = []
    keys = []
    for i in range(size):
        key = random.randint(1, 100)
        val = random.choice("tomorrow")
        lst.append(record(key, val))
        keys.append(key)

    print str(keys)

    merge_sort(lst)
    for i in lst:
        print str(i.key),