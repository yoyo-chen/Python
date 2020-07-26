# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 18:05:12 2020

leetcode 852题 山脉数组的峰顶索引
如果一个数组k符合下面两个属性，则称之为山脉数组
数组的长度大于等于3
存在$i$，$i$ >0 且$i<\operatorname{len}(k)-1$， 使得$$\mathrm{k}[0]<\mathrm{k}[1]<\ldots<\mathrm{k}[\mathrm{i}-1]<\mathrm{k}[\mathrm{j}]>\mathrm{k}[\mathrm{i}+1] \ldots>\mathrm{k}[\operatorname{len}(\mathrm{k})-1]$$
这个$i$就是顶峰索引。
现在，给定一个山脉数组，求顶峰索引。

示例:
输入：[1, 3, 4, 5, 3]
输出：True
输入：[1, 2, 4, 6, 4, 5]
输出：False

@author: Nobody
"""
a, b=1, 2