# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 09:32:11 2024

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
class maxlimitcalculator(calculator):
    def add(self,val):
        self.value+=val
        if self.value>=100:
            self.value=100
            
cal=maxlimitcalculator()
cal.add(60)
cal.add(50)
print(cal.value)

#3
all([1,2,abs(-3)-3])        #false
chr(ord('a'))=='a'          #true

#4
list(filter(lambda x:x>0,[1,-2,3,-5,8,-3]))

#5
hex(234)
int('0xea',16)

#6
list(map(lambda x:x*3,[1,2,3,4]))

#7
data=[-8,2,7,5,-3,5,0,1]
max(data)
min(data)
result=max(data)+min(data)
print(result)

#8
17/3
round(17/3)

#9

#10

#11
import time
time.strftime("%Y/%m/%d %H:%M:%S")

#12
import random
result=[]
while len(result)<6:
    num=random.randint(1,45)
    if num not in result:
        result.append(num)
print(result)

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
