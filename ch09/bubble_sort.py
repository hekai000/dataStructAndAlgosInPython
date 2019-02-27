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


def bubble_sort(nums):
    for i in range(len(nums)):
        found = False
        for j in range(1, len(nums) - i):
            if nums[j-1].key > nums[j].key:
                nums[j-1], nums[j] = nums[j], nums[j-1]
                found = True
        if not found:
            break
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

    bubble_sort(lst)
    for i in lst:
        print str(i.key),