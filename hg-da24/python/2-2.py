# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 11:53:25 2024

@author: soyoung
"""

# 2.2 스크래핑 사용학
#검색결과 페이지 가져오기

import gdown
 
gdown.download("https://bit.ly/3q9SZix",'20s_best_book.json',quiet=False)

import pandas as pd

books_df=pd.read_json('20s_best_book.json')
books_df.head()

books=books_df[['no','ranking','bookname','authors','publisher','publication_year','isbn13']]
books.head()

books_df.loc[[0,1],['bookname','authors']]
books_df.loc[0:1,'bookname':'authors']

books=books_df.loc[:,'no':'isbn13']
books.head()

books_df.loc[::2,'no':'isbn13'].head()

import requests

isbn=9791190090018
url='http://www.yes24.com/Product/Search?domain=BOOK&query={}'

r=requests.get(url.format(isbn))

print(r.text)


#뷰티풀수프

from bs4 import BeautifulSoup

soup=BeautifulSoup(r.text,'html.parser')

prd_link=soup.find('a',attrs={'class':'gd_name'})

print(prd_link)

print(prd_link['href'])         # /Product/Goods/74261416

#우리가 빛의 속도로 갈 수 없다면 의 상세 페이지 가져오기
url='http://www.yes24.com'+prd_link['href']
r=requests.get(url)

print(r.text)

soup=BeautifulSoup(r.text,'html.parser')
prd_detail=soup.find('div',attrs={'id':'infoset_specific'})
print(prd_detail)

prd_tr_list=prd_detail.find_all('tr')
print(prd_tr_list)

for tr in prd_tr_list:
    if tr.find('th').get_text()=='쪽수, 무게, 크기':
        page_td= tr.find('td').get_text()
        break
    
print(page_td)

print(page_td.split()[0])


#전체 도서의 쪽수 구하기

def get_page_cnt(isbn):
    #yes24 도서 검색 페이지 url
    url='http://www.yes24.com/Product/Search?domain=BOOK&query={}'
    #url 에 isbn을 넣어 html 가져오기
    r=requests.get(url.format(isbn))
    soup=BeautifulSoup(r.text,'html.parser')        #html파싱
    #검색결과에서 해당도서를 선택합니다.
    prd_info=soup.find('a',attrs={'class':'gd_name'})
    if prd_info==None:
        return ''
    #도서 상세 페이지 가져오기
    url='http://www.yes24.com'+prd_info['href']
    r=requests.get(url)
    soup=BeautifulSoup(r.text,'html.parser')        #html파싱
    #상품 상세정보 div를 선택합니다
    prd_detail=soup.find('div',attrs={'id':'infoset_specific'})
    #테이블에 있는 tr태그를 가져옵니다.
    prd_tr_list=prd_detail.find_all('tr')
    #쪽수가 들어있는 th를 찾아 td에 담긴 값을 반환합니다.
    for tr in prd_tr_list:
        if tr.find('th').get_text()=='쪽수, 무게, 크기':
            return tr.find('td').get_text().split()[0]
    return ''
    
get_page_cnt(9791190090018)

top10_books=books.head(10)

def get_page_cnt2(row):
    isbn=row['isbn13']
    return get_page_cnt(isbn)

page_count=top10_books.apply(get_page_cnt2,axis=1)
print(page_count)

page_count=top10_books.apply(lambda row:get_page_cnt(row['isbn13']),axis=1)

page_count.name='page_count'
print(page_count)

top10_with_page_count=pd.merge(top10_books,page_count,left_index=True,right_index=True)
top10_with_page_count


#merge()함수의 매개변수
df1=pd.DataFrame({'col1':['a','b','c'], 'col2':[1,2,3]})
df1

df2=pd.DataFrame({'col1':['a','b','d'], 'col3':[10,20,30]})
df2

pd.merge(df1,df2,on='col1')
pd.merge(df1,df2)                   #위 코드와 같은 결과 

pd.merge(df1,df2,how='left',on='col1')
pd.merge(df1,df2,how='right',on='col1')

pd.merge(df1,df2,how='outer',on='col1')

pd.merge(df1,df2,left_on='col1',right_on='col1')

pd.merge(df1,df2,left_on='col2',right_index=True)
