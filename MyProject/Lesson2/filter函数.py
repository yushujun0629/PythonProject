#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author:Scott.yu
"""

movie_people = ['sb_alex', 'sb_wupeiqi', 'sb_yuanhao', 'linhaifeng']
def sb_show(name):
    return name.startswith('sb')


def filter_test(func, array):
    res = []
    for item in array:
        if not func(item):
            res.append(item)
    return res
#
a = filter_test(sb_show, movie_people)
print(a)
res1 = filter(lambda n: n.startswith('sb'), movie_people)
res2 = map(lambda n: n.startswith('sb'), movie_people)
print(list(res1))
print(list(res2))