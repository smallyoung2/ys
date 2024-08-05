print("hello, python")


print("파이썬의 세계에 오신 것을 환영합니다.")

"""
할당은 우측의 값을 좌측 변수에 넣는다
기존의 좌측의 값은 지워지고 지정된 새로운 값이 들어간다

(변수타입)
지정되는 값에 의해 결정
이미 선언된 변수도 다른 타입으로 변환 가능하다
이미 선언된 변수에 다른 타입의 값을 넣으면 해당하는 타입으로 변환

(변수확인)
자료형확인 type()
메모리확인 id()

id()
객체를 식별할 수 있는 고유의 값
메모리 주소와 맵핑된 형태
id가 같으면 동일한 메모리 참조
"""

# %%

#1
# 1만원 4장 1천원 3장 500원 5개 100원 9개 10원 6개  총금액은?
a=10000
b=1000
c=500
d=100
e=10
total=a*4+b*3+c*5+d*9+e*6
print(total)


#2
#위 1번 문제의 총금액에서 15000원짜리 2개를 지출하고남은 금액은?
book=15000

total=total-book*2
print(total)

#3
# 한달 급여 400만원 분기별 보너스는 월 급여의 30% 지급
# 세금은 월 급여의 3% 보너스에 대한 세금 없음
# 월 세후 수령액은 얼마인가?
# 연 총세금은 얼마인가?
# 세후 연 수령액은 얼마인가?
pay=4000000
bonus=pay*0.3
tax=pay*0.03

totalpay=pay+bonus-tax
print(totalpay)

totaltax=tax*12
print(totaltax)

totalyearpay=totalpay*12
print(totalyearpay)

#%% p.71
# 아래 숫자 문자열에서 각각 홀수와 짝의 문자를 추출하라.
#단 슬라이싱을 이용하여라
nums="0123456789"

print(f"문자열 ({nums})에서 홀수는 ({nums[1::2]}) 이다.")

start=1
end=len(nums)
step=2
odd=nums[start:end:step]
print(f"문자열 ({nums})에서 홀수는 ({odd}) 이다.")


print(f"문자열 ({nums})에서 홀수는 ({nums[0::2]}) 이다.")

start=0
end=len(nums)
step=2
even=nums[start:end:step]
print(f"문자열 ({nums})에서 홀수는 ({even}) 이다.")

def positive(l):
    result=[]
    for i in l:
        if i%2==0:
            result.append(i)
    return result
print(positive([0,1,2,3,4,5,6,7,8,9]))

def positive(x):
    return x%2==0
print(list(filter(positive,[0,1,2,3,4,5,6,7,8,9])))

list(filter(lambda x:x%2==0,[0,1,2,3,4,5,6,7,8,9]))

#%% 
#문자열을 연속해서 찾기
#문자열 변수(s)에서 지정된 문자열 ('t')의 위치를 모두 찾아라
#단, find()함수를 이용하라
#정답 : 2 10 17
s="python is the best choice"
print("0123456789"*4)
print(s)

#찾을 문자열
findstr='t'
print(f"문자열 ('{s}')에서 문자열 ('{findstr}')의 갯수는? ", s.count(findstr))

a=s.find('t')
b=s.find('t',3)
c=s.find('t',11)

result= print(a,b,c)

#%%
#아래 전화번호를 공백('' ')대신에 하이픈'-'으로 대체하라
#단, 최종적으로 join 함수를 이용하여 완성하라
hp="010 1234 1234"
hp.replace(" ","-")

t1=hp.split()
t1
result="-".join(t1)
print(result)
