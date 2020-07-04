#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author:Scott.yu
"""

from functools import reduce

num_l = [1, 2, 3, 100]
res = reduce(lambda x, y: x+y, num_l)
print(res)