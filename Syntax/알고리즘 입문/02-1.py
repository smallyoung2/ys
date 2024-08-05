# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 11:40:17 2024

@author: soyoung
"""

#2-1
print('학생 그룹 점수의 합계와 평균을 구합니다.')
score1=int(input('1번 학생의 점수를 입력하세요 :'))
score2=int(input('2번 학생의 점수를 입력하세요 :'))
score3=int(input('3번 학생의 점수를 입력하세요 :'))
score4=int(input('4번 학생의 점수를 입력하세요 :'))
score5=int(input('5번 학생의 점수를 입력하세요 :'))

total=0
total+=score1
total+=score2
total+=score3
total+=score4
total+=score5

print(f'합계는 {total}점 입니다.')
print(f'평균은 {total/5}점 입니다.')


#리스트와 튜플 알아보기
list01=[]
list02=[1,2,3]
list03=['a','b','c',]

list04=list()
list05=list('abc')
list06=list([1,2,3])
list07=list((1,2,3))
list08=list({1,2,3})

list09=list(range(7))
list10=list(range(3,8))
list11=list(range(3,13,2))

list12=[None]*5

tuple01=()
tuple02=1,
tuple03=(1,)

tuple04=1,2,3
tuple05=1,2,3,
tuple06=(1,2,3)
tuple07=(1,2,3, )
tuple08='a','b','c'

v01=1
v02=(1)

tuple09=tuple()
tuple10=tuple('abc')
tuple11=tuple([1,2,3])
tuple12=tuple({1,2,3})

tuple13=tuple(range(7))
tuple14=tuple(range(3,8))
tuple15=tuple(range(3,13,2))

x=[1,2,3]
a,b,c=x
a,b,c

#인덱스로 원소에 접근하기
x=[11,22,33,44,55,66,77]
x[2]
x[-3]
x[-4]=3.14
x
x[7]            #x[7] 존재하지않으므로 오류
x[7]=3.14       #x[7] 에는 값을 대입할수 없으므로 오류

#슬라이스식으로 원소에 접근하기
s=[11,22,33,44,55,66,77]
s[0:6]
s[0:7]
s[0:7:2]
s[-4:-2]
s[3:1]          #[] 출력 , 오류는 

s[::2]          # 맨앞부터 2개씩 건너뛰며 출력 [11, 33, 55, 77]
s[::-1]         # 리스트 s의 맨끝부터 전부 출력 [77, 66, 55, 44, 33, 22, 11]

x=0
type(x+1)
type(x=17)

a=b=1

#자료구조의 개념 알아보기
x=[15,64,7,3.14,[32,55],'abc']
len(x)
if x:
    #x가 비어있지 않으면 (True)실행
    print("true")
else:
    #x가 비어있으면 (False)실행
    print("false")
    
[1,2,3]==[1,2,3]
[1,2,3]<[1,2,4]    
[1,2,3,4]==[1,2,3,4]
[1,2,3]<[1,2,3,5]
[1,2,3]<[1,2,3,5]<[1,2,3,5,6]


numbers=[1,2,3,4,5]
twice=[num*2 for num in numbers if num%2==1]
print(twice)
