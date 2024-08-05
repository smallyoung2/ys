# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 15:18:12 2024

@author: soyoung
"""

#2-7
a=True
b=False

type(a)
type(b)

1==1
2>1
2<1

a=[1,2,3,4]
while a:
    print(a.pop())

if []:
    print("참")
else:
    print("거짓")


if [1,2,3]:
    print("참")
else:
    print("거짓")

bool('python')
bool('')
bool([1,2,3])
bool([])
bool(0)
bool(3)

#2-8

a=1
b="python"
c=[1,2,3]

a=[1,2,3]
id(a)
id(a)
b=a
id(a)
id(b)
b
a is b
a[1]
a[1]=4
a
b

a=[1,2,3]
b=a[:]
a[1]=4
a
b

from copy import copy
a=[1,2,3]
b= copy(a)
b
id(a)
id(b)
b is a

a,b=('python','life')
(a,b)
a
b

a=3
b=5
a,b=b,a
a
b

#1분 코딩
a=[1,2,3]
b=[1,2,3]
a is b
