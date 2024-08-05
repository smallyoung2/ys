# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 14:57:47 2024

@author: soyoung
"""

#클래스(class)
#객체지향 프로그래밍: 객체, 인스턴스
#클래스: 속성, 함수를 하나의 묶음으로 처리

#속성: 동일한 자료들의 그룹,멤버변수,공개(정보 은폐를 지원하지않음)
#함수: 멤버함수,메서드,멤버변수에 접근할수 있는 함수
#self: 생성된 객체의 식별자
#메서드를 호출할때는 self생략
#멤버변수(속성):
    # - 멤버변수가 생성,

#%%

#클래스 정의
#학생 정보를 다루는 전용클래스
#속성: 이름 점수(국어, 영어, 수학)

class student:
    def name(self,val):
        self.name=val
    def korean(self,val):
        self.kor=val
    def english(self,val):
        self.eng=val
    def maths(self,val):
        self.math=val
    def score(self):
        return self.kor,self.eng,self.math
    
#%%

#학생(student) 클래스 선언
    
s1=student()            #객체 생성
s1.name('홍길동')       #객체 멤버 메서드에 접근(셰터)
s1.korean(90)
s1.english(80)
s1.maths(70)
print(s1)

#상속
#자식이 자신의 생성자를 정의하면
#더이상 부모의 생성자가 자동으로 호출되지않는다.

#다중상속
#상속: 속성, 메서드를 상속
#상속된 부모 클래스에서 동일한 메서드가 있으면?
#  -> 먼저 상속된 클래스의 메서드가 사용된다.
#명시하지 않고 부모의 속성이나 메서드를 사용할때
# 기본적으로 선택되는 부모는 먼저 상속한 부모의 것을 사용한다.

#%%

class a:
    def printval(self,val):
        print("[a] val= ",val)
        
class b:
    def printval(self,val):
        print("[b] val= ",val)
        
class c(b,a):
    def count(self):
        return self.cnt

class d(a,b):
    pass

c=c()
c.printval(10)              # [b] val=  10

d=d()
d.printval(20)              # [a] val=  20


#[전자] 전자계산기
#다중상속을 이용하라
#사칙연산을 수행하는 클래스를 각각 정의(덧셈,뺼셈,곱셈,나눗셈)
#최하위 클래스에서 다중상속을 하여 통합(총점,평균처리)

class a:
    def add(self,val):
        self.result+=val
        self.count+=1

class b:
    def minus(self,val):
        self.result-=val

class c:
    def mul(self,val):
        self.result*=val
       
class d:
    def div(self,val):
        self.result/=val

    
class calculator(a,b,c,d):
    def __init__(self):
        self.result=0
        self.count=0
        self.operations=[a(),b(),c(),d()]
    def total(self,val):
        for i in self.operations:
            i.add(val)
            i.minus(val)
            i.mul(val)
            i.div(val)
        self.count+=1
        return self.result
    def average(self):
        if self.count==0:
            return 0
        return self.result/self.count
   
data=calculator()
data.add(4)
data.minus(1)
data.mul(5)
data.div(3)
print(data.result)
print(data.total)
print(data.average())
