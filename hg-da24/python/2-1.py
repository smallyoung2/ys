# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 11:15:10 2024

@author: soyoung
"""
#2-1 api사용하기

#파이썬에서 json데이터 다루기

d={"name":"혼자 공부하는 데이터 분석"}
print(d['name'])

import json

d_str=json.dumps(d,ensure_ascii=False)
print(d_str)

print(type(d_str))      # <class 'str'>

d2=json.loads(d_str)
print(d2['name'])

print(type(d2))         # <class 'dict'>

d3=json.loads('{"name":"혼자 공부하는 데이터 분석","author":"박해선","year":2022}')

print(d3['name'])
print(d3['author'])
print(d3['year'])

d3=json.loads('{"name":"혼자 공부하는 데이터 분석","author":["박해선","홍길동"],\
              "year":2022}')
    
print(d3['author'][1])

d4_str="""
[
 {"name":"혼자 공부하는 데이터 분석","author":"박해선","year":2022},
 {"name":"혼자 공부하는 머신러닝+딥러닝","author":"박해선","year":2020}
 ] """

d4=json.loads(d4_str)
print(d4[0]['name'])

import pandas as pd
pd.read_json(d4_str)
pd.DataFrame(d4)            # 위아래 결과 같음

#파이썬에서 xml다루기

x_str="""
<book>
    <name>혼자 공부하는 데이터 분석</name>
    <author>박해선</author>
    <year>2022</year>
</book> """

import xml.etree.ElementTree as et
book=et.fromstring(x_str)

print(type(book))           # <class 'xml.etree.ElementTree.Element'>

print(book.tag)             # book

book_childs=list(book)
print(book_childs)
#[<Element 'name' at 0x0000023AA0D762A0>, <Element 'author' at 0x0000023AA0D76B10>, <Element 'year' at 0x0000023AA0D75E40>]

name,author,year=book_childs

print(name.text)            # 혼자 공부하는 데이터 분석
print(author.text)          # 박해선
print(year.text)            # 2022

name=book.findtext('name')
author=book.findtext('author')
year=book.findtext('year')

print(name,author,year)

age=book.findtext('age')    # 존재하지 않는 age 찾기
print(age)                  # None

x2_str="""
<books>
    <book>
        <name>혼자 공부하는 데이터 분석</name>
        <author>박해선</author>
        <year>2022</year>
    </book> 
    <book>
        <name>혼자 공부하는 머신러닝+딥러닝</name>
        <author>박해선</author>
        <year>2020</year>
    </book> 
</books> """

books=et.fromstring(x2_str)
print(books.tag)            # books

for book in books.findall('book'):
    name=book.findtext('name')
    author=book.findtext('author')
    year=book.findtext('year')
    
    print(name,author,year,"\n")
    
pd.read_xml(x2_str)

#파이썬으로 api 호출하기

import requests
import pandas as pd

#인증키를 발급받아 문자열 맨 끝에 추가해주세요.
url="http://data4library.kr/api/loanItemSrch?format=json&startDt=2021-04-01&endDt=2021-04-30&age=20&authKey=c01ec15e4574f74ee45cba2601bad15b82971e606e3b0740977ee4b363ce2fe2"

"""
url 을 분석해보면 다음과 같다.
base_url=http://data4library.kr/api/loanItemSrch
format=json
startDt=2021-04-01
endDt=2021-04-30
age=20
authKey=c01ec15e4574f74ee45cba2601bad15b82971e606e3b0740977ee4b363ce2fe2
"""


r=requests.get(url)

data=r.json()
print(data)
data

data['response']['docs']

books=[]
for d in data['response']['docs']:
    books.append(d['doc'])
    
books=[d['doc'] for d in data['response']['docs']]
books

books_df=pd.DataFrame(books)
books_df

books_df.to_json('20s_best_book.json')


