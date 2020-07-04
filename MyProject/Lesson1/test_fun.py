#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author:Scott.yu
"""


def test(x, *args, **kwargs):
    """
    This function is used to test and calculated y
    :param x: should be used int type
    :return: according to x, it will be return y
    """
    print(x)
    print(args)
    print(kwargs)
    #return "ok"

test(1, *[2, 3, 4], name='alex', age=19)
#print(res)

