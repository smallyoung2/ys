# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 09:22:07 2024

@author: soyoung
"""
# 6-1 구구단 2단 만들기

def gugu(n):
    for i in range(9):
        i+=1
        print(n,"*",i,"=",int(i*n))

gugu(2)

def gugu(n):
    result=[]
    result.append(n*1)
    result.append(n*2)
    result.append(n*3)
    result.append(n*4)
    result.append(n*5)
    result.append(n*6)
    result.append(n*7)
    result.append(n*8)
    result.append(n*9)
    return result
print(gugu(2))

def gugu(n):
    result=[]
    i=1
    while i<10:
        result.append(n*i)
        i+=1
    return result
        
gugu(2)

# 6-2 3과 5의 배수를 모두 더하기

result=0
for i in range(1,1000):
    if i%3==0 or i%5==0:
        result+=i
print(result)


result=0
for i in range(1,1000):
    if i%3==0:
        result+=i
    if i%5==0:
        result+=i
    if i%15==0:
        result-=i
print(result)

# 6-3 게시판 페이징하기
def get_total_page(m,n):
    if m%n==0:
        return m//n
    else:
        return m//n+1

print(get_total_page(5,10))
print(get_total_page(15,10))
print(get_total_page(25,10))
print(get_total_page(30,10))

# 6-5 탭 문자를 공백 문자 4 개로 바꾸기
