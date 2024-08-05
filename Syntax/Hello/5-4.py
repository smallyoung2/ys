# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 12:41:15 2024

@author: soyoung
"""

try:
    4/0
except ZeroDivisionError as e:
    print (e)
    
try:
    f=open('foo.txt','w')
finally:
    f.close()
    
try:
    a=[1,2]
    print(a[3])
    4/0
except ZeroDivisionError:
    print("0으로 나눌수 없습니다.")
except IndexError:
    print("인덱싱 할수 없습니다. ")
    
try:
    a=[1,2]
    print(a[3])
    4/0
except ZeroDivisionError as e:
    print(e)
except IndexError as e:
    print(e)    
    
try:
    a=[1,2]
    print(a[3])
    4/0
except (ZeroDivisionError,IndexError) as e:
    print(e)

try:
    age=int(input('나이를 입력하세요 :  '))
except:
    print("입력이 정확하지 않습니다.")
else:
    if age<=18:
        print("미성년자는 출입금지입니다.")
    else:
        print("환영합니다.")
        
try:
    f=open("나없는파일",'r')
except FileNotFoundError:
    pass

class bird:
    def fly(self):
        raise NotImplementedError                   

class eagle(bird):
    pass
eagle=eagle()
eagle.fly()
class eagle(bird):
    def fly(self):
        print("very fast")
        
eagel=eagle()
eagel.fly()

class myerror(Exception):
    pass
def say_nick(nick):
    if nick=="바보":
        raise myerror()
    print(nick)
    
say_nick("천사")
say_nick("바보")

try:
    say_nick("천사")
    say_nick("바보")
except myerror:
    print("허용되지 않는 별명입니다.")
    
try:
    say_nick("천사")
    say_nick("바보")
except myerror as e:
    print(e)
    
class myerror(Exception):
    def __str__(self):
        return "허용되지 않는 별명입니다."
    
try:
    say_nick("천사")
    say_nick("바보")
except myerror as e:
    print(e)