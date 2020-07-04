#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author:Scott.yu
"""

name = 'alex'


def foo():
    name = 'linhaifeng'

    def bar():
        name = 'wupeiqi'
        print(name)
        # return 123

    return bar


b = foo()()
print(b)
a = foo()
print(a)
a()
