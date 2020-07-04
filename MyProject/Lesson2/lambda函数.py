#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author:Scott.yu
"""

# score = input("input score:")
#
# print(str(score) + 'belongs to' + (lambda x:(x>=90 and 'A' or x>=60 and 'B' or 'C'))(score))

# factors = lambda x: filter( lambda i: x%i==0 and i,range(1,x))
# f = lambda x: sum(factors(x)) == x
# print([(i,list(factors(i))) for i in list(filter(f, range(2,1001)))])

# test = lambda x: x%2 == 0 and 7
# # print(test())
# #
# # print(3 and 3)


# test = lambda x:x+' love money'
# res = test('yushujun')
# print(res)

# a = 1
# def test(x):
#     global a
#     a = x
#     return a
# test(2)
# print(a)
def foo(n):
    print(n)

def bar(name):
    print("my name is %s" %name)
    return bar

foo(bar('yushujun'))