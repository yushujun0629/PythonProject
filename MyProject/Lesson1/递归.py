#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author:Scott.yu
"""


# def fib_recur(n):
#   assert n >= 0, "n > 0"
#   if n <= 1:
#     return n
#   return fib_recur(n-1) + fib_recur(n-2)
#
# for i in range(1, 20):
#     print(fib_recur(i), end=' ')
# def fib_loop(n):
#   a, b = 0, 1
#   for i in range(n + 1):
#     a, b = b, a + b
#   return a
#
#
# for i in range(20):
#   print(fib_loop(i), end=' ')
a = 0
b = 1
def Fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return Fibo(n) + Fibo(n - 1)

print(Fibo(4))