# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 18:05:12 2020
2、修改列表

问题描述：

lst = [1, [4, 6], True]

请将列表里所有数字修改成原来的两倍

@author: Nobody
"""

lst=[1, [4, 6], True]
for i in range(len(lst)):
    if type(lst[i])==int or type(lst[i])==float:
        lst[i]=lst[i]*2
print(lst)
