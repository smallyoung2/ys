# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 17:10:47 2024

@author: soyoung
"""

#4-1 통계로 요약하기
#기술통계구하기

import gdown
gdown.download('https://bit.ly/3736JW1','ns_book6.csv',quiet=False)

import pandas as pd
ns_book6=pd.read_csv('ns_book6.csv',low_memory=False)
ns_book6.head()

ns_book6.describe()

sum(ns_book6['도서권수']==0)        #도서권수가 0인 행은 3206개

#도서권수가 0인 행 제외
ns_book7=ns_book6[ns_book6['도서권수']>0]

ns_book7.describe(percentiles=[0.3,0.6,0.9])

ns_book7.describe(include='object')

#평균 구하기
x=[10,20,30]
sum=0
for i in range(3):
    sum+=x[i]
print("평균:",sum/len(x))

ns_book7['대출건수'].mean()

#중앙값 구하기
ns_book7['대출건수'].median()

temp_df=df=pd.DataFrame([1,2,3,4])
temp_df.median()

#중복값 제거하고 중앙값 구하기
ns_book7['대출건수'].drop_duplicates().median()

#최대값, 최소값 구하기
ns_book7['대출건수'].min()
ns_book7['대출건수'].max()

#분위수 구하기
ns_book7['대출건수'].quantile(0.25)
ns_book7['대출건수'].quantile([0.25,0.5,0.75])

pd.Series([1,2,3,4,5]).quantile(0.9)        #interpolation=linear으로 기본값 지정됨

#0.9이므로 0.75 분위수값과 1.00 분위수 값 이 기준이됨

#분위수에 상관없이 무조건 중앙값, 4와 5
pd.Series([1,2,3,4,5]).quantile(0.9,interpolation='midpoint')       #4.5
#두수 중에서 가까운값 (0.9 가 1에 가깝기때문에)
pd.Series([1,2,3,4,5]).quantile(0.9,interpolation='nearest')        #5

#백분위 구하기
borrow_10_flag=ns_book7['대출건수']<10
borrow_10_flag.mean()                    #Out[275]: 0.6402712530190833
ns_book7['대출건수'].quantile(0.65)      #Out[276]: 10.0


#분산구하기
import numpy as np
np.var(ns_book7['대출건수'])        #Out[6]: 371.6946438971496 넘파이 이용,n으로 나눔
ns_book7['대출건수'].var()          #Out[7]: 371.69563042906674 판다스 이용,n-1로 나눔

np.var(ns_book7['대출건수'],ddof=1) #Out[8]: 371.69563042906674 넘파이 이용,n-1으로 나눔
ns_book7['대출건수'].var(ddof=0)    #Out[10]: 371.6946438971496 판다스 이용, n으로나눔


#표준편차 구하기
np.std(ns_book7['대출건수'])        #Out[12]: 19.27938390865096  ddof생략, 기본값:0

#최빈값 구하기
values, counts=np.unique(ns_book7['도서명'],return_counts=True)

max_idx=np.argmax(counts)           #등장횟수가 가장많은 값의 인덱스 찾기.argmax()
values[max_idx]                     #Out[18]: '승정원일기'


#확인문제
#3
#판다스이용
a=[1,10,3,6,20]

pd.Series(a).var()          #Out[28]: 56.5
pd.Series(a).std()          #Out[29]: 7.516648189186454

#넘파이 이용
a = [1, 2, 3, 4, 5]
a_np = np.array(a)
variance = a_np.var()
print(variance)             #Out[23]: 45.2
print(a_np.std())           #6.723094525588644


#4
ns_book7[['출판사','대출건수']].groupby('출판사').mean().sort_values('대출건수',ascending=False).head(10)

#5
target_range=[ns_book7['대출건수'].quantile(0.25),ns_book7['대출건수'].quantile(0.75)]
print(target_range)                                 #[2.0, 14.0]

target_bool_idx=(ns_book7['대출건수']>=target_range[0])\
    &(ns_book7['대출건수']<=target_range[1])    #대출건수가 2.0이상 14.0 이하이면 ture
target_bool_idx.sum()/len(ns_book7)*100         
