# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 15:52:14 2020

@author: Nobody
"""

import random
target = random.randint(0, 100)

print("猜测一个0到100之间的整数。")
i=0
while True:
    i=i+1
    temp = input("第"+ str(i) +"次猜，请输入一个整形数字：")
    try:
    	guess = int(temp)
    except TypeError:
        print("输入无效")   
    else:
    	if guess > target:
        	print("Large")
    	elif guess == target:
            print("Bingo!")
            break
        elif guess < target:
            print("Small")
print("Game over")