#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author:Scott.yu
"""

"""
如果函数中的变量没有global关键字，优先读取局部变量，然后读取全局变量，无法对全局变量的内容做修改
如果函数中有global关键字，局部中的变量名本质上就是全局的那个变量，可读取，可修改。
代码规范：全局变量都大写，局部变量都小写
"""
NAME = "yushujun"  # this is global variable


# def change_name():
#     # name = "hello"
#     # global name
#     name = "hello world"
#     print(name)
#
# """
# nolocal 指的是上一级变量
# """
# change_name()

