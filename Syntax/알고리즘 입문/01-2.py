# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 10:03:51 2024

@author: soyoung
"""

#1-7
print('1부터 n까지의 정수의 합을 구합니다. ')
n=int(input('n의 값을 입력하세요 : '))

sum=0
i=1
while i<=n:
    sum+=i
    i+=1
print(f'1부터 {n}까지 정수의 합은 {sum}입니다.')
print(f'i의 값은 {i}입니다.')

#1-8
print('1부터 n까지의 정수의 합을 구합니다. ')
n=int(input('n의 값을 입력하세요 : '))

sum=0
for i in range(1,n+1):
    sum+=i
print(f'1부터 {n}까지 정수의 합은 {sum}입니다.')

#가우스 덧셈 방법
print('1부터 n까지의 정수의 합을 구합니다. ')
n=int(input('n의 값을 입력하세요 : '))

sum=n*(n+1)//2
print(f'1부터 {n}까지 정수의 합은 {sum}입니다.')


#1-9
print('a부터 b까지의 정수의 합을 구합니다. ')
a=int(input('정수 a의 값을 입력하세요: '))
b=int(input('정수 b의 값을 입력하세요: '))

if a>b:
    a,b=b,a                 # a와 b의 값을 교환(단일 대입문 사용)
sum=0
for i in range(a,b+1):
    sum+=i
    
print(f'1부터 {n}까지 정수의 합은 {sum}입니다.')


#1-10
print('a부터 b까지의 정수의 합을 구합니다. ')
a=int(input('정수 a의 값을 입력하세요: '))
b=int(input('정수 b의 값을 입력하세요: '))

if a>b:
    a,b=b,a                 # a와 b의 값을 교환(단일 대입문 사용)
sum=0
for i in range(a,b+1):
    if i<b:
        print(f'{i} + ',end='')
    else:
        print(f'{i} = ',end='')
    sum+=i
print(sum)


#1-11 10번에 비해서 효율이 높음.
print('a부터 b까지의 정수의 합을 구합니다. ')
a=int(input('정수 a의 값을 입력하세요: '))
b=int(input('정수 b의 값을 입력하세요: '))

if a>b:
    a,b=b,a                 # a와 b의 값을 교환(단일 대입문 사용)
sum=0
for i in range(a,b):
    print(f'{i} + ',end='')
    sum+=i
print(f'{b} = ',end='')
sum+=b
print(sum)


#1-12
print('+와 -를 번갈아 출력합니다.')
n=int(input('몇개를 출력할까요? : '))

for i in range(n):
    if i%2:                     #i%2==1 이므로 i가 홀수이면 - 출력
        print('-',end='')
    else:                       #i%2==0 이므로 i가 짝수이면 + 출력
        print('+',end='')

#1-13
print('+와 -를 번갈아 출력합니다.')
n=int(input('몇개를 출력할까요? : '))

for _ in range(n//2):           # _ 는 for문에서 인덱스값이 필요없기때문에 사용
    print('+-',end='')
if n%2==1:
    print('+',end='')
    
    
#1-14
print('*를 출력합니다.')
n=int(input('몇개를 출력할까요? :'))
w=int(input('몇개마다 줄바꿈 할까요? :'))

for i in range(1,n+1):
    print('*',end='')
    if i%w==0:
        print()
if n%w:
    print()
    

#1-15
print('*를 출력합니다.')
n=int(input('몇개를 출력할까요? :'))
w=int(input('몇개마다 줄바꿈 할까요? :'))

for _ in range(n//w):       #몫 만큼 줄 생성
    print("*"*w)

rest=n%w
if rest:                    #나머지만큼 * 생성
    print('*'*rest)
    
    
#1-16
print('1부터 n까지 정수의 합을 구합니다.')
while True:
    n=int(input('n의 값을 입력하세요.: '))
    if n>0:
        break
sum=0
for i in range(1,n+1):
    sum+=i
print(f'1부터 {n}까지의 정수의 합은 {sum}입니다. ')


#1-17
area=int(input('직사각형의 넓이를 입력하세요 :'))
for i in range(1,area+1):
    if i*i>area:
        break
    if area%i:
        continue
    print(f'{i} x {area//i} ')
    
for i in range(1,area+1):
    if i*i>area:
        break
    if area%i==0:
        print(f'{i} x {area//i} ')
        

#1-18
import random
n=int(input('난수의 개수를 입력하세요: '))
for _ in range(n):
    r=random.randint(10,99)
    print(r,end=' ')
    if r==13:
        print('\n프로그램을 중단합니다. ')
        break
else:
    print('\n난수 생성을 종료합니다. ')
    
    
#1-19
#1~12까지 8을 건너뛰고 출력하기
for i in range(1,13):
    if i==8:
        continue
    print(i,end=' ')
    
#1-20
for i in list(range(1,8))+list(range(9,13)):
    print(i,end=' ') 
    

# 2자리 양수(10~99) 입력받기
print('2자리 양수를 입력하세요: ')
while True:
    no=int(input("갑을 입력하세요: "))
    if no>=10 and no<100:
        break
print(f'입력받은 양수는 {no}입니다.')

# if no>=10 and no<100: 
# if 10<=no<=99
# if not (no<10 or no>99) (드모르간 법칙)


#1-21
print('-'*35)
for i in range(1,10):
    for j in range(1,10):
        print(f'{i*j :3}',end=' ')
    print('')
print('-'*35)


#1-22
print('왼쪽 아래가 직각인 이등변 삼각형을 출력합니다. ')
n=int(input('짧은 변의 길이를 입력하세요 :'))
for i in range(n):
    for j in range(i+1):
        print("*",end='')
    print()
    
#1-23
print('오른쪽 아래가 직각인 이등변 삼각형을 출력합니다. ')
n=int(input('짧은 변의 길이를 입력하세요 :'))
for i in range(n):
    for _ in range(n-i-1):
        print(' ',end='')
    for _ in range(i+1):
        print('*',end='')
    print()
    
#파이썬의 변수 알아보기
n=17
id(17)      # 17의 id와 n의 id 값 같음  '17'의 id는 다르다.
id(n)
id('17')

n=1
def put_id():
    x=1
    print(f'id(x) = {id(x)}')
    
print(f'id(1)= {id(1)}')
print(f'id(n)= {id(n)}')
put_id()                    # 위 3개의 id값 모두 같음.


for i in range(1,101):
    print(f'i={i:3}   id({i}) ={id(i)}')
