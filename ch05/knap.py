# encoding: utf-8
# !/usr/bin/env python

'''

@author: hekai

@license: (C) Copyright 2013-2017, kylinos.

@contact: hekai@kylinos.com.cn

@software: garner

@file: knap.py.py

@time: 2019/1/24 10:09

@desc:

'''

def knap_rec(weight, wlist, n):
    if weight == 0:
        return True
    if weight < 0 or (weight > 0 and n < 1):
       return False
    if knap_rec(weight-wlist[n-1], wlist,n-1):
        print "Item" + str(n) + ":" + str(wlist[n-1])
        return True
    if knap_rec(weight, wlist, n-1):
        return True
    else: return False

if __name__ == "__main__":
    weight = 45
    wlist = [1,2,3,4,5,6,7,8,9,10,30]
    n = 11
    print knap_rec(weight, wlist, n)