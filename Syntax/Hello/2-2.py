# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 11:49:45 2024

@author: soyoung
"""

"hello world"
'hello world'
"""life is too short"""
'''life is too short'''

#문자열 안에 따옴표 포함
food="python's favorite food is perl"
food
say='"python is very eassy." he says.'
food='python\'s favorite food is perl'
food

#줄 바꾸기
multiline="life is too short\nyou need python"
multiline='''
life is too short!
you need python
'''
print(multiline)

#문자열 연산
head="python"
tail=" is fun!"
head+tail

a="python"
a*2

#응용
print("="*50)
print("my program")
print("="*50)

#문자열 길이
a="life is too short"
len(a)
b="you need python"
len(b)

# 문자열 인덱싱과 슬라이스
a="life is too short, you need python"
a[3]
a[-1]
a[-3]
b=a[0]+a[1]+a[2]+a[3]
b
a[0:4]
a[0:5]
a[5:7]
a[:]
a[19:-7]

a="20230331rainy"
date=a[:8]
weatger=a[8:]
year=a[:4]
day=a[4:8]

a="pithon"
a[:1]
a[2:]
a[:1]+'y'+a[2:]

#문자열 포매팅
"i eat %d apples." %3
"i eat %s apples." %"five"
number=3
"i eat %d apples." %number
number=10
day="three"
"i ate %d apples. so i was sick for %s days" %(number, day)

"rate is %s" %3.234
"error is %d%%." % 98

#포맷 코드와 숫자 함께 사용
"%10s" %"hi"
"%-10s jane" % "hi"

"%0.4f" %3.42134234
"%10.4f" %3.42134234

"i eat {0} apples" .format(3)
"i eat {0} apples" .format("five")
number=3
"i eat {0} apples" .format(number)
number=10
day="three"
"i ate {0} apples. soo i was sick {1} days" .format(number,day)
"i ate {number} appels. so i was sick {day} days" .format(number=10,day=3)
"i ate {0} appels. so i was sick {day} days" .format(10,day=3)

"{0:<10}" .format("hi")
"{0:>10}" .format("hi")
"{0:^10}" .format("hi")
"{0:=^10}" .format("hi")
"{0:!^10}" .format("hi")

y=3.42134234
"{0:0.4f}" .format(y)
"{0:10.4f}" .format(y)
"{{ and }}" .format()

# f문자열 포매팅
name='홍길동'
age=30
f"나의 이름은 {name}입니다. 나이는 {age}입니다."
f"나는 내년이면 {age+1}살이 된다."
d={'name':'홍길동', 'age':30}
f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.'

f'{"hi":<10}'
f'{"hi":>10}'
f'{"hi":^10}'

f'{"hi":=^10}'
f'{"hi":!<10}'

y=3.42134234
f'{y:0.4f}'
f'{y:10.4f}'
f'{{ and }}'

#1분코딩
f'{"python":!^12}'
"{0:!^12}" .format("python")

#문자열 관련 함수들
a="hobby"
a.count('b')
a="python is the best choice"
a.find("b")
a.find('k')

a="life is too short"
a.index('t')
a.index('k')

"," .join('abcd')
"," .join(['a','b','c','d'])

a="hi"
a.upper()
a="HI"
a.lower()

a="  hi  "
a.lstrip()
a.rstrip()
a.strip()

a="life is too short"
a.replace("life","your leg")

a.split()
b="a:b:c:d"
b.split(':')
