# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 10:48:02 2024

@author: soyoung
"""

#1
def is_odd(number):
    if number%2==1:
        return True
    else:
        return False
is_odd(3)

#2
def avg_numbers(*args):
    result=0
    for i in args:
        result+=i
    return result/len(args)
avg_numbers(1,2)
avg_numbers(1,2,3,4,5)

#3
input1=input("첫번째 숫자를 입력하세요: ")
input2=input("두번째 숫자를 입력하세요: ")
total=int(input1)+int(input2)
print("두수의 합은 %s입니다." %total)

#4
print("you""need""python")
print("you"+"need"+"python")
print("you","need","python")
print("".join(["you","need","python"]))

#5
f1=open("test.txt",'w')
f1.write("life is too short")
f1.close()

f2=open("test.txt",'r')
print(f2.read())
f2.close()

#6
user_input=input("저장할 내용을 입력하세요 : ")
f=open('test.txt','a')
f.write(user_input)
f.write("\n")
f.close()
