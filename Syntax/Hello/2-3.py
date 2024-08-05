# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 12:44:22 2024

@author: soyoung
"""

odd=[1,3,5,7,9]
odd
odd[0]

a=[1,2,3]
a[0]+a[2]
a[-1]

a=[1,2,3,['a','b','c']]
a[-1]
a[3]
a[-1][0]

a=[1,2,['a','b',['life','is']]]
a[2][2][0]

a=[1,2,3,4,5]
a[0:2]
a="12345"
a[0:2]

#1분코딩
a=[1,2,3,4,5]
a[1:3]

a=[1,2,3,['a','b','c'],4,5]
a[2:5]
a[3][:2]

#리스트 연산
a=[1,2,3]
b=[4,5,6]
a+b
a*3
len(a)
str(a[2])+"hi"

a[2]=4
a
del a[1]
a
a=[1,2,3,4,5]
del a[2:]
a

#리스트 관련 함수
a=[1,2,3]
a.append(4)
a
a.append([5,6])
a

a=[1,4,3,2]
a.sort()
a
a=['a','d','b','c']
a.sort()
a

a=['a','c','b']
a.reverse()
a

a=[1,2,3]
a.index(3)
a.index(1)
a.index(0)

a.insert(0,4)
a
a.insert(3,5)
a

a=[1,2,3,1,2,3]
a.remove(3)
a
a.remove(3)
a

a=[1,2,3]
a.pop()
a
a=[1,2,3]
a.pop(1)
a

a=[1,2,3,1]
a.count(1)

a=[1,2,3]
a.extend([4,5])
a
b=[6,7]
a.extend(b)
a
