# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 15:58:11 2024

@author: soyoung
"""

money=True
if money:
    print("택시를 타고가라")
else:
    print("걸어가라")

x=3
y=2
x>y
x<y
x==y
x!=y

money=2000
if money>=3000 :
    print("택시")
else:
    print("걸어가라")

card=True
if money>=3000 or card :
    print("택시")
else:
    print("걸어가라")
    
1 in [1,2,3]
1 not in [1,2,3]
'a' in ['a','b','c']
'j' not in 'python'
'p' in 'python'

pocket=['paper','cellphone','money']
if 'money' in pocket:
    print("택시")
else:
    print("걸어가라")
    
#1분 코딩
if 'card' in pocket:
    print("택시")
else:
    print("걸어가라")
    
pocket=['paper','cellphone','money']
if 'money' in pocket:
    pass
else:
    print("카드를 꺼내라")
    
pocket=['paper','cellphone']
if 'money' in pocket:
    print("택시")
else:
    if card:
        print("카드로 택시")
    else:
        print("걸어가라")
    
if 'money' in pocket:
    print("택시")
elif card:
    print("카드로 택시")
else:
    print("걸어가라")
    
if score>=60:
    message="success"
else:
    message="failure"

message="success" if score>=60 else "failure"
