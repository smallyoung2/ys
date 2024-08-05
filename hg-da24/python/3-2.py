# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 12:02:54 2024

@author: soyoung
"""

#3-2 잘못된 데이터 수정하기
#데이터 프레임 정보 요약 확인하기
import gdown
gdown.download('https://bit.ly/3GisL6J', 'ns_book4.csv',quiet=False)

import pandas as pd
ns_book4=pd.read_csv('ns_book4.csv',low_memory=False)
ns_book4.head()

ns_book4.info()
ns_book4.info(memory_usage='deep')

#누락된 값 처리하기
ns_book4.isna().sum()               #누락된 값 세기
ns_book4.notna().sum()              #누락되지 않은 값 세기

ns_book4['도서권수'].isna().sum()   # 0
ns_book4.loc[0,'도서권수']=None     #도서권수의 첫번째 행을 none 으로 바꿈
ns_book4['도서권수'].isna().sum()   # 1

ns_book4.head(2)                #도서권수 정수에서 실수형으로 바뀜(none은 실수형이므로)

ns_book4.loc[0,'도서권수']=1
ns_book4.head(2)                #여전히 실수형이다

ns_book4=ns_book4.astype({'도서권수':'int32','대출건수':'int32'})
ns_book4.head(2)                # 도서권수,대출건수 정수형으로 바뀐것 확인 가능

ns_book4.loc[0,'부가기호']=None
ns_book4.head(2)                # nan이 문자열 그대로 none으로 바뀜

import numpy as np
ns_book4.loc[0,'부가기호']=np.nan
ns_book4.head(2)

set_isbn_na_rows=ns_book4['세트 ISBN'].isna()     #누락된 값을 찾아 불리언 배열로 반환

ns_book4.loc[set_isbn_na_rows,'세트 ISBN']=''     #누락된 값을 빈문자열로 바꿈
ns_book4['세트 ISBN'].isna().sum()
    

#fillna()
ns_book4.fillna('없음').isna().sum()              #누락된 값을 '없음'으로 모두 바꿈->누락된값 0

ns_book4['부가기호'].fillna('없음').isna().sum()

ns_book4.fillna({'부가기호':'없음'}).isna().sum()

#replace()
ns_book4.replace(np.nan,'없음').isna().sum()

ns_book4.replace([np.nan,'2021'],['없음','21']).head()
ns_book4.replace({np.nan:'없음','2021':'21'}).head()

ns_book4.replace({'부가기호':np.nan},'없음').head()

ns_book4.replace({'부가기호': {np.nan:'없음'}, '발행년도': {'2021':'21' }}).head()


#정규표현식
#숫자 찾기( \d)
ns_book4.replace({'발행년도': {'2021':'21'}})[100:102]

ns_temp=ns_book4.replace({'발행년도':{'2021':'21'}})
ns_temp[100:102]

ns_book4.replace({'발행년도':{r'\d\d(\d\d)': r'\1'}},regex=True)[100:102]
ns_book4.replace({'발행년도':{r'\d{2}(\d{2})': r'\1'}},regex=True)[100:102]

#문자 찾기 (.)
ns_book4.replace({'저자':{r'(.*)\s\(지은이\)(.*)\s\(옮긴이\)':r'\1\2'},
                  '발행년도':{r'\d{2}(\d{2})':r'\1'}}, regex=True)[100:102]

#잘못된 값 바꾸기

ns_book4.astype({'발행년도': 'int32'})      #1988. 이라는 숫자가아닌 문자가 있는 연도있으므로 오류

ns_book4['발행년도'].str.contains('1988').sum()     #407 개의 1988 포함된 행의수 발견

invalid_number=ns_book4['발행년도'].str.contains('\D',na=True)
print(invalid_number.sum())                 # 1777개가 숫자가 아닌 문자가 포함되었다
ns_book4[invalid_number]['발행년도'].head()

ns_book5=ns_book4.replace({'발행년도':r'.*(\d{4}).*'}, r'\1',regex=True)
ns_book5[invalid_number].head()             # 숫자 네자리와 문자 있는 행 숫자 4자리로 변환

unkown_year=ns_book5['발행년도'].str.contains('\D',na=True)
print(unkown_year.sum())                    #숫자 네자리가 없는 행 67개 발견
ns_book5[unkown_year].head()            #nan 이거나  숫자 네자리가 포함되지 않은것 확인

#알지못한 발행년도 모두 -1 로 변환후 데이터 타입 정수형으로 변환
ns_book5.loc[unkown_year,'발행년도']='-1'       # -1로 표시
ns_book5=ns_book5.astype({'발행년도':'int32'})  

ns_book5['발행년도'].gt(4000).sum()         #발행년도가 4000이상인 행의 갯수 131
(ns_book5['발행년도']>4000).sum()               #131

#4000년 이상인 경우 단군기원 사용한 것으로, 
#2333년 빼서 서기로 바꾼후 4000년 넘는 도서 있는지 확인

dangun_yy_rows=ns_book5['발행년도'].gt(4000)
dangun_yy_rows.sum()                    # 131

ns_book5.loc[dangun_yy_rows,'발행년도']=ns_book5.loc[dangun_yy_rows,'발행년도']-2333

dangun_year=ns_book5['발행년도'].gt(4000)
print(dangun_year.sum())                #2333년 뺐는데도 13개의 행이 4000이 넘음

ns_book5[dangun_year].head(2)

ns_book5.loc[dangun_year,'발행년도']=-1     #13개의 행 -1로 표시

#연도가 작은 값 확인, 0보다 크고 1900년 이전의 도서 찾기
old_books=ns_book5['발행년도'].gt(0)& ns_book5['발행년도'].lt(1900)
old_books.sum()                             #6개의 행 발견

ns_book5.loc[old_books,'발행년도']=-1       #6개의 행  -1 로 표시

ns_book5['발행년도'].eq(-1).sum()           #값이 -1 인 행 86 개 발견


#누락된 정보 채우기

na_rows=ns_book5['도서명'].isna()|ns_book5['저자'].isna() \
    |ns_book5['출판사'].isna()| ns_book5['발행년도'].eq(-1)

print(na_rows.sum())                    #5268의 행이 값 누락되거나 알수없음
ns_book5[na_rows].head()

import requests
from bs4 import BeautifulSoup


#도서명을 가져오는 함수 작성
def get_book_title(isbn):
    url='http://www.yes24.com/Product/Search?domain=BOOK&query={}'
    r=requests.get(url.format(isbn))
    soup=BeautifulSoup(r.text,'html.parser')
    #클래스 이름이 'gd_name'인 <a>태그의 텍스트를 가져옵니다.
    title=soup.find('a',attrs={'class':'gd_name'}).get_text()
    return title

get_book_title(9791191266054)       #Out[210]: '골목의 시간을 그리다'


#저자,출판사,발행연도 추출하여 반환하는 함수

import re

def get_book_info(row):
    title=row['도서명']
    author=row['저자']
    pub=row['출판사']
    year=row['발행년도']
    
    url='http://www.yes24.com/Product/Search?domain=BOOK&query={}'
    r=requests.get(url.format(row['ISBN']))
    soup=BeautifulSoup(r.text,'html.parser')
    
    try:
        if pd.isna(author):
            authors=soup.find('span',attrs={'class':'info_auth'}).find_all('a')
            author_list=[auth.get_text() for auth in authors]
            author=','.join(author_list)
            
    except AttributeError:
        pass
    
    try:
        if pd.isna(pub):
            pub=soup.find('span',attrs={'class':'info_pub'}).find('a').get_text()
            
    except AttributeError:
        pass
    
    try:
        if year==-1:
            year_str=soup.find('span',attrs={'class':'info_date'}).get_text()
            year=re.findall(r'\d{4}',year_str)[0]
        
    except AttributeError:
        pass
    
    return title, author, pub, year

updated_sample=ns_book5[na_rows].head(2).apply(get_book_info,axis=1,result_type='expand')
updated_sample


gdown.download('https://bit.ly/3UJZiHw','ns_book5_update.csv',quiet=False)

ns_book5_update=pd.read_csv('ns_book5_update.csv',index_col=0)
ns_book5_update.head()


ns_book5.update(ns_book5_update)

na_rows=ns_book5['도서명'].isna()| ns_book5['저자'].isna()\
    | ns_book5['출판사'].isna() |ns_book5['발행년도'].eq(-1)
    
print(na_rows.sum())


ns_book5=ns_book5.astype({'발행년도':'int32'})
ns_book6=ns_book5.dropna(subset=['도서명','저자','출판사'])
ns_book6=ns_book6[ns_book6['발행년도']!=-1]
ns_book6.head()

ns_book6.to_csv('ns_book6.csv',index=False)


#데이터를 이해하고 올바르게 정제하기
#일괄 처리함수

def data_fixing(ns_book4):
    """잘못된 값을 수정하거나 nan을 채우는 함수
        :param ns_book4 :data_cleaning() 함수에서 전처리된 데이터 프레임"""
    #도서권수와 대출건수를 int32로 바꿉니다
    ns_book4=ns_book4.astype({'도서권수':'int32', '대출건수':'int32'})
    #nan인 세트 isbn을 빈문자열로 바꿉니다.
    set_isbn_na_rows=ns_book4['세트 ISBN'].isna()
    ns_book4.loc[set_isbn_na_rows,'세트 ISBN']=''
    #발행년도 열에서 연도 네자리를 추출하여 대체합니다. 나머지 발행년도는 -1로 변환
    ns_book5=ns_book4.replace({'발행년도':'.*(\d{4}).*'}, r'\1', regex=True)
    unkown_year=ns_book5['발행년도'].str.contains('\D', na=True)
    ns_book5.loc[unkown_year,'발행년도']='-1'
    #발행년도를 int32로 바꿉니다
    ns_book5=ns_book5.astype({'발행년도':'int32'})
    #4000년 이상인 경우 2333년을 뺍니다
    dangun_yy_rows=ns_book5['발행년도'].gt(4000)
    ns_book5.loc[dangun_yy_rows,'발행년도']-=2333
    #여전히 4000년 이상인 경우 -1로 바꿉니다
    dangun_year=ns_book5['발행년도'].gt(4000)
    ns_book5.loc[dangun_year,'발행년도']=-1
    #0~1900년 사이의 발행 년도는 -1 로바꿉니다.
    old_books=ns_book5['발행년도'].gt(0)&ns_book5['발행년도'].lt(1900)
    ns_book5.loc[old_books,'발행년도']=--1
    #도서명, 저자, 출판사가 nan이거나 발행년도가 -1인 행을 찾습니다.
    na_rows=ns_book5['도서명'].isna()|ns_book5['저자'].isna() \
        |ns_book5['출판사'].isna()| ns_book5['발행년도'].eq(-1)
    #yes 24도서 상세 페이지에서 누락된 정보를 채웁니다.
    updated_sample=ns_book5[na_rows].apply(get_book_info,axis=1,result_type='expand')
    updated_sample.columns=['도서명','저자','출판사','발행년도']
    ns_book5.update(updated_sample)
    #도서명, 저자, 출판사가 nan이거나 발행년도가 -1 인행을 삭제합니다
    ns_book6=ns_book5.dropna(subset=['도서명','저자','출판사'])
    ns_book6=ns_book6[ns_book6['발행년도'] !=-1]
    
    return ns_book6