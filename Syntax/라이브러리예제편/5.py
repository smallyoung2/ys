# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 17:20:36 2024

@author: soyoung
"""

#23 itertools.cycle
import itertools
emp_pool=itertools.cycle(['은경','명자','성진'])
next(emp_pool)
next(emp_pool)
next(emp_pool)
next(emp_pool)
next(emp_pool)
next(emp_pool)

#24 itertools.accumulate 월별 누적합계
import itertools
monthly_income=[1161,1814,1270,2256,1413,1842,2221,2207,2450,2823,2540,2134]
result=list(itertools.accumulate(monthly_income))
print(result)
 
result=list(itertools.accumulate(monthly_income,max))
print(result)

#25 itertools.groupby
data=[
      {'name':'민서','blood':'O'},
      {'name':'영순','blood':'B'},
      {'name':'상호','blood':'AB'},
      {'name':'지민','blood':'B'},
      {'name':'상현','blood':'AB'},
      {'name':'지아','blood':'A'},
      {'name':'우진','blood':'A'},
      {'name':'은주','blood':'A'},]
import operator
data=sorted(data,key=operator.itemgetter('blood'))

import pprint
pprint.pprint(data)
print(data)

import itertools
grouped_data=itertools.groupby(data,key=operator.itemgetter('blood'))

result={}
for key,group_data in grouped_data:
    result[key]=list(group_data)
    
print(result)
pprint.pprint(result)


import itertools
import operator
import pprint

data=[
      {'name':'민서','blood':'O'},
      {'name':'영순','blood':'B'},
      {'name':'상호','blood':'AB'},
      {'name':'지민','blood':'B'},
      {'name':'상현','blood':'AB'},
      {'name':'지아','blood':'A'},
      {'name':'우진','blood':'A'},
      {'name':'은주','blood':'A'},]

data=sorted(data,key=operator.itemgetter('blood'))
#groupby전에 분류기준으로 정렬하기

grouped_data=itertools.groupby(data,key=operator.itemgetter('blood'))

result={}
for key,group_data in grouped_data:
    result[key]=list(group_data)
    
pprint.pprint(result)

#26 itertools.zip_longest
students=['민서','지민','영철','광수','승민']
rewards=['사탕','초콜릿','젤리']
result=zip(students,rewards)
print(list(result))

import itertools
students=['민서','지민','영철','광수','승민']
rewards=['사탕','초콜릿','젤리']
result=itertools.zip_longest(students,rewards,fillvalue='새우깡')
print(list(result))

#27 itertools.permutations 순열
import itertools
list(itertools.permutations(['1','2','3'],2))


list(itertools.combinations(['1','2','3'],2))
#순서에 상관없이 2장 고르는 조합


#28 itertools.combinations
import itertools
it=itertools.combinations(range(1,46),6)
for num in it:
    print(num)
    
len(list(itertools.combinations(range(1,46),6)))


#만약 중복을 허용한다면 갯수
len(list(itertools.combinations_with_replacement(range(1,46),6)))


#29 functools.cmp_to_key
import functools
def xy_compare(n1,n2):
    if n1[1]>n2[1]:
        return 1
    elif n1[1]==n2[1]:
        if n1[0]>n2[0]:
            return 1 
        elif n1[0]==n2[0]:
            return 0
        else:
            return -1
    else:
        return -1
    
src=[(0,4),(1,2),(1,-1),(2,2),(3,3)]
result=sorted(src, key=functools.cmp_to_key(xy_compare))

print(result)


#30 functools.lru_cache (maxsize=128)


#31 functools.partial
def add_mul(choice,*args):
    if choice=="add":
        result=0
        for i in args:
            result+=i
    elif choice=="mul":
        result=1
        for i in args:
            result*=i
    return result

def add(*args):
    return add_mul('add',*args)
def mul(*args):
    return add_mul('mul',*args)
print(add(1,2,3,4,5))
print(mul(1,2,3,4,5))


from functools import partial
def add_mul(choice,*args):
    if choice=="add":
        result=0
        for i in args:
            result+=i
    elif choice=="mul":
        result=1
        for i in args:
            result*=i
    return result
add=partial(add_mul,'add')
mul=partial(add_mul,'mul')

print(add(1,2,3,4,5))
print(mul(1,2,3,4,5))

add=partial(add_mul,'add',100)
add(1)
mul=partial(add_mul,'mul',100)
mul(5)
mul(2,3)

print(add.func)
print(add.args)


#32 functools.reduce
def add(data):
    result=0
    for i in data:
        result+=i
    return result
data=[1,2,3,4,5]
result=add(data)
print(result)

import functools
data=[1,2,3,4,5]
result=functools.reduce(lambda x,y:x+y,data)
print(result)

num_list=[3,2,8,1,6,7]
max_num=functools.reduce(lambda x,y:x if x>y else y, num_list)
print(max_num)



#33
import time
def elapsed(original_func):
    def wrapper(*args,**kwargs):
        start=time.time()
        result=original_func(*args,**kwargs)
        end=time.time()
        print("함수 수행 시간 : %f초" %(end-start))
        return result
    return wrapper

@elapsed
def add(a,b):
    """두 수 a,b를 더한 값을 반환하는 함수"""
    return a+b
result=add(3,4)

print(add)
help(add)


import functools
import time
def elapsed(original_func):
    @functools.wraps(original_func)
    def wrapper(*args,**kwargs):
        start=time.time()
        result=original_func(*args,*kwargs)
        end=time.time()
        print("함수 수행 시간: %d초" %(end-start))
        return result
    return wrapper

@elapsed
def add(a,b):
    """두 수 a,b를 더한 값을 반환하는 함수"""
    return a+b
print(add)
help(add)


#34
import pprint
from operator import itemgetter
students=[
    ("jane",22,'a'),
    ("dave",32,'b'),
    ("sally",17,'b')]
result=sorted(students,key=itemgetter(1))
print(result)


students=[
    {"name":"jane","age":22,"grade":'a'},
    {"name":"dave","age":32,"grade":'b'},
    {"name":"sally","age":17,"grade":'b'}]
result=sorted(students,key=itemgetter('age'))
print(result)
pprint.pprint(result)


from operator import attrgetter
class Student:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade
        
students=[
    Student('jane',22,'a'),
    Student('dave',32,'b'),
    Student('sally',17,'b')]

result=sorted(students,key=attrgetter('age'))


for student in result:
    print(f"name:{student.name}, age:{student.age}, grade={student.grade}")
