# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 11:17:35 2024

@author: soyoung
"""

result=0
def add(num):
    global result
    result+=num
    return result
print(add(3))
print(add(4))

result1=0
result2=0

def add1(num):
    global result1
    result1+=num
    return result1
def add2(num):
    global result2
    result2+=num
    return result2

print(add1(3))
print(add1(8))
print(add2(3))
print(add2(10))

class calculator:
    def __init__(self):
        self.result=0
    def add(self,num):
        self.result+=num
        return self.result
    def sub(self,num):
        self.result-=num
        return self.result
    
cal1=calculator()
cal2=calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))
       
class cookie:
    pass           
a=cookie()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
b=cookie()

#사칙 연산 클래스 만들기
class fourcal:
    def __init__(self,first,second):
        self.first=first
        self.second=second
    def setdata(self,first,second):
        self.first=first
        self.second=second
    def add(self):
        result=self.first+self.second
        return result
    def mul(self):
        result=self.first*self.second
        return result
    def sub(self):
        result=self.first-self.second
        return result
    def div(self):
        result=self.first/self.second
        return result
a=fourcal()
type(a)
a.setdata(4,2)

a.first
a.second

b=fourcal()
b.setdata(3,8)

b.first
b.second

a.add()
b.add()

a.mul()
b.mul()

a.sub()
b.sub()

a.div()
b.div()

#생성자 __init__추가 후
a=fourcal()
a=fourcal(4,2)

a.first
a.second

#클래스 상속
class morefourcal(fourcal):
    pass
a=morefourcal(4,2)
a.add()
a.mul()
a.sub()
a.div()

class morefourcal(fourcal):
    def pow(self):
        result=self.first ** self.second
        return result
    
a=morefourcal(4,2)
a.pow()
a.add()


class safefourcal(fourcal):
    def div(self):
        if self.second==0:
            return 0
        else:
            return self.first/self.second
        
a=safefourcal(4,0)
a.div()

#클래스 변수
class family:
    lastname="김"
    
family.lastname
a=family()
b=family()
a.lastname
b.lastname

family.lastname="박"
a.lastname
b.lastname

a.lastname="최"
b.lastname
family.lastname
