# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 09:42:10 2024

@author: soyoung
"""

#4-2분포 요약하기
#산점도 그리기

import gdown
gdown.download('https://bit.ly/3pK7iuu','ns_book7.csv',quiet=False)

import pandas as pd
ns_book7=pd.read_csv('ns_book7.csv',low_memory=False)
ns_book7.head()

import matplotlib.pyplot as plt

plt.scatter([1,2,3,4],[1,2,3,4])
plt.show()

plt.scatter(ns_book7['번호'],ns_book7['대출건수'])    
plt.show()            #x축:번호, y축:대출건수

plt.scatter(ns_book7['도서권수'],ns_book7['대출건수'])
plt.show()            #x축:도서권수, y축:대출건수

plt.scatter(ns_book7['도서권수'],ns_book7['대출건수'],alpha=0.1)
plt.show()            #x축:도서권수, y축:대출건수, alpha(0에가까울수록 투명, 범위0~1)

average_borrows=ns_book7['대출건수']/ns_book7['도서권수']
plt.scatter(average_borrows,ns_book7['대출건수'],alpha=0.1)
plt.show()            #x축:대출건수/도서권수, y축:대출건수, 기울기 양수이므로 양의상관관계


#히스토그램 그리기
# 구간안에 속한 데이터의 개수: 도수

plt.hist([0,3,5,6,7,7,9,13],bins=5)
plt.show()           #bins=5 :데이터를 5개의 구간으로 나누어 히스토그램 생성

import numpy as np
np.histogram_bin_edges([0,3,5,6,7,7,9,13], bins=5)
#Out[68]: array([ 0. ,  2.6,  5.2,  7.8, 10.4, 13. ])

np.random.seed(42)
random_samples=np.random.randn(1000)

print(np.mean(random_samples),np.std(random_samples))
# 0.01933205582232549 0.9787262077473543  평균이 0, 표준편차가 1에 가까울수록 표준정규분포에 따름

plt.hist(random_samples)
plt.show()                  #평균 0을 중심으로 볼록한 종모양의 분포:표쥰정규분포의 형태

plt.hist(ns_book7['대출건수']) #대출건수 대부분 작으므로 막대 한개 그려짐->구간 조정하기

plt.hist(ns_book7['대출건수'])
plt.yscale('log')               #y축이 로그로 10의 0, 10의 1, 10의 2 제곱,,등으로 변환됨
plt.show()                      #yscale

plt.hist(ns_book7['대출건수'],bins=100)
plt.yscale('log')
plt.show()

title_len=ns_book7['도서명'].apply(len)
plt.hist(title_len,bins=100)
plt.show()                      #도서명의 title 길이를 반환하여 히스토그램 출력

plt.hist(title_len,bins=100)
plt.xscale('log')
plt.show()                      #x축에 로그스케일 적용 xscale


#상자수염 그리기
#IQR= 3분위수(0.75)-1분위수(0.25)

plt.boxplot(ns_book7[['대출건수','도서권수']])  #1번상자:대출건수, 2번상자:도서권수

plt.boxplot(ns_book7[['대출건수','도서권수']])
plt.yscale('log')
plt.show()

plt.boxplot(ns_book7[['대출건수','도서권수']],vert=False)   #vert=false는 수평으로 박스플롯 그림
plt.xscale('log')
plt.show()

plt.boxplot(ns_book7[['대출건수','도서권수']],whis=10)  #whis: 수염의 길이 조정
#기본적으로 수염의 길이는 igr의 1.5배, 기본값:1.5,, 위는 IQR의 10배로 멀리떨어진 데이터까지 표시

plt.boxplot(ns_book7[['대출건수','도서권수']], whis=(0,100))
plt.yscale('log')
plt.show()              #whis매개변수 백분율로 지정


#통계량을 시각적으로 표현하기
#좀더 알아보기: 판다스의 그래프함수
ns_book7.plot.scatter('도서권수','대출건수',alpha=0.1)
plt.show()

ns_book7['도서명'].apply(len).plot.hist(bins=100)
plt.show()

ns_book7[['대출건수','도서권수']].boxplot()
plt.yscale('log')
plt.show()

#x축, y축의 열이름이 한글이여서 제대로 출력 x-> 6장에서 

#확인문제
#4
selected_rows=(ns_book7['발행년도']>=1980) &(ns_book7['발행년도']<=2022)
plt.hist(ns_book7.loc[selected_rows,'발행년도'])
plt.show()


#5
plt.boxplot(ns_book7.loc[selected_rows,'발행년도'])
