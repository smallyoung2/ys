# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 14:28:38 2024

@author: soyoung
"""


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

#한줄에 여러 변수 선언 가능 
#(unpacking) 개별 자료형 갖게된다. 튜플 x
a,b,c=10,20,'END'
d,e,f=(10,20,'END')
print(type(a))          # a,b int,  c str
print(type(f))          # d,e int,  f str

#튜플 (1,3,5,7,9)에서 인덱스 2번째 값 5를 10으로 바꿔라.
c=(1,3,5,7,9)
t1=c[0:2]
t2=c[3:5]
print(t1+(10,)+t2)


tv=10   #바꿀 값
tx=2    #바꿀 위치
tp=(1,3,5,7,9)

#튜플을 리스트 객체로 만든 후에 다시 튜플 객체로 전환
tl=list(tp)
tl[tx]=tv
tp=tuple(tl)
print(tp)
