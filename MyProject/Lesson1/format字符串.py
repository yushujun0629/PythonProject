#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author:Scott.yu
"""
# 需要一一对应，少一个都不行
# tpl = "I am {}, age {}, {}".format('seven', 18, 'alex')
# print(tpl)

# 可以只取一部分
# tpl = "I am {2}, age {1}".format('seven', 18, 'alex')
# print(tpl)

tpl = "I am {name}, age {age}, really {name}".format(name = 'alex',age = 18)
print(tpl)