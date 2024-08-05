# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 16:55:41 2024

@author: soyoung
"""

#chap3 되새김 문제

#1
a="life is too short, you need python"

if "wife" in a :print ("wife")
elif "python" in a and " you" not in a :print("python")
elif "shirt" not in a : print("shirt")
elif "need" in a : print("need")
else:print("none")

#2
result=0
i=1
while i<=1000:
    if i%3==0:
        result+=i
    i+=1
print(result)

#3
i=0
while True:
    i+=1
    if i>5 :break
    print("*"*i )

#4
for i in range(1,101):
    print(i)
    
#5
a=[70,60,55,75,95,90,80,80,85,100]
len(a)
total=0
for score in a:
    total+=score
average=total/len(a)
print(average)

#6
numbers=[1,2,3,4,5]
result=[]
for n in numbers:
    if n % 2 ==1:
        result.append(n*2)
print(result)

numbers=[1,2,3,4,5]
result=[num*2 for num in numbers if num %2 ==1]
print(result)
