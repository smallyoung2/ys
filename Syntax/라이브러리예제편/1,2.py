# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 12:06:35 2024

@author: soyoung
"""
#1 textwrap.shorten
import textwrap
textwrap.shorten("life is too short, yoou need python",width=15)
textwrap.shorten("인생은 짧으니 파이썬이 필요해",width=15)
textwrap.shorten("인생은 짧으니 파이썬이 필요해",width=15,placeholder='...')

#2 textwrap.wrap
long_text='life is too short, you need python'*10
long_text

result=textwrap.wrap(long_text,width=70)        #한줄에 70자 넘지 않음
result

print('\n'.join(result))

result=textwrap.fill(long_text,width=70)
print(result)

#3 re (import re)

data="""
홍길동의 주민 등록 번호는 800905-1049118 입니다.
그리고 고길동의 주민등록 번호는 700905-1059119 입니다.
그렇다면 누가 형님일까요?
"""
result=[]
for line in data.split("\n"):
    word_result=[]
    for word in line.split(" "):
        if len(word)==14 and word[:6].isdigit() and word[7:].isdigit():
            word=word[:6]+"-" +"*******"
        word_result.append(word)
    result.append(" ".join(word_result))
print("\n".join(result))

import re

pat=re.compile("(\d{6})[-]\d{7}")
print(pat.sub("\g<1>-********",data))

#4 struct
import struct
with open('output','rb') as f:
    chunk=f.read(16)
    result=struct.unpack('dicccc',chunk)
    print(result)