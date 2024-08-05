# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 16:35:46 2024

@author: soyoung
"""

#1
class calculator:
    def __init__(self):
        self.value=0
    def add(self,val):
        self.value+=val
        
class upgradecalculator(calculator):
    def minus(self,val):
        self.value-=val

cal=upgradecalculator()
cal.add(10)
cal.minus(7)

print(cal.value)

#2
class calculator:
    def __init__(self):
        self.value=0
    def add(self,val):
        self.value+=val

class maxlimitcalculator(calculator):
    def add(self,val):
        self.value+=val
        if self.value>100:
            self.value= 100
       
        
cal=maxlimitcalculator()
cal.add(50)
cal.add(60)

print(cal.value)

#3
all([1,2,abs(-3)-3])
chr(ord('a'))=='a'

#4
list(filter(lambda x:x>0,[1,-2,3,-5,8,-3]))

#5
hex(234)
int('0xea',16)

#6
list(map(lambda a:a*3,[1,2,3,4]))

#7
max=max([-8,2,7,5,-3,5,0,1])
min=min([-8,2,7,5,-3,5,0,1])
sum=max+min
print(sum)

#8
round(17/3,4)

#9


#10
import glob
glob.glob("c:/doit/*.py")

#11
import time
time.strftime("%Y/%m/%d  %H:%M:%S")

#12
import random
result=[]
while len(result)<6:
    num=random.randint(1,45)
    if num not in result:
        result.append(num)
print(result)


import itertools
it=itertools.combinations(range(1,46),6)

for num in it:
    print(num)
    
#13
import datetime
day1=datetime.date(1995,11,20)
day2=datetime.date(1998,10,6)
diff=day2-day1
diff.days

#14
from operator import itemgetter
data=[('서현',15.25),('예지',13.31),('예원',15.34),('순자',15.57),
      ('시우',15.48),('숙자',17.9),('정웅',13.39),('혜진',16.63),
      ('보람',17.14),('지영',14.83),('성호',17.7),('옥순',16.71),
      ('민지',17.65),('영철',16.7),('병철',15.67),('상현',14.16),
      ('영순',14.81),('지아',15.13),('지은',16.93),('재호',16.39)]
result=sorted(data,key=itemgetter(1))
print(result)

#15
import itertools
students=['지혜','성민','지현','정숙']
result=itertools.combinations(students,2)
print(list(result))

#16
import itertools
result=itertools.permutations("abcd",4)
for r in result:
    print(''.join(r))
    
#17
import random
import itertools
students=['승현','진호','춘자','예준','현주']
works=['청소','빨래','설거지']

random.sample(students,len(students))       #무작위로 섞는다.

result=itertools.zip_longest(students,works,fillvalue='휴식')

for r in result: print(r)

#18
import math

width=200
height=80

square_size=math.gcd(80,200)
print("정사각형의 길이: {}".format(square_size))
width_count=width/square_size
height_count=height/square_size
print("필요한 타일의 개수:",width_count*height_count)
print("필요한 타일의 개수: {}".format(width_count*height_count))
