# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 16:35:30 2024

@author: soyoung
"""

test_list=['one','two','three']
for i in test_list:
    print(i)

a=[(1,2),(3,4),(5,6)]
for (first,last) in a:
    print(first+last)
    
marks=[90,25,67,45,80]

number=0
for mark in marks:
    number=number+1
    if mark>=60:
        print("%d번 학생은 합격입니다." %number)
    else:
        print("%d번 학생은 불합격 입니다." %number)
        
    number=0
for mark in marks:
    number=number+1
    if mark<60:
        continue
    print("%d번 학생 축하합니다. 합격입니다." %number)

a=range(10)
a
a=range(1,11)
a

add=0
for i in range (1,11):
    add=add+i
print(add)

for number in range(len(marks)):
    if marks[number]<60:
        continue
    print("%d번 학생 축하합니다. 합격입니다." % (number+1))
    
#1분코딩
add=0
for i in range(1,101):
    add=add+i
print(add)

for i in range(2,10):
    for j in range(1,10):
        print(i ,"*", j ,"=",  i*j, end="  ")
    print("  ")
    
a=[1,2,3,4]
result=[]
for num in a:
    result.append(num*3)
print(result)

result=[num*3 for num in a]
print(result)

result=[num*3 for num in a if num%2 ==0]
print(result)

result=[x*y for x in range(2,10)
            for y in range(1,10)]
print(result)
