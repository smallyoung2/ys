# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 12:37:51 2024

@author: soyoung
"""

# 8-1
data="""
park 800905-1049118
kim 700905-1059119 """
result=[]
for line in data.split("\n"):
    word_result=[]
    for word in line.split(" "):
        if len(word)==14 and word[:6].isdigit() and word[7:].isdigit():
            word=word[:6]+"-"+"*******"
        word_result.append(word)
    result.append(" ".join(word_result))
print("\n".join(result))

import re
data="""
park 800905-1049118
kim 700905-1059119 """
pat=re.compile("(\d{6})[-]\d{7}")
print(pat.sub("\g<1>-*******",data))

#%% 8-2
import re
p=re.compile('ab*')

p=re.compile('[a-z]+')
m=p.match("python")
print(m)
m=p.match("3 python")
print(m)

m=p.search("python")
print(m)
m=p.search("3 python")
print(m)

result=p.findall("life is too short")
print(result)

result=p.finditer("life is too short")
print(result)
for r in result:print(r)

m=p.match("python")
m.group()
m.start()
m.end()
m.span()
m=p.search("3 python")
m.group()
m.start()
m.end()
m.span()

#컴파일 옵션
import re
p=re.compile('a.b', re.DOTALL)
m=p.match('a\nb')
print(m)

p=re.compile('[a-z]+',re.I)
p.match('python')
p.match('Python')
p.match('PYTHON')

p=re.compile("^python\s\w+",re.MULTILINE)

data="""python one
life is too short
python two
you need python
python three"""
print(p.findall(data))

p=re.compile('\\section')
p=re.compile('\\\\section')

#%% 8-3
import re
p=re.compile('crow|servo')
m=p.match('crowhello')
print(m)

print(re.search('^life', 'life is too short'))
print(re.search('^life', 'mylife'))

print(re.search('short$','life is too short'))
print(re.search('short$','life is too short, you need python'))

p=re.compile(r'\bclass\b')
print(p.search('no class at all'))

print(p.search('the declassified algorithm'))
print(p.search('one subclass is'))

p=re.compile(r'\Bclass\B')
print(p.search('no class at all'))

print(p.search('the declassified algorithm'))
print(p.search('one subclass is'))

#그루핑
p=re.compile('(ABC)+')
m=p.search('ABCABCABC OK?')
print(m.group())

p=re.compile(r"\w+\s+\d+[-]\d+[-]\d+")
m=p.search("park 010-1234-1234")

p=re.compile(r"(\w+)\s+\d+[-]\d+[-]\d+")
m=p.search("park 010-1234-1234")
print(m.group(1))

print(m.group(0))
print(m.group(2))

p=re.compile(r"(\w+)\s+(\d+[-]\d+[-]\d+)")
m=p.search("park 010-1234-1234")
print(m.group(1))

print(m.group(0))
print(m.group(2))
print(m.group(3))

p=re.compile(r"(\w+)\s+((\d+)[-]\d+[-]\d+)")
m=p.search("park 010-1234-1234")
print(m.group(1))

print(m.group(0))
print(m.group(2))
print(m.group(3))

p=re.compile(r'(\b\w+)\s+\1')
p.search('paris in the the spring').group()
