#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author:Scott.yu
"""

num_l = [1, 2, 10, 5, 3, 7]


def add_one(x):
    return x+1


def reduce_one(x):
    return x-1

def chengfang(x):
    return x**2

a = map(add_one, num_l)
print(a)
print(list(a))

res1 = map(lambda x: x-1, num_l)
print(res1)
print(list(res1))

res2 = map(lambda x: x**2, num_l)
print(list(res2))

res3 = map(lambda x: x.upper(), "yushujun")
print(list(res3))