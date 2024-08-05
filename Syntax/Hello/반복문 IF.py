# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 15:21:30 2024

@author: soyoung
"""

i=0
result1=[]
result2=[]
while i<=100:
    i+=1
    if i%3==0:
        result1.append(i)
    elif i%5==0:
        result2.append(i)
    else: continue
    

print(result1)
print(result2)

#1부터 10까지 홀수 합 짝수합
result1=0
result2=0
for i in range(11):
    if i%2==0:
        result1+=i
    else:
        result2+=i
    
print("짝수합 :",result1)
print("홀수합 :",result2)

#구구단 프로그램을 작성하여라
for i in range(2,10):
    for j in range(1,10):
        print(i,"*",j,"=",i*j)
    print(" ")   
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 