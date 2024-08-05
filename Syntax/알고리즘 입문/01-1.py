# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 09:08:32 2024

@author: soyoung
"""

#1-1
print('세 정수의 최댓값을 구합니다.')
a=int(input('정수 a의 값을 입력하세요: '))
b=int(input('정수 b의 값을 입력하세요: '))
c=int(input('정수 c의 값을 입력하세요: '))

maximum=a
if b>maximum :maximum=b
if c>maximum :maximum=c
print(f'최댓값은 {maximum}입니다. ')

print('이름을 입력하세요 :',end='')
name=input()
print(f"안녕하세요? {name}님.")

name=input('이름을 입력하세요 : ')
print(f"안녕하세요? {name}님.")

int('17')           #10진수 문자열을 10진수 정수형으로
int('0b110',2)      #2진수 문자열을 10진수 정수형으로
int('0o75',8)       #8진수 문자열을 10진수 정수형으로
int('13',10)        #10진수 문자열을 10진수 정수형으로
int('0x3F',16)      #16진수 문자열을 10진수 정수형으로
float('3.14')       #문자열을 실수형으로 변환


#1-2
def max3(a,b,c):
    """a,b,c 의 최댓값을 구하여 반환"""
    maximum=a
    if b>maximum:maximum=b
    if c>maximum:maximum=c
    return maximum
print(f'max3(3,2,1)={max3(3,2,1)}')
print(f'max3(3,2,2)={max3(3,2,2)}')
print(f'max3(3,1,2)={max3(3,1,2)}')
print(f'max3(3,2,3)={max3(3,2,3)}')
print(f'max3(2,1,3)={max3(2,1,3)}')

def med3(a,b,c):
    """a,b,c 의 중앙값을 구하여 반환"""
    if a>=b:
        if b>=c:
            return b
        elif a<=c:
            return a
        else:
            return c
    elif a>c:
        return a
    elif b>c:
        return c
    else:
        return b
    
print('세 정수의 중앙값을 구합니다.')
a=int(input('정수 a의 값을 입력하세요: '))
b=int(input('정수 b의 값을 입력하세요: '))
c=int(input('정수 c의 값을 입력하세요: '))

print(f'중앙값은 {med3(a,b,c)} 입니다. ')

def med3(a,b,c):
    """a,b,c 의 중앙값을 구하여 반환(다른방법) """
    if (b>=a and c<=a) or (b<=a and c>=a):
        return a
    elif(a>b and c<b) or (a<b and c>b):
        return b
    return c


#1-3
n=int(input('정수를 입력하세요 : '))
if n>0:
    print('이 수는 양수입니다. ')
elif n<0:
    print('이 수는 음수입니다. ')
else:
    print('이 수는 0 입니다. ')
    
#1-4
n=int (input('정수를 입력하세요 : '))
if n==1:
    print('A')
elif n==2:
    print('B')
else:
    print('C')
    
#1-5
n=int (input('정수를 입력하세요 : '))
if n==1:
    print('A')
elif n==2:
    print('B')
elif n==3:
    print('C')
    
#1-6
n=int (input('정수를 입력하세요 : '))
if n==1:
    print('A')
elif n==2:
    print('B')
elif n==3:
    print('C')
else:
    pass
    
x=10
y=20
a=x if x>y else y
c=0
print('c는 0입니다. ' if c==0 else 'c는 0이 아닙니다.')
    