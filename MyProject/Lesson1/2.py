#! /usr/bin/env python
# -*- coding:utf-8 -*-

print("hello world")

# name = "scott"
# if "tt" in name:
#     print("ok")
# else:
#     print("Error")
#
# num=4
# print(num.bit_length())
# # int("abc")
# test = "2"
# v1 = test.isdecimal()
# v2 = test.isdigit()
# print(v1,v2)
#
# v3 = test.join("abc")
# print(v3)
# print(len("12ab余书军"))
# for item in range(0, 10):
# #     print(item)
# template = "I am {name}, my age is {age}"
# #v = template.format(name='yushujun', age=19)
# v = template.format(**{"name": "yushujun", "age": 19})
# print(v)
#N = input("Please input number:")
#M = input("Please input number2:")
#string = ""
# for i in range(1, 10):
#     string = ""
#     for j in range(1, i+1):
#         s = str(i) + '*' + str(j) + '=' + str(i*j) + '\t'
#         #print(s)
#         string += s
#     print(string)
#     #break
#
# #print(count)
"""
for i in range(1,10):
    for j in range(1,i+1):
        print(str(i) + "*" + str(j) + "=" + str(i*j), end="\t")
    print()
"""

# for x in range(1,100//5):
    # for y in range(1,100//3):
    #     for z in range(1,101):
    #         if x+y+z == 100 and (5*x +3*y + 1/3*z ==100):
    #             print(x,y,z)
# li_new = []
# li = ['alex', 'eric', 'rain', 123]
# for i in li:
#     li_new += str(i)
# print("_".join(li_new))
tu = ('alex', 'eric', 'rain',)
# for i in tu:
#     print(i,end="\t")
# print()
# for index in range(len(tu)):
#     print(index)

# for index, lem in enumerate(tu, 10):
#     print(index, lem)

# a = [11, 22, 33, 44]
# print(a.index(11))
"""
li = ['alex', 'eric', 'rain']
print(len(li))
a = li.append('seven')
print(a)
for i in enumerate(li, 10):
    print(i)
"""

user_list = []
for i in range(1, 300):
    temp = {"name": "alex" + str(i), "email": "alex" + str(i) + "@live.com", "pwd": "pwd" + str(i)}
    user_list.append(temp)

# for j in user_list:
#     print(j)
while (1):
    s = input("Please input page number:")
    s = int(s)
    if type(s) == int:
        start = (s - 1) * 10
        end = s * 10
        result = user_list[start:end]
        for item in result:
            print(item)
    else:
        print("The value of input is wrong")