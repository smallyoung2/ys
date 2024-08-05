# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 15:29:07 2024

@author: soyoung
"""

import datetime
day1=datetime.date(2021,12,14)
day2=datetime.date(2023,4,5)

diff=day2-day1
day=datetime.date(2022,11,18)
day.weekday()
day.isoweekday()

import time
time.time()
time.localtime(time.time())
time.asctime(time.localtime(time.time()))
time.ctime()

import time
time.strftime('%x',time.localtime(time.time()))
time.strftime('%c',time.localtime(time.time()))

for i in range(10):
    print(i)
    time.sleep(1)

time.localtime()
time.asctime()
time.strftime('%c')

import math
math.gcd(60,100,80)

60/20,100/20,80/20

math.lcm(15,25)

import random
random.random()

random.randint(1,10)
random.randint(1,55)

import random
def random_pop(data):
    number=random.randint(0,len(data)-1)
    return data.pop(number)

if __name__=="__main__":
    data=[1,2,3,4,5]
    while data:
        print(random_pop(data))
        
def random_pop(data):
    number=random.choice(data)
    data.remove(number)
    return number

data=[1,2,3,4,5]
random.sample(data,len(data))

students=['한민서','황지민','이영철','이광수','김승민']
snacks=['사탕','초콜릿','젤리']
result=zip(students,snacks)
print(list(result))

import itertools
resultall=itertools.zip_longest(students,snacks,fillvalue="새우깡")
print(list(resultall))

import itertools
list(itertools.permutations(['1','2','3'],2))

list(itertools.combinations(['1','2','3'],2))

it=itertools.combinations(range(1,46),6)

for num in it:
    print(num)
len(list(itertools.combinations(range(1,46),6)))
len(list(itertools.combinations_with_replacement(range(1,46),6)))

import functools
data=[1,2,3,4,5]
result=functools.reduce(lambda x,y:x+y,data)
print(result)

num_list=[3,2,8,1,6,7]
max_num=functools.reduce(lambda x,y:x if x>y else y, num_list)
print(max_num)

from operator import itemgetter
students=[
    ("jane",22,'a'),
    ("dave",32,'b'),
    ("sally",17,'c')]
result=sorted(students,key=itemgetter(1))
print(result)

students=[
    {"name":"jane","age":22,"grade":"a"},
    {"name":"dave","age":32,"grade":"b"},
    {"name":"sally","age":17,"grade":"c"}]
result=sorted(students,key=itemgetter('age'))
print(result)

from operator import attrgetter
class student:
    def __init__(self,name,age,grade):
        self.name=name,
        self.age=age,
        self.grade=grade
        
students=[
    student('jane',22,'a'),
    student('dave',32,'b'),
    student('sally',17,'c')]
result=sorted(students,key=attrgetter('age'))
print(result)

# p.277
import time
import threading
def long_task():
    for i in range(5):
        time.sleep(1)
        print("working:%s\n" %i)
print("start")
threads=[]
for i in range(5):
    t=threading.Thread(target=long_task)
    threads.append(t)
    
for t in threads:
    t.start()

for t in threads:
    t.join()
print("end")

import tempfile
filename=tempfile.mkstemp()
filename

f=tempfile.TemporaryFile()
f.close()


import traceback

def a():
    return 1/0
def b():
    a()
    
def main():
    try:
        b()
    except:
        print("오류 발생")
        print(traceback.format_exc())
main()

import webbrowser
webbrowser.open_new('http:\\python.org')
webbrowser.open('http:\\python.org')
