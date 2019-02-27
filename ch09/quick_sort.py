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


def quick_sort(nums):
    quick_rec2(nums, 0, len(nums) - 1)

def quick_rec(nums, start, end):
    if start >= end:
        return
    i = start
    j = end
    pivot = nums[start]
    while i < j:
        while i < j and nums[j].key >= pivot.key:
            j -= 1
        if i < j:
            nums[i] = nums[j]
            i += 1
        while i < j and nums[i].key <= pivot.key:
            i += 1
        if i < j:
            nums[j] = nums[i]
            j -= 1
        nums[i] = pivot
        quick_rec(nums, start, i - 1)
        quick_rec(nums, i + 1, end)


def quick_rec2(nums, start, end):
    if start >= end:
        return
    pivot = nums[start]
    i = start

    for j in range(i+1, end + 1):
        if nums[j] < pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[start],  nums[i] = nums[i], nums[start]

    quick_rec(nums, start, i - 1)
    quick_rec(nums, i + 1, end)


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

    quick_sort(lst)
    for i in lst:
        print str(i.key),