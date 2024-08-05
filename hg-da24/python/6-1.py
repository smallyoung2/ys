# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 12:33:56 2024

@author: soyoung
"""

#6-1 객체지향 API로 그래프 꾸미기
#pyplot과 객체지향 api 방식

import matplotlib.pyplot as plt

plt.rcParams['figure.dpi']=100      #해상도 높여줌

#pyplot방식으로 그래프 그리기
plt.plot([1,4,9,16])                #인덱스 x축, 원소 y축
plt.title('simple line graph')
plt.show()

#객체지향 API방식으로 그래프 그리기
fig,ax=plt.subplots()
ax.plot([1,4,9,16])
ax.set_title('simple line graph')
fig.show()

#그래프에 한글 출력하기
import matplotlib.pyplot as plt

#폰트지정하기1. font.family 속성
plt.rcParams['font.family']             # Out[132]: ['sans-serif']
plt.rcParams['font.family']='Malgun Gothic'
plt.rcParams['font.family']             # Out[157]: ['Malgun Gothic']
    
#폰트지정하기2. rc()함수
plt.rc('font',family='Malgun Gothic')
plt.rc('font',family='Malgun Gothic', size=11)
print(plt.rcParams['font.family'], plt.rcParams['font.size']) # ['NanumBarunGothic'] 11.0

#맷 플롯립에서 사용할수있는 폰트의 전체목록 
from matplotlib.font_manager import findSystemFonts
findSystemFonts()                       # 사용할수 있는 폰트 전체목록 출력됨

plt.plot([1,4,9,16])
plt.title('간단한 선그래프')
plt.show()

plt.rc('font',size=10)


#출판사별 발행도서 개수 산점도 그리기
import gdown
gdown.download('https://bit.ly/3pK7iuu','ns_book7.csv', quiet=False)

import pandas as pd
ns_book7=pd.read_csv('ns_book7.csv',low_memory=False)
ns_book7.head()

top30_pubs=ns_book7['출판사'].value_counts()[:30]
top30_pubs


top30_pubs_idx=ns_book7['출판사'].isin(top30_pubs.index)
top30_pubs_idx                  #top30인 출판사는 true, 아닌 출판사는 false로 불리언배열 만듬

top30_pubs_idx.sum()            #상위 30개 출판사의 발행도서개수 Out[179]: 51886

#50000개가 넘으므로 산점도 그리기에 데이터가 많음->1000개만 랜덤으로 선택
ns_book8=ns_book7[top30_pubs_idx].sample(1000,random_state=42)
ns_book8.head()

#ns_book8로 산점도 그리기
fig,ax=plt.subplots(figsize=(10,8))     #피겨의 크기 (10,8) 로지정
ax.scatter(ns_book8['발행년도'],ns_book8['출판사'])
ax.set_title('출판사별 발행도서')
fig.show()

#값에 따라 마커크기를 다르게 나타내기 (s매개변수)
fig, ax=plt.subplots(figsize=(10,8))
ax.scatter(ns_book8['발행년도'],ns_book8['출판사'],s=ns_book8['대출건수'])
ax.set_title('출판사별 발행도서')
fig.show()

#마커 꾸미기
#투명도 조절(alpha매개변수) 
#마커테두리 색바꾸기(edgecolor매개변수) 기본값:face
#마커테두리 선 두께 바꾸기(linewidths매개변수) 기본값:1.5
#산점도 색 바꾸기(c매개변수) 
fig, ax=plt.subplots(figsize=(10,8))
ax.scatter(ns_book8['발행년도'],ns_book8['출판사'],linewidths=0.5,edgecolors='k',\
           alpha=0.3,s=ns_book8['대출건수']*2,c=ns_book8['대출건수'])
ax.set_title('출판사별 발행도서')
fig.show()

#값에따라 색상 표현하기:컬러맵(cmap매개변수),컬러막대(colorbar(매개변수))
fig, ax=plt.subplots(figsize=(10,8))
sc=ax.scatter(ns_book8['발행년도'],ns_book8['출판사'],linewidths=0.5,edgecolors='k',\
           alpha=0.3,s=ns_book8['대출건수']*1.3,c=ns_book8['대출건수'],cmap='jet')
ax.set_title('출판사별 발행도서')
fig.colorbar(sc)
fig.show()
