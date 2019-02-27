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


def selection_sort(nums):
    min = float("inf")

    for j in range(len(nums)):
        index = 0
        for i in range(1, len(nums)):
            if nums[i].key < min:
                min = nums[i]
                index = i
        tmp = nums[j]
        nums[j] = nums[index]
        nums[index] = tmp
    return


def selection_sort2(nums):

    for i in range(len(nums)-1):
        k = i
        for j in range(i, len(nums)):
            if nums[j].key < nums[k].key:
                k = j
        if k != i:
            nums[k], nums[i] = nums[i], nums[k]
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

    selection_sort2(lst)
    for i in lst:
        print str(i.key),