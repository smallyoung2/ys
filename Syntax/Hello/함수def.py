# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 09:10:55 2024

@author: soyoung
"""

#함수(function)
#함수는 호출하기 전에 정의가 되어있어야한다
#함수의 리턴값이 없는 경우 리턴값을 받으면 None이다
#함수 정의에서 리턴값이 없으면 return 을 생략하면 된다
#함수 정읭에서 파라미터가 없으면 함수() 형태로 파라미터를 생략한다.

#함수 장점
#1.모듈화:기능별로 분리
#2.블랙박스화:처리과정보다는 결과
#3.코드의 재사용

#매개변수와 인수
#매개변수(parameter):함수에 입력으로 전달된 값을 받는 변수,함수정의
#인수(arguments):함수를 호출할때 전달하는 입력값

def hello():
    print("hello, world!")
    
hello()

#문제 
#함수를 이용하여 사칙연산 계산기를 만들어라
#계산기능 : 더하기,빼기,나누기,곱하기,나머지,제곱
#총합 누적, 평균
#히스토리(이력)

class calculator():
    def __init__(self):
        self.value=0
    def add(self,val):
        self.value+=val
        print(self.value,"+",val,"=",self.value)
    def minus(self,val):
        self.value-=val
    def div(self,val):
        self.value/=val
    def multi(self,val):
        self.value*=val
    def pows(self,val):
        self.value**=val
    def rest(self,val):
        self.value%=val
        
