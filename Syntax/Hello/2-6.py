# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 14:23:30 2024

@author: soyoung
"""

s1=set([1,2,3])
s1
s2=set("hello")
s2

l1=list(s1)
l1
l1[0]

t1=tuple(s1)
t1
t1[0]

s1=set([1,2,3,4,5,6])
s2=set([4,5,6,7,8,9])

s1&s2
s1.intersection(s2)

s1|s2
s1.union(s2)

s1-s2
s2-s1
s1.difference(s2)
s2.difference(s1)

s1=set([1,2,3])
s1.add(4)
s1

s1=set([1,2,3])
s1.update([4,5,6])
s1

s1.remove(4)
s1
