# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 10:37:19 2024

@author: soyoung
"""

#7-1
a="life is too short"
b=a.encode('utf-8')
b
a="한글"

a.encode("ascii")
a.encode("euc-kr")
a.encode('utf-8')

a='한글'
b=a.encode('euc=kr')
b.decode('euc-kr')
b.decode('utf-8')



#%% 7-2
#클로저
class mul:
    def __init__ (self,m):
        self.m=m
    def mul(self,n):
        return self.m*n
    
if __name__ =="__main__":
    mul3=mul(3)
    mul5=mul(5)
    
    print(mul3.mul(10))
    print(mul5.mul(10))
    
class mul:
    def __init__ (self,m):
        self.m=m
    def __call__(self,n):
        return self.m*n
    
if __name__ =="__main__":
    mul3=mul(3)
    mul5=mul(5)
    
    print(mul3(10))
    print(mul5(10))
    
def mul(m):
    def wrapper(n):
        return m*n
    return wrapper

if __name__ =="__main__":
    mul3=mul(3)
    mul5=mul(5)
    
    print(mul3(10))
    print(mul5(10))
    
#데코레이터
import time
def myfunc():
    start=time.time()
    print("함수가 실행됩니다.")
    end=time.time()
    print("함수 수행시간 : %f 초" % (end-start))
    
myfunc()

def elapsed(original_func):
    def wrapper():
        start=time.time()
        result=original_func()
        end=time.time()
        print("함수 수행시간 : %f 초" % (end-start))
        return result
    return wrapper

@elapsed
def myfunc():
    print("함수가 실행됩니다. ")
    
decorated_myfunc=elapsed(myfunc)
decorated_myfunc()
myfunc()

#%% 7-3
#이터레이터
a=[1,2,3]
next(a)

ia=iter(a)
type(ia)

next(ia)
next(ia)
next(ia)
next(ia)

a=[1,2,3]
ia=iter(a)
for i in ia:
    print(i)
for i in ia:
    print(i)   
    
class myiterator:
    def __init__(self,data):
        self.data=data
        self.position=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.position>=len(self.data):
            raise StopIteration
        result=self.data[self.position]
        self.position+=1
        return result
    
if __name__ =="__main__":
    i=myiterator([1,2,3])
    for item in i:
        print(item)
        
        
class reverseiterator:
    def __init__(self,data):
        self.data=data
        self.position=len(self.data)-1
    def __iter__(self):
        return self
    def __next__(self):
        if self.position<0:
            raise StopIteration
        result=self.data[self.position]
        self.position -= 1
        return result
    
if __name__ =="__main__":
    i=reverseiterator([1,2,3])
    for item in i:
        print(item)
        
#제너레이터
def mygen():
    yield 'a'
    yield 'b'
    yield 'c'
    
g=mygen()

type(g)
next(g)
next(g)
next(g)
next(g)

def mygen():
    for i in range(1,1000):
        result=i*i
        yield result
        
gen=mygen()
print(next(gen))
print(next(gen))
print(next(gen))

gen=(i*i for i in range(1,1000))
 
import time
def longtime_job():
    print("job start")
    time.sleep(1)
    return "done"
list_job=[longtime_job() for i in range(5)]
print(list_job[0])

import time
def longtime_job():
    print("job start")
    time.sleep(1)
    return "done"
list_job=(longtime_job() for i in range(5))
print(next(list_job))

#%% 7-4
a=1
type(a)
a="1"
type(a)

num:int=1
def add(a:int,b:int)->int:
    return a+b

result=add(3,3.4)
print(result)
