# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 12:28:28 2024

@author: soyoung
"""

#1.프로그래밍 기본개념
1+2
var1=5
var1
var1=10
var1
var2=20
var2
var3=var1+var2
var3
print(var1)
print(var1+var2)
print(var1,var2)
print("덧셈: ",var1+var2)

#2. 자료형
var1=10
type(var1)
var2=3.14
type(var2)
var3=1+2
var4=3+0.14
type(var3)
type(var4)

str1="easy"
str1
type(str1)
str2="파이썬 딥러닝"
str2
str3='ver1.0'
type(str3)
len(str1)
str1[0]
str1[3]
str1[-1]
str1[-3]
str1[0:3]
str1[-3:-1]
str1[-3:]
str4='%s 파이썬딥러닝'%str1
str4

list1=[1,2,3,4,5]
list1
list2=[10]
print(list2)
type(list2)
list3=list()
print(list3)
list4=[]
list_of_list=[list1,list2,list3]
type(list_of_list)
list_of_list[0]
list_of_list[0][1]
list_of_list[-1]
list_of_list[-3]
list_of_list[0:2]
list1.append(100)
list1
list3.append(7)
list3.append(8)
list3.append(9)
list3

tuple1=(1,2)
type(tuple1)
tuple2=("a","b",100)
tuple3=tuple()
tuple4=()
print(tuple3,tuple4)
tuple2[0]
tuple2[1:]

dict1={"name":"jay","age":20}
dict1
type(dict1)
dict1['name']
dict1['age']
dict1['grade']=[3.0,4.0,3.5,4.2]
dict1
dict1.keys()
dict1.values()
dict1.items()

#3. 연산자
1+2
new_str="good"+" "+"morning"
new_str
2-3
3*4
"a"*3
5/3
5//3
5%3
3**2
True
not True
type(False)
True and True           #Out[104]: True
True and False          #Out[105]: False
False and False         #Out[106]: False
True or True            #Out[107]: True
True or False           #Out[108]: True
False or False          #Out[109]: False
3==3
3!=3
'a'=='a'
'a'!='a'
var1='a'
var2='a'
var1==var2
4<5
4<=5
4>=5
4>5
4<5 and 4<=5            #Out[124]: True
4<5 or 4>5              #Out[125]: True
not 'a'!='a'            #Out[126]: True

#4.제어문
a=4
if a%2==0:
    print("a는 짝수")
    print("a는 2의 배수")
    
if a%2!=0:
    print("a는 홀수")

b=7
if b%2==0:
    print("b는 짝수")
else:
    print("b는 홀수")
    
c=-1
if c>0:
    print("c는 양수")
elif c<0:
    print("c는 음수")
else:
    print("c는 0")
    
num_list=[1,2,3]
for num in num_list:
    print(num)
    
for num in [1,2,3]:
    print("기존:",num)
    print("2배",num*2)
    print("\n")
    
double=[]
for num in [1,2,3]:
    double.append(num*2)
print(double)

num=1
while num<4:
    print(num)
    num+=1
num=1
while num<4:
    print("기존:",num)
    print("2배",num*2)
    print("\n")
    num+=1
    
num=1
double=[]
while True:
    double.append(num*2)
    if len(double)==3:
        break
    num+=1
print(double)

num_range=range(1,46)
len(num_range)
num_list=list(num_range)
print(num_list)

import random
random.shuffle(num_list)
print(num_list)

lotto=[]
while len(lotto)<6:
    random.shuffle(num_list)        #45개 셔플로 랜덤하게 돌림
    num_selected=num_list[0]        #45개 숫자중 첫번째 숫자
    if num_selected in lotto:       #lotto 안에 num_selected있다면 반복문 처음으로 돌아가기
        continue
    lotto.append(num_selected)      #없다면 lotto에 num_selected 요소 추가
    print(num_selected)
print(lotto)

data={'name': 'jay', 'age': 20, 'grade': [3.0, 4.0, 3.5, 4.2]}
data
data['address']                 #address 키값 없으므로 오류 발생

try:
    print("주소",data['address'])     #있다면 주소 출력
except:
    print("주소 정보가 없습니다.")
    
try:
    print("이름",data['name'])
except:
    print("이름정보가 없습니다.")
finally:
    print("모든 작업이 완료되었습니다.")
    
#5. 함수
def cal_modulo(a,b):
    temp=a%b
    return temp
cal_modulo(5,3)
modulo=cal_modulo(10,3)
print(modulo)

num_pairs=[(5,3),(2,2),(10,3)]
for a,b in num_pairs:
    modulo=cal_modulo(a,b)
    print(modulo)

def cal_pairs_modulo(num_pair_list):        #딕셔너리형태로 저장
    result={}
    for a,b in num_pairs:
        modulo=a%b
        result[(a,b)]=modulo
    return result
mod_pairs=cal_pairs_modulo(num_pairs)
mod_pairs

def print_mod_pairs():                      #출력하는 함수
    print(cal_pairs_modulo(num_pairs))
print_mod_pairs()

result              #함수안에서 정의된 지역변수 이므로 함수밖에서 호출 x <->전역변수

def add_one(num):
    return num+1
answer=add_one(1)
print(answer)

add_one_list=[]
for x in [1,2,3]:
    y=add_one(x)
    add_one_list.append(y)
print(add_one_list)   

add_one_lambda=[]
add_func=lambda x:add_one_lambda.append(x+1)
for x in [1,2,3]:
    add_func(x)
print(add_one_lambda)

new_add_func=lambda x,y:x+y
answer=new_add_func(2,3)
print(answer)

numbers=[1,2,3,4,5,6,7,8,9,10]
sum(numbers)
max(numbers)
min(numbers)
len(numbers)
for i,num in enumerate(numbers):
    print(i,num)
    
range(10)
list(range(1,10))
print(list(range(10)))
eval('print(numbers)')
add_one=lambda x:x+1
results=map(add_one,numbers)
print(list(results))        #[2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(results)              #<map object at 0x000002C48A128A30>

even_num=lambda x:x%2==0 
results=filter(even_num,numbers)
print(list(results))

int(3.14)
str(3.14)
round(3.14)                 #반올림
numbers_reversed=reversed(numbers)
print(list(numbers_reversed))
sorted([3,4,2,1])

chars=['a','b','c']
nums=[1,2,3]
pairs=zip(chars,nums)
print(list(pairs))

#6.클래스
def add(num1,num2):
    return num1+num2

class calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
        self.result=0
    def add(self):
        self.result=self.num1+self.num2
        return self.result

cal=calculator(1,2)
print(cal.num1,cal.num2,cal.result)             #1 2 0
cal.add()
cal.result

class calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
        self.result=0
    def add(self):
        self.result=self.num1+self.num2
        return self.result
    def subtract(self):
        self.result=self.num1-self.num2
        return self.result
    def multiply(self):
        self.result=self.num1*self.num2
        return self.result
    def divide(self):
        self.result=self.num1/self.num2
        return self.result
    def change(self,num1,num2):
        self.num1=num1
        self.num2=num2
        print("num1:",self.num1)
        print("num2:",self.num2)
        
cal2=calculator(1,2)
print(cal2.num1,cal2.num2)

print(cal2.add())
print(cal2.subtract())
print(cal2.multiply())
print(cal2.divide())
cal2.change(3,2)
cal2.add()
