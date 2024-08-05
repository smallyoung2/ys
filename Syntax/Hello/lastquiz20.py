# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 15:21:33 2024

@author: soyoung
"""

#1
str="a:b:c:d"
str=str.split(':')
result="#".join(str)
print(result)

#2
a={'a':90,'b':80}
a=a.get('c',70)
print(a)            #70

#2 
a={'a':90,'b':80}
a['c']=70
print(a)            #{'a': 90, 'b': 80, 'c': 70}

#3
a=[1,2,3]       #주소 다름
id(a)
a=a+[4,5]
id(a)
a

a=[1,2,3]       #주소 같음
id(a)
a.extend([4,5])
id(a)
a
#%%
#4
a=[20,55,67,82,45,33,90,87,100,25]

result=0                        #for문 사용
for i in range(len(a)):
    if a[i]>=50:
        result+=a[i]
    i+=1

print(result)


result=0                        #while문 사용
i=0
while i<len(a):
    if a[i]>=50:
        result+=a[i]
    i+=1

print(result)


result=0                        #책 답안

while a:             # A 리스트에 값이 있는 동안
    mark=a.pop()     # A리스트의 가장 마지막 항목을 하나씩 뽑아냄
    if mark>=50:
        result+=mark
print(result)
#a.pop():리스트에서 원소를 제거하고 반환하는 함수(마지막원소 제거후 반환)

#%%

#5 피보나치 함수
#첫번째항 0, 두번째항의 값 1, 세번째부터는 앞의 두항 더한값 으로 이루어짐
#입력 n받으면 n항까지의 피보나치 수열 출력하는 함수 작성하기


def pibo(n):
    result=[0,1]
    i=0
    if n==0: return 0
    if n==1: return 0 ,1
    else:
        for i in range(n-2) :
            result.append(result[i]+result[i+1])
        return result

n=int(input("input value: "))         #input하면 str이므로 int 로 반환해주어야함
print(pibo(n))


def pibo(n):                    #책 답안
    if n==0: return 0
    if n==1: return 1
    return pibo(n-2)+pibo(n-1)
for i in range(10):
    print(pibo(i))
    

#%%

#6
userinput=input("input values : ")
data=userinput.split(",")
intdata=list(map(int,data))   #map():원본 iterable의 각 요소에 함수를 적용,결과를 새로운 iterable로 반환
print(sum(intdata))


userinput=input("input values : ")
data=userinput.split(",")
total=0
for i in data:
    total +=int(i)
print(total)

#%%

#7
userinput=input("input value(2~9) : ")

for i in range(10):
    print(int(userinput)*i)             #한줄이 아님
   
    
result=[]
for i in range(1,10):
    result.append(int(userinput)*i)
                                        #리스트에 모아두고 한번에 출력
print(result)               


intdata=int(userinput)                  #책 답안
for i in range(1,10):
    print(i*intdata,end=" ")            #print뒤에 end로 줄바꿈 대신 빈칸출력
    
#2번째 방법은 한번에 출력가능하지만 list로 , 로 숫자 구분된다.
#3번째 방법은 , 없이 빈칸으로 숫자 구분 가능
#%%

#8 파일 읽어 역순으로 저장하기

with open('abc.txt','w')as file:
    file.write('AAA\nBBB\nCCC\nDDD\nEEE')
f=open('abc.txt','r')
lines=f.readlines()
f.close()

lines.reverse()

f=open('abc.txt','w')
for line in lines:
    line=line.strip()
    f.write(line)
    f.write('\n')
f.close()

#%%
#9
with open('sample.txt','w')as file:
    file.write('70\n60\n55\n75\n95\n90\n80\n80\n85\n100')
f=open('sample.txt','r')
lines=f.readlines()
f.close()

total=0
for line in lines:
    score=int(line)
    total+=score
average=total/len(lines)

f=open("result.txt",'w')
f.write(str(average))
f.close()

#%%

#10 계산기 만들기 
class calculator:
    def __init__(self,numberlist):
        self.numberlist=numberlist
    def add(self):
        result=0
        for num in self.numberlist:
            result+=num
        return result
    def avg(self):
        total=self.add()
        return total/len(self.numberlist)
    
cal1=calculator([1,2,3,4,5])
print(cal1.add())
print(cal1.avg())

cal2=calculator([6,7,8,9,10])
print(cal2.add())
print(cal2.avg())

        
#%%

#11.모듈을 사용하는 방법

#12.오류와 예외처리

#13.dashinsert함수
# 홀수 연속되면 두수사이에 - 추가,짝수 연속되면 두수사이에 * 추가
# 입력 4546793   출력 : 454*67-9-3

data="4546793"
type(data)
numbers=list(map(int,data))
result=[]

# enumerate는 i 인덱스 num 데이터 enumerate 는 i,num 모두필요

for i,num in enumerate(numbers):              #책 답안 numbers[i]=num같은 의미
    result.append(str(numbers[i]))
    if i<len(numbers)-1 :
        is_odd=numbers[i]%2==1
        is_next_odd=numbers[i+1]%2==1
        if is_odd and is_next_odd:
            result.append("-")
        elif not is_odd and not is_next_odd:
            result.append("*")
print("".join(result))        


result=[]
for i,num in enumerate(numbers):
    result.append(str(numbers[i]))       #문자열로 변환해야 print 때 join 가능
    if i<len(numbers)-1 :
        is_odd=numbers[i]%2==1
        is_next_odd=numbers[i+1]%2==1
        if is_odd and is_next_odd:
            result.append("-")
        elif not is_odd and not is_next_odd:
            result.append("*")
            
print("".join(result)) 

#%%

#14. 문자열 압축하기

def compress(data):
    if not data:
        return ""
    result=[]
    current_char=data[0]
    char_count=1
    
    for char in data[1:]:
        if char ==current_char:
            char_count+=1
        else:
            result.append(current_char+str(char_count))
            current_char=char
            char_count=1
    result.append(current_char+str(char_count))
    return "".join(result)

data="aaabbcccccca"
result=compress(data)
print(result)

data=input("input str : ")
print(compress(data))


def compress_string(s):                     #책 답안
    _c=""
    cnt=0
    result=""
    
    for c in s:
        if c!=_c:
            _c=c
            if cnt:
                result=result+str(cnt)
            result=result+c
            cnt=1
        else:
                cnt+=1
    if cnt :
        result+=str(cnt)
    return result
    
print(compress_string("aaabbcccccca"))
    
data=input("input str : ")
print(compress(data))
    
#%%
# duplicate numbers 함수

def chk_dup_numbers(s):                     #책 답안
    result=[]
    for num in s:
        if num not in result:
            result.append(num)
        else:
            return False
    return len(result)==10

print(chk_dup_numbers("0123456789"))   
print(chk_dup_numbers("01234")) 
print(chk_dup_numbers("01234567890")) 
print(chk_dup_numbers("6789012345")) 
print(chk_dup_numbers("012322456789"))
print(chk_dup_numbers("1111111111"))
print(chk_dup_numbers("dd"))


def duplicate(s):
    if not s.isdigit():
        return False
    if len(s)!=10:
        return False

    return all(s.count(str(i))==1 for i in range(10)) #0~9까지 한번씩 사용되었는지

print(duplicate("0123456789"))   
print(duplicate("01234")) 
print(duplicate("01234567890")) 
print(duplicate("6789012345")) 
print(duplicate("012322456789"))
print(duplicate("1111111111"))
print(duplicate("dd"))


#%%
#16. 모스부호 해독
dic = {
    '.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F',
    '--.':'G','....':'H','..':'I','.---':'J','-.-':'K','.-..':'L',
    '--':'M','-.':'N','---':'O','.--.':'P','--.-':'Q','.-.':'R',
    '...':'S','-':'T','..-':'U','...-':'V','.--':'W','-..-':'X',
    '-.--':'Y','--..':'Z'
}
def morse(src):                                 #책 답안
    result=[]
    for word in src.split("  "):
        for char in word.split(" "):
            result.append(dic[char])
        result.append(" ")
    return "".join(result)

print(morse('.... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--'))


#%%
#17
import re
p=re.compile("a[.]{3,}b")

print(p.match("accb"))
print(p.match("a...b"))
print(p.match("aaab"))
print(p.match("a.cccb"))
print(p.match("a......b"))

#%%
#18
import re
p=re.compile("[a-z]+")
m=p.search("5 python")
print(m.start()+m.end())
           
#19
s="""
park 010-9999-9999
kim 010-9909-7789
lee 010-8789-7768 """

pat=re.compile("(\d{3}[-]\d{4}[-])\d{4}")
result=pat.sub("\g<1>####",s)                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
print(result)


#%%
#20
import re
pat=re.compile(".*[@].*[.](?=com$|net$).*$")

print(pat.match("park@naver.com"))
print(pat.match("kim@daum.net"))
print(pat.match("lee@myhome.co.kr"))
print(pat.match("pahkey@gmail.com"))
