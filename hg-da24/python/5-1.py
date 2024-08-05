# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 10:51:14 2024

@author: soyoung
"""

#5-1 맷플롯립 기본요소 알아보기

#Figure 객체: 모든 그래프 구성요소를 담고있는 최상위 객체
import gdown
gdown.download('https://bit.ly/3pK7iuu','ns_book7.csv', quiet=False)

import pandas as pd
ns_book7=pd.read_csv('ns_book7.csv',low_memory=False)
ns_book7.head()

import matplotlib.pyplot as plt
plt.scatter(ns_book7['도서권수'],ns_book7['대출건수'],alpha=0.1)
plt.show()

plt.figure(figsize=(9,6))
plt.scatter(ns_book7['도서권수'],ns_book7['대출건수'],alpha=0.1)
plt.show()

print(plt.rcParams['figure.dpi'])       #현재 설치된 맷플롯립의 기본그래프크기:72.0

plt.figure(figsize=(900/72 ,600/72))
plt.scatter(ns_book7['도서권수'],ns_book7['대출건수'],alpha=0.1)
plt.show()

#그래프 주변에 공백 만들기->그래프 작아짐
%config InlineBackend.print_figure_kwargs={'bbox_inches':None}
plt.figure(figsize=(900/72, 600/72))
plt.scatter(ns_book7['도서권수'],ns_book7['대출건수'],alpha=0.1)
plt.show()

#그래프 주변의 공백없애기 타이트하게->그래프커짐
%config InlineBackend.print_figure_kwargs={'bbox_inches':'tight'}

plt.figure(dpi=144)
plt.scatter(ns_book7['도서권수'],ns_book7['대출건수'],alpha=0.1)
plt.show()



#rcParams객체: 그래프의 기본값을 관리하는 객체
#dpi 기본값 바꾸기
plt.rcParams['figure.dpi']=100
#산점도 마커모양바꾸기
plt.rcParams['scatter.marker']      #기본값출력:  Out[36]: 'o'

plt.rcParams['scatter.marker']='*'
plt.scatter(ns_book7['도서권수'],ns_book7['대출건수'],alpha=0.1) #산점도가 별모양으로 그려짐
plt.show()

#마커의 기본값을 바꾸기대신 한번 마커의 모양 바꾼다면 maker매개변수 사용
plt.scatter(ns_book7['도서권수'],ns_book7['대출건수'],alpha=0.1, marker='+')
plt.show()




#여러개의 서브플롯 출력하기
fig,axs=plt.subplots(2)
axs[0].scatter(ns_book7['도서권수'],ns_book7['대출건수'],alpha=0.1) #첫번째 그래프
axs[1].hist(ns_book7['대출건수'],bins=100)                          #두번째 그래프
axs[1].set_yscale('log')
fig.show()

fig,axs=plt.subplots(2,figsize=(6,8))       #size조절
axs[0].scatter(ns_book7['도서권수'],ns_book7['대출건수'],alpha=0.1) #첫번째 그래프
axs[0].set_title('scatter plot')                          #첫번째 그래프의 제목 삽입
axs[1].hist(ns_book7['대출건수'],bins=100)                          #두번째 그래프
axs[1].set_title('histogram')                             #두번째 그래프의 제목 삽입
axs[1].set_yscale('log')
fig.show()


fig,axs=plt.subplots(1,2,figsize=(10,4))
axs[0].scatter(ns_book7['도서권수'],ns_book7['대출건수'],alpha=0.1) #첫번째 그래프
axs[0].set_title('scatter plot')                          #첫번째 그래프의 제목 삽입
axs[0].set_xlabel('number of books')
axs[0].set_ylabel('borrow count')
axs[1].hist(ns_book7['대출건수'],bins=100)                          #두번째 그래프
axs[1].set_title('histogram')                             #두번째 그래프의 제목 삽입
axs[1].set_yscale('log')
axs[1].set_xlabel('borrow count')
axs[1].set_ylabel('frequency')
fig.show()

#확인문제
#3
plt.rcParams['scatter.marker']="o"
plt.scatter(ns_book7['도서권수'],ns_book7['대출건수'],alpha=0.1)
plt.show()
