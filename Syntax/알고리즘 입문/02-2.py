# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 12:16:15 2024

@author: soyoung
"""


"""
def max_of(a):
    maximum=a[0]
    for i in range(1,len(a)):
        if a[i]>maximum:
            maximum=a[i] """
            
#2-2 시퀀스 원소의 최댓값 출력하기
from typing import Any,Sequence
def max_of(a:Sequence)->Any:
    maximum=a[0]
    for i in range(1,len(a)):
        if a[i]>maximum:
            maximum=a[i]
    return maximum

if __name__ =='__main__':
    print('배열의 최댓값을 구합니다.')
    num=int(input('원소 수를 입력하세요 :'))
    x=[None] *num
    
    for i in range(num):
        x[i]=int(input(f'x[{i}]값을 입력하세요 :'))
    print(f'최댓값은 {max_of(x)}입니다. ')
    
#2-3 배열 원소의 최댓값을 구해서 출력하기(원소값을 입력받음) 디버그하기!!
from max1 import max_of
print('배열의 최댓값을 구합니다')
print("주의 :'end'를 입력하면 종료합니다. ")
number=0
x=[]
while True:
    s=input(f'x[{number}]값을 입력하세요 :')
    if s=='end':
        break
    x.append(int(s))
    number+=1
    
print(f'{number}개를 입력했습니다. ')
print(f'최댓값은 {max_of(x)}입니다. ')

#2-4 배열원소의 최댓값을 구해서 출력하기(원소값을 난수로 생성)
import random
from max1 import max_of

print("난수의 최댓값을 구합니다. ")
num=int(input('난수의 개수를 입력하세요 :'))
lo=int(input('난수의 최소값을 입력하세요 :'))
hi=int(input('난수의 최댓값을 입력하세요 :'))
x=[None]*num

for i in range(num):
    x[i]=random.randint(lo,hi)
    
print(f'{(x)}')
print(f'이 가운데 최댓값은 {max_of(x)}입니다.')

#2-5 각 배열 원소의 최댓값을 구해서 출력하기(튜플,문자열,문자열 리스트)
from max1 import max_of
t=(4,7,5.6,2,3.14,1)
s='string'
a=['dts','aac','flac']

print(f'{t}의 최댓값은 {max_of(t)}입니다. ')
print(f'{s}의 최댓값은 {max_of(s)}입니다. ')
print(f'{a}의 최댓값은 {max_of(a)}입니다. ')


#리스트와 튜플2
lst1=[1,2,3,4,5]
lst2=[1,2,3,4,5]
lst1 is lst2            #false

lst1=[1,2,3,4,5]
lst2=lst1
lst1 is lst2            #true

lst1[2]=9
lst1
lst2                    #lst1이 바뀌면 lst2도 바뀐다.

lst2[2]=4
lst1
lst2                    #lst2이 바뀌면 lst1도 바뀐다.


#리스트 스캔
#리스트의 모든원소를 스캔하기(원소 수를 미리 파악)
x=['john','george','paul','ringo']
for i in range(len(x)):
    print(f'x[{i}]={x[i]}')
for i in range(len(x)):
    print("x[%d]=" %i,x[i])
    
#리스트의 모든 원소를 enumerate()함수로 스캔하기
x=['john','george','paul','ringo']

for i ,name in enumerate(x):
    print(f'x[{i}] = {name}')
    
#리스트의 모든 원소를 enumerate()g함수로 스캔하기(1부터 카운트)
x=['john','george','paul','ringo']
for i,name in enumerate(x,1):
    print(f'{i}번째 = {name}')
    
#리스트의 모든 원소를 스캔하기(인덱스 값을 사용하지 않음)
x=['john','george','paul','ringo']
for i in x:
    print(i)
    
#튜플의 스캔
x=('john','george','paul','ringo')
for i in range(len(x)):
    print(f'x[{i}]={x[i]}')

for i, name in enumerate(x):
    print(f'x[{i}] = {name}')
    
for i, name in enumerate(x, 1):
    print(f'{i} 번째 = {name}')
    
for i in x:
    print(i)
    
#2-6 뮤터블 시퀀스 원소를 역순으로 정렬
from typing import Any,MutableSequence

def reverse_array(a:MutableSequence)->None:
    n=len(a)
    for i in range(n//2):
        a[i],a[n-i-1]=a[n-i-1],a[i]
        
if __name__=='__main__':
    print('배열 원소를 역순으로 정렬합니다.')
    nx=int(input('원소수를 입력하세요 :'))
    x=[None]*nx
    
    for i in range(nx):
        x[i]=int(input(f'x[{i}]값을 입력하세요 : '))
    reverse_array(x)
    
    print('배열 원소를 역순으로 정렬했습니다. ')
    for i in range(nx):
        print(f'x[{i}]={x[i]}')
        
        
x.reverse()
print(x)
x.reverse()
print(x)
y=list(reversed(x))
print(y)


#2-7a
#10진수 정숫값을 입력받아 2~34진수로 변환하여 출력하기
def card_conv(x:int,r:int)->str:
    """정숫값 x를 r진수로 변환한뒤 그 수를 나타내는 문자열 반환"""
    d=''
    dchar='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    while x>0:
        d+=dchar[x%r]
        x//=r
    return d[::-1]

if __name__=='__main__':
    print('10진수를 n진수로 변환합니다.')
    
    while True:
        while True:
            no=int(input('변환할 값으로 음이 아닌 정수를 입력하세요'))
            if no>0:
                break
            
        while True:
            cd=int(input('어떤 진수로 변환할까요? ; '))
            if 2<= cd <=36:
                break
        print(f'{cd}진수로는 {card_conv(no,cd)}입니다. ')
        
        retry=input('한번 더 변환 할까요? (Y/N) : ')
        if retry in {'N','n'}:
            break
        
#%%
def card_conv(x:int,r:int)->str:
    """정숫값 x를 r진수로 변환한뒤 그 수를 나타내는 문자열 반환"""
    d=''
    dchar='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    n=len(str(x))
    
    print(f'{r:2} | {x:{n}d}')
    while x>0:
        print('  +'+(n+2)*'-')
        if x//r:
            print(f'{r:2} | {x//r:{n}d} --- {x%r}')
        else:
            print(f'    {x//r:{n}d} --- {x%r}')
        d+=dchar[x%r]
        x//=r
    return d[::-1]

if __name__=='__main__':
    print('10진수를 n진수로 변환합니다.')
    
    while True:
        while True:
            no=int(input('변환할 값으로 음이 아닌 정수를 입력하세요'))
            if no>0:
                break
            
        while True:
            cd=int(input('어떤 진수로 변환할까요? ; '))
            if 2<= cd <=36:
                break
        print(f'{cd}진수로는 {card_conv(no,cd)}입니다. ')
        
        retry=input('한번 더 변환 할까요? (Y/N) : ')
        if retry in {'N','n'}:
            break
        
#1부터 n까지 정수의 합 구하기
def sum_1ton(n):
    s=0
    while n>0:
        s+=n
        n+=-1
    return s
x=int(input('x의 값을 입력하세요 : '))
print(f'1부터 {x}까지의 정수의 합은 {sum_1ton(x)}입니다.')

#리스트에서 임의의 원솟값을 업데이트하기
def change(lst,idx,val):
    """lst[idx]의 값을 val로 업데이트"""
    lst[idx]=val
    
x=[11,22,33,44,55]
print('x=',x)
 
index=int(input('업데이트 할 인덱스를 선택하세요 :'))
value=int(input('새로운 값을 입력하세요 : '))

change(x,index,value)
print(f'x={x}')


#2-8 1000이하의 소수를 나열하기
counter=0                           #나눗셈 횟수를 카운트
for n in range(2,1000001):
    for i in range(2,n):
        counter+=1
        if n%i==0:
            break
    else:
        print(n)
print(f'나눗셈을 실행한 횟수 : {counter}')

#2-9 1000이하의 소수를 나열하기 (알고리즘 개선1)
counter=0                       #나눗셈 횟수 카운트
ptr=0                           #이미 찾은 소수의 갯수
prime=[None]*500                #소수를 저장하는 배열

prime[ptr]=2                    #2는 소수이므로 초깃값으로 지정
ptr+=1
for n in range(3,1001,2):       #홀수만을 대상으로 설정(짝수는 소수 아니므로)
    for i in range(1,ptr):      #이미 찾은 소수로 나눔
        counter+=1
        if n%prime[i]==0:       #나누어떨어지면 소수 아님.->반복 중단
            break
    else:                       #끝까지 나누어 떨어지지 않았다면 소수로 배열에 등록
        prime[ptr]=n
        ptr+=1
        
for i in range(ptr):            #ptr 의 소수 를 출력
    print(prime[i])
print(f'나눗셈을 실행한 횟수 : {counter}')    


#2-10 1000이하의 소수를 나열하기(알고리즘 개선2)
counter=0
ptr=0
prime=[None]*500

prime[ptr]=2                        #2는 소수 prime[0]=2
ptr+=1
prime[ptr]=3                        #3은 소수 prime[1]=3
ptr+=1

for n in range(5,1001,2):
    i=1
    while prime[i]*prime[i]<=n:
        counter+=2
        if n%prime[i]==0:
            break
        i+=1
    else:
        prime[ptr]=n
        ptr+=1
        counter+=1
        
for i in range(ptr):
    print(prime[i])
print(f'곱셈과 나눗셈을 실행한 횟수 :{counter}')


#자료형을 정하지 않은 리스트 원소 확인하기
x=[15,64,7,3.14,[32,55],'abc']
for i in range(len(x)):
    print(f'x[{i}] = {x[i]}')
    
#리스트의 원소와 복사
x=[[1,2,3],[4,5,6]]         #얕은 복사
y=x.copy()
x[0][1]=9
x                           #x와 y의 값 같음
y


import copy                 #깊은 복사
x=[[1,2,3],[4,5,6]]      
y=copy.deepcopy(x)
x[0][1]=9
x                           #x와 y의 값 다름
y

