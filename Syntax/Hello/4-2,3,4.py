# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 09:15:48 2024

@author: soyoung
"""

# 4-2
a=input()
a

number=input("숫자를 입력하세요 : ")
print(number)
type(number)

print("life" "is" "too" "short")
print("life"+"is"+"too"+"short")

print("life","is","too","short")

for i in range(10):
    print(i,end=' ') 

# 4-3
f=open("새파일.txt",'w')
f.close()

f=open("C:/doit/새파일.txt",'w')
f.close()

f=open("C:/doit/복습.txt",'w')
f.close()

f=open("C:/doit/새파일.txt",'w')
for i in range(1,11):
    data="%d번째 줄입니다.\n" %i
    f.write(data)
f.close()

for i in range(1,11):
    data="%d번째 줄입니다.\n" %i
    print(data)

f=open("C:/doit/새파일.txt",'r')
line=f.readline()
print(line)
f.close()

f=open("C:/doit/새파일.txt",'r')
while True:
    line=f.readline()
    if not line: break
    print(line)
f.close()

while True:
    data=input()
    if not data : break
    print(data)

f=open("C:/doit/새파일.txt",'r')
lines=f.readlines()
for line in lines:
    print(line)
f.close()

f=open("C:/doit/새파일.txt",'r')
lines=f.readlines()
for line in lines:
    line =line.strip()
    print(line)
f.close()

f=open("C:/doit/새파일.txt",'r')
data=f.read()
print(data)
f.close()

f=open("C:/doit/새파일.txt",'r')
for line in f:
    print(line)
f.close()

f=open("C:/doit/새파일.txt",'a')
for i in range(11,20):
    data="%d번째 줄입니다.\n" %i
    f.write(data)
f.close()

f=open("foo.txt",'w')
f.write("life is too short, you need python")
f.close()

with open("foo.txt",'w') as f:
    f.write("life is short, you need python")

#4-4
import sys
args=sys.argv[1:]
for i in args:
    print(i)
    
import sys
args=sys.argv[1:]
for i in args:
    print(i.upper(),end='')