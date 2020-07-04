#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
Author:Scott.yu
"""

# import random
#
# f = open("data.txt", 'w+')
# for i in range(10):
#     f.write(str(random.randint(1, 100)) + ' ')
# f.seek(0)
# print(f.read())
# f.close()

import os
import random
import string

# def gen_code(len=4):
#     # 随机生成4位验证码
#     li = random.sample(string.ascii_letters + string.digits, len)
#     print(''.join(li))
#
# gen_code()
def create_mac():
    MAC = '01-AF-3B'
    hex_num = string.hexdigits
    for i in range(3):
        n = random.sample(hex_num,2)
        sn = '-' + ''.join(n).upper()
        MAC+=sn
        return MAC

def main():
    with open('mac.txt', 'w+') as f:
        for i in range(10):
            mac = create_mac()
            f.write(mac + '\n')
        f.seek(0)
        data = f.read()
        print(data)


main()
