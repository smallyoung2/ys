# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 14:28:38 2024

@author: soyoung
"""

odd=[1,3,5,7,9]
olen=len(odd)
print(olen)

lst=[1,3,5,['a','b','c']]
print(lst,len(lst))
print('count: ',len(lst))

print(type(lst))
print(type(lst[0]))
print(type(lst[-1]))

#빈튜플 생성
t0=()
te=tuple()
print(type(t0))         #<class 'tuple'>

#소괄호는 연산자 우선순위를 적용하여 튜플로 인식x
t1=(1)
t2=((99+1)*2)
print(type(t1),t1)      #<class 'int'> 1

#요소가 1개인 경우 반드시 요소 뒤에 콤마 
t99=(99,)
print(type(t99),t99)    #<class 'tuple'> (99,)

#요소가 2개 이상긴 경우 콤마 붙일 필요x
t3=(1,2,3)
t4=(4,5,6,)             #<class 'tuple'>

#소괄호 생략 가능
tex1=5,
tex2=10,20,30
tex3=1,3,5,7
print(type(tex1))       #<class 'tuple'>
print(type(tex2))
