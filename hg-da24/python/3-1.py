# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 14:14:05 2024

@author: soyoung
"""

#3-1 불필요한 데이터 삭제하기

#열 삭제하기 columns
import gdown

gdown.download('https://bit.ly/3RhoNho','ns_202104.csv',quiet=False)

import pandas as pd

ns_df=pd.read_csv('ns_202104.csv',low_memory=False)
ns_df.head()

ns_book=ns_df.loc[:,'번호':'등록일자']
ns_book.head()

print(ns_df.columns)
print(ns_df.columns[0])
ns_df.columns != 'Unnamed: 13'

#unnamed: 13 칼럼 빼고 보여주기
selected_columns=ns_df.columns !='Unnamed: 13'
ns_book=ns_df.loc[:,selected_columns]
ns_book.head()

#부가기호 칼럼 빼고 보여주기
selected_columns=ns_df.columns !='부가기호'
ns_book=ns_df.loc[:,selected_columns]
ns_book.head()

#unnamed: 13 칼럼 없애기
ns_book=ns_df.drop('Unnamed: 13',axis=1)
ns_book.head()

#부가기호 칼럼 없애기 -> 위에서 uunamed 칼럼 없앤후 부가기호 칼럼 없앴으므로
#두개 모두 없어짐
ns_book=ns_df.drop('부가기호',axis=1)
ns_book.head()

ns_book.drop('주제분류번호',axis=1,inplace=True)
ns_book.head()


print(ns_book.columns)

#dropna()메서드
ns_book=ns_df.dropna(axis=1)
ns_book.head()

ns_book=ns_df.dropna(axis=1, how='all')
ns_book.head()


#행 삭제하기 rows
ns_book2=ns_book.drop([0,1])        #인덱스  0,1 행 삭제
ns_book2.head()

ns_book2=ns_book[2:]
ns_book2.head()

ns_book2=ns_book[0:2]
ns_book2.head()

#[]연산자와 불리언 배열
selected_rows=ns_df['출판사']=='한빛미디어'
ns_book2=ns_book[selected_rows]
ns_book2.head()

ns_book2=ns_book.loc[selected_rows]
ns_book2.head()

ns_book2=ns_book[ns_book['대출건수']>1000]
ns_book2.head()

#중복된 행 찾기 duplicated() 메서드

sum(ns_book.duplicated())

sum(ns_book.duplicated(subset=['도서명','저자','ISBN']))

dup_rows=ns_book.duplicated(subset=['도서명','저자','ISBN'],keep=False)
ns_book3=ns_book[dup_rows]
ns_book3.head()

#그룹별로 모으기
count_df=ns_book[['도서명','저자','ISBN','권','대출건수']]

group_df=count_df.groupby(by=['도서명','저자','ISBN','권'], dropna=False)
loan_count=group_df.sum()


loan_count=count_df.groupby(by=['도서명','저자','ISBN','권'], dropna=False).sum()
loan_count.head()


#원본데이터 업데이트하기
dup_rows=ns_book.duplicated(subset=['도서명','저자','ISBN','권'])  #중복된행 TURE표시
unique_rows=~dup_rows       #불리언 배열 반전시켜서 공유한행을 true 표시
ns_book3=ns_book[unique_rows].copy()     #고유한행만 복사하여 ns_book3에 저장

sum(ns_book3.duplicated(subset=['도서명','저자','ISBN','권']))
         #중복된행 없으므로 고유한행만 잘 고른것 확인
         
ns_book3.set_index(['도서명','저자','ISBN','권'],inplace=True)
ns_book3.head()

#업데이트하기 update()메서드
ns_book3.update(loan_count)
ns_book3.head()

ns_book4=ns_book3.reset_index()
ns_book4.head()

sum(ns_book['대출건수']>100)
sum(ns_book4['대출건수']>100)

ns_book4=ns_book4[ns_book.columns]      #원래의 열 순서대로 ns_book4 열 순서 변경
ns_book4.head()

ns_book4.to_csv('ns_book4.csv',index=False)


#일괄 처리 함수 만들기

def data_cleaning(filename):
    """ 남산 도서관 장서 csv데이터 전처리 함수:
        param filename: csv 파일이름"""
    #파일을 데이터 프레임으로 읽습니다
    ns_df=pd.read_csv(filename,low_memory=False)
    #nan 열을 삭제합니다.
    ns_book=ns_df.dropna(axis=1,how='all')
    #대출건수를 합치기위해 필요한 행만 추출하여 count_df 데이터 프레임을 만듭니다
    count_df=ns_book[['도서명','저자','ISBN','권','대출건수']]
    #도서명, 저자, ISBN, 권을 기준으로 대출건수를 groupby합니다.
    loan_count=count_df.groupby(by=['도서명','저자','ISBN','권'],
                                dropna=False).sum()
    #원본 데이터프레임에서 중복된행을 제거하고 고유한 행만 추출하여 복사합니다
    dup_rows=ns_book.duplicated(subset=['도서명','저자','ISBN','권'])
    unique_rows=~dup_rows
    ns_book3=ns_book[unique_rows].copy()
    #도서명, 저자, ISBN, 권을 인덱스로 설정합니다
    ns_book3.set_index(['도서명','저자','ISBN','권'], inplace=True)
    #loan_count에 저장된 누적 대출건수를 업데이트 합니다.
    ns_book3.update(loan_count)
    #인덱스 재설정
    ns_book4=ns_book3.reset_index()
    #원본데이터 프레임의 열순서로 변경합니다.
    ns_book4=ns_book4[ns_book.columns]
    
    return ns_book4

new_ns_book4=data_cleaning('ns_202104.csv')
ns_book4.equals(new_ns_book4)

#true 반환: new_ns_book4와 ns_book4 의 결과는 같다.