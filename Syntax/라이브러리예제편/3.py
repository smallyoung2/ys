# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 12:32:08 2024

@author: soyoung
"""

#5 datetime.date
import datetime
day1=datetime.date(2019,12,14)
day1
day2=datetime.date(2021,6,5)
day2

diff=day2-day1
diff
diff.days

day3=datetime.datetime(2020,12,14,14,10,50)
day3.hour
day3.minute
day3.second

day=datetime.date(2019,12,14)
time=datetime.time(10,14,50)
dt=datetime.datetime.combine(day,time)
dt

day=datetime.date(2019,12,14)
day.weekday()               # 0월요일,1화요일,2수요일,3목요일 ...
day.isoweekday()            # 1월요일,2화요일,3수요일,4목요일 ...

#6 datetime.timedelta
import datetime
today=datetime.date.today()
today                       # 오늘날짜 얻음 
diff_days=datetime.timedelta(days=100)
diff_days

today+diff_days
today-diff_days

#7 calendar.isleap
def is_leap_year(year):     #True: 29일까지, False: 28일까지
    if year%400==0:
        return True
    if year%100==0:
        return False
    if year%4==0:
        return True
    return False

import calendar
calendar.isleap(0)      #True
calendar.isleap(1)      #False
calendar.isleap(4)      #True
calendar.isleap(1200)   #True
calendar.isleap(700)    #False
calendar.isleap(2020)   #True

#8 collections.deque
from collections import deque
a=[1,2,3,4,5]
q=deque(a)
q.rotate(2)             #시계방향 회전은 양수, 반시계방향은 음수
result=list(q)
result

from collections import deque
d=deque([1,2,3,4,5])
d.append(6)
d
d.appendleft(0)
d
d.pop()
d
d.popleft()
d

#9 collections.namedtuple
data=[
      ('홍길동',23,'01099990001'),
      ('김철수',31,'01099991002'),
      ('이영희',29,'01099992003')]
emp=data[0]

from collections import namedtuple
employee=namedtuple('employee','name,age,cellphone')
data=[employee(emp[0], emp[1], emp[2])for emp in data]
data=[employee._make(emp) for emp in data]

emp=data[0]
emp.name
emp.age
emp.cellphone

emp._asdict()

emp[0]
emp[1]
emp[2]

emp.name='박길동'              #네임드 튜플은 튜플이므로 변경 x ->오류 발생
new_emp=emp._replace(name='박길동')
new_emp                        # _replace함수로만 값 변경가능(새로운 객체 만들어서 변경됨)

#10 collections.counter
from collections import Counter
import re
data="""
산에는 꽃 피네 꽃이 피네 갈 봄 여름 없이 꽃이 피네
산에 산에 피는 꽃은 저만치 혼자서 피어있네
산에서 우는 작은 새여 꽃이 좋아 산에서 사노라네
산에는 꽃 지네 꽃이 지네 갈 봄 여름 없이 꽃이 지네"""

words=re.findall(r'\w+',data)
counter=Counter(words)
print(counter)

print(counter.most_common(1))
print(counter.most_common(2))

#11 collections.defaultdict
text="Life is too short, You need python."
d=dict()
for key in text:
    if key not in d:
        d[key]=0
    d[key]+=1
    
print(d)


from collections import defaultdict
text="Life is too short, You need python."

d=defaultdict(int)
for key in text:
    d[key]+=1
    
print(dict(d))

#12 heapq
import heapq
data=[
      (12,23,'보람'),(12.31,'지원'),(11.98,'시우'),(11.99,'준혁'),
      (11.67,'정웅'),(12.02,'중수'),(11.57,'동현'),(12.04,'미숙'),
      (11.92,'시우'),(12.22,'민석')]
h=[]
for score in data:              #data를 힙 구조에 맞게 변경
    heapq.heappush(h,score)
    
for i in range(3):
    print(heapq.heappop(h))
#%%    
heapq.heapify(data)             #data를 힙 구조에 맞게 변경
for i in range(3):
    print(heapq.heappop(data))
    
#%%
print(heapq.nsmallest(3,data))  #가장 간단한 코드방법 (작은수부터 나열)
print(heapq.nlargest(3,data))   #가장 간단한 코드방법 (큰수부터나열)

#13 pprint
import pprint
pprint.pprint(data)             #(pretty print) 보기좋게 출력 
print(data)

#14 bisect
import bisect
result=[]
for score in [33,99,77,70,89,90,100]:   # 60,70,80,90 이상일때 
    pos=bisect.bisect([60,70,80,90],score)
    grade='FDCBA'[pos]
    result.append(grade)
    
print(result)


import bisect
result=[]
for score in [33,99,77,70,89,90,100]:   # 60,70,80,90 초과일때 
    pos=bisect.bisect_left([60,70,80,90],score)
    grade='FDCBA'[pos]
    result.append(grade)
    
print(result)

a=[60,70,80,90]
bisect.insort(a,85)                     # 정렬할수 있는 위치에 숫자 삽입
a

#15 enum
from datetime import date
def get_menu(input_date):
    weekday=input_date.isoweekday()
    if weekday==1:
        menu="김치찌개"
    elif weekday==2:
        menu="비빔밥"
    elif weekday==3:
        menu="된장찌개"
    elif weekday==4:
        menu="불고기"
    elif weekday==5:
        menu="갈비탕"
    elif weekday==6:
        menu="라면"
    elif weekday==7:
        menu="건빵"
    return menu
print(get_menu(date(2021,12,6)))
print(get_menu(date(2021,12,18)))

from enum import IntEnum

class week(IntEnum):
    MONDAY=1
    TUESDAY=2
    WEDNESDAY=3
    THURSDAY=4
    FRIDAY=5
    SATURDAY=6
    SUNDAY=7

def get_menu(input_date):
    menu={
        week.MONDAY:"김치찌개",
        week.TUESDAY:"비빔밥",
        week.WEDNESDAY:"된장찌개",
        week.THURSDAY:"불고기",
        week.FRIDAY:"갈비탕",
        week.SATURDAY:"라면",
        week.SUNDAY:"건빵"}
    return menu[input_date.isoweekday()]

print(get_menu(date(2021,12,6)))
print(get_menu(date(2021,12,18)))

print(week.MONDAY.value)
print(week.MONDAY.name)

for week in week:
    print("{}:{}".format(week.name,week.value))
    
#16 graphlib.TopologicalsSorter
from graphlib import TopologicalSorter
ts=TopologicalSorter()

ts.add('영어 중급','영어 초급')
ts.add('영어 고급','영어 중급')

ts.add('영어 문법','영어 중급')
ts.add('영어 고급','영어 문법')

ts.add("영어 회화",'영어 문법')

print(list(ts.static_order()))
