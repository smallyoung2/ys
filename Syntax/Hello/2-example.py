# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 15:29:52 2024

@author: soyoung
"""

#1
a=80
b=75
c=55
mean=(a+b+c)/3
mean

#2
if(13%2==1):
    print("홀수")
else:
    print("짝수")

#3
pin="881120-1068234"
yyyymmdd=pin[:6]
num=pin[7:]
print(yyyymmdd)
print(num)

#4
pin="881120-1068234"
print(pin[7:8])

#5
a="a:b:c:d"
b=a.replace(":","#")
print(b)

#6
a=[1,3,5,4,2]
a.sort()
a.reverse()
print(a)

#7
a=['Life','is','too','short']
result=" " .join(a)
print(result)

#8
a=(1,2,3)
a=a+(4,)
print(a)

#9
a=dict()
a

#10
a={'a':90,'b':80,'c':70}
result=a.pop('b')
print(a)
print(result)

#11
a=[1,1,1,2,2,3,3,3,4,4,5]
aSet=set(a)
b=list(aSet)
print(b)

#12
a=b=[1,2,3]
a[1]=4
print(b)
