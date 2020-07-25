# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 18:05:12 2020
2、修改列表

问题描述：

lst = [1, [4, 6], True]

请将列表里所有数字修改成原来的两倍

@author: Nobody
"""

lst=[2,5,6,7,8,9,2,9,9]
lst.append(15)
print(lst)

lst=[2,5,6,7,8,9,2,9,9]
lst.insert(int(len(lst)/2),20)
print(lst)

lst=[2,5,6,7,8,9,2,9,9]
lst.extend([2,5,6])
print(lst)

lst=[2,5,6,7,8,9,2,9,9]
lst.pop(3)
print(lst)

lst=[2,5,6,7,8,9,2,9,9]
lst.reverse()
print(lst)

lst=[2,5,6,7,8,9,2,9,9]
lst.sort()
print(lst)

lst=[2,5,6,7,8,9,2,9,9]
lst.sort(reverse=True)
print(lst)
