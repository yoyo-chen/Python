# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 18:05:12 2020

@author: Nobody
"""

import math
# v1,v2,t,s,l=map(int,input().split())
v1,v2,t,s,l=10,5,5,2,20
"""
v1 兔子的速度
v2 乌龟的速度
t  兔子领先t米以上
s  一旦任一秒结束后假如兔子发现自己领先t米以上，就休息s秒
l  总路程
"""

l1=0 #兔子走的路程
l2=0 #乌龟走的路程
l1time=0 #兔子现在走了的时间
l2time=0 #乌龟现在走了的时间

while True:
    if (l1-l2)>=t:
        l2+=s*v2
        l1time+=s
        l2time+=s
    dt1=l1time+(l-l1)/v1 #兔子走到终点所需的时间
    dt2=l2time+(l-l2)/v2 #乌龟走到终点所需的时间
    l1+=v1
    l2+=v2
    l1time+=1
    l2time+=1
    if l1>=l or l2>=l:
        if dt1>dt2:
            print('T')
            print(math.ceil(dt2))
            break
        elif dt1==dt2:
            print('D')
            print(math.ceil(dt1))
            break
        else:
            print('R')
            print(math.ceil(dt1))
            break
            
            