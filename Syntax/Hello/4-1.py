# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 17:21:29 2024

@author: soyoung
"""

def add(a,b):
    return a+b
a=3
b=4
c=add(a,b)
print(c)

a=add(3,4)
print(a)

def say():
    return "hi"

a=say()
print(a)

def add(a,b):
    print("%d, %d의 합은 %d입니다." %(a,b,a+b))

a=add(3,4)
print(a)

say()

def sub(a,b):
    return a-b
result=sub(a=7,b=3)
print(result)

result=sub(b=5,a=3)
print(result)

def add_many(*args):
    result=0
    for i in args:
        result += i
    return result
result=add_many(1,2,3)
print(result)

result=add_many(1,2,3,4,5,6,7,8,9,10)
print(result)

def add_mul(choice,*args):
    if choice =="add":
        result=0
        for i in args:
            result+=i
    elif choice =="mul":
        result=1
        for i in args:
            result=result*i
    return result

result=add_mul('add',1,2,3,4,5)
print(result)

result=add_mul("mul",1,2,3,4,5)
print(result)

def print_kwargs(**kwargs):
    print(kwargs)
    
print_kwargs(a=1)
print_kwargs(name='foo',age=3)

#함수의 리턴값은 언제나 하나이다.
def add_and_mul(a,b):
    return a+b,a*b
result=add_and_mul(3,4)
print(result)

result1,result2=add_and_mul(3,4)
print(result1)
print(result2)

def add_and_mul(a,b):
    return a+b
    return a*b

def say_nick(nick):
    if nick=="바보":
        return 
    print("나의 별명은 %s입니다." %nick)

say_nick('야호')
say_nick('바보')

def say_myself(name,age,man=True):
    print("나의 이름은 %s입니다."%name)
    print("나이는 %d살입니다."%age)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")
        
say_myself("박응용",27)
say_myself("박응용",27,True)
say_myself("박응신",27,False)

a=1
def vartest(a):
    a=a+1
    return a
vartest(a)
print(a)

vartest(3)
print(a)

a=vartest(a)
print(a)

a=1
def vartest():
    global a
    a=a+1
vartest()
print(a)

# 람다 에약어
add= lambda a,b:a+b
result=add(3,4)
print(result)

def add(a,b):
    return a+b
result=add(3,4)
print(result)
