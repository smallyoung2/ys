# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 16:51:31 2024

@author: soyoung
"""

#7-1 통계적으로 추론하기
#모수검정이란: 모집단에 대한 파라미터(평균,분산...)를 추정하는 방법
#표준점수(z점수)구하기:각 값이 평균에서 얼마나 떨어져있는지 표준편라를 사용해 변환한 점수

#z점수 구하기
import numpy as np
x=[0,3,5,7,10]
s=np.std(x)
m=np.mean(x)
z=(7-m)/s
print (z)

from scipy import stats
stats.zscore(x)

#누적분포 이해하기
stats.norm.cdf(0)       #0까지의 누적분포 0.5
stats.norm.cdf(1.0)-stats.norm.cdf(-1.0) #Out[349]: 0.6826894921370859
stats.norm.cdf(2.0)-stats.norm.cdf(-2.0) #Out[350]: 0.9544997361036416

stats.norm.ppf(0.9) #Out[351]: 1.2815515655446004

#중심극한정리: 무작위로 샘플을뽑아 만듣 표본의 평균은 정규분포에 가깝다..이론
import gdown
gdown.download('https://bit.ly/3pK7iuu','ns_book7.csv', quiet=False)

import pandas as pd
ns_book7=pd.read_csv('ns_book7.csv',low_memory=False)
ns_book7.head()

import matplotlib.pyplot as plt
plt.hist(ns_book7['대출건수'],bins=50)
plt.yscale('log')
plt.show()

#샘플링하기
#샘플링 크기30
np.random.seed(42)
sample_means=[]
for _ in range(1000):
    m=ns_book7['대출건수'].sample(30).mean()
    sample_means.append(m)
    
plt.hist(sample_means,bins=30)
plt.show()

#샘플링크기와 정확도
np.mean(sample_means)       #무작위로 뽑은 표본의 통계량 Out[360]: 11.539900000000001
ns_book7['대출건수'].mean() #실제 모집단의 통계량        Out[362]: 11.593438968070707


#샘플링 크기20
np.random.seed(42)
sample_means=[]
for _ in range(1000):
    m=ns_book7['대출건수'].sample(20).mean()
    sample_means.append(m)
np.mean(sample_means)                    #샘플링 크기20:  Out[366]: 11.39945

#샘플링 크기40
np.random.seed(42)
sample_means=[]
for _ in range(1000):
    m=ns_book7['대출건수'].sample(40).mean()
    sample_means.append(m)
np.mean(sample_means)                   #샘플링 크기40:  Out[367]: 11.5613

#샘플링 크기 클수록 실제 모집단평균에 가까워짐.

np.std(sample_means)           #표본으로 표준편차를 구했을때:   Out[368]: 3.0355987564235165
np.std(ns_book7['대출건수'])/np.sqrt(40) #모집단 표준편차/루트40:Out[369]: 3.048338251806833


#모집단의 평균범위 추정하기:신뢰구간
python_books_index=ns_book7['주제분류번호'].str.startswith('00')&\
    ns_book7['도서명'].str.contains('파이썬')
python_books=ns_book7[python_books_index]
python_books.head()

len(python_books)           #Out[372]: 251
python_mean=np.mean(python_books['대출건수'])
python_mean                 #Out[376]: 14.749003984063744 파이썬 도서 대출건수 평균

python_std=np.std(python_books['대출건수'])
python_se=python_std/np.sqrt(len(python_books))
python_se                   #Out[379]: 0.8041612072427442  표준오차

#95%이내 구간에 포함된다고 확신하고싶음
stats.norm.ppf(0.975)       #Out[380]:  1.959963984540054
stats.norm.ppf(0.025)       #Out[381]: -1.9599639845400545

print(python_mean-1.96*python_se,python_mean+1.96*python_se)
# 13.172848017867965 16.325159950259522  모집단의 평균이 13.2~16.3 에있을거라고 95%확신한다.



#통계적 의미 확인하기:가설검정(표본에 대한 정보를 사용해 모집단의 파라미터에대한 가정 검정)
#영가설(귀무가설):파이썬과 c++도서의 평균 대출건수가 같다는 가설(H0)
#대립가설: 반대로, 파이썬과 c++도서의 평균 대출건수가 같지 않다는 가설(H A)

#Z점수로 가설 검증하기
cplus_books_index=ns_book7['주제분류번호'].str.startswith('00')&\
    ns_book7['도서명'].str.contains('C++',regex=False)
cplus_books=ns_book7[cplus_books_index]
cplus_books.head()

len(cplus_books)            #Out[386]: 89

cplus_mean=np.mean(cplus_books['대출건수'])
cplus_mean                  #Out[388]: 11.595505617977528  C++도서 대출건수 평균

cplus_se=np.std(cplus_books['대출건수'])/np.sqrt(len(cplus_books))
cplus_se                    #Out[390]: 0.9748405650607009  표준오차

#가설검정 공식에 대입,, 영가설에 따르면 두 모집단의 평균은같다.
(python_mean-cplus_mean)/np.sqrt(python_se**2+cplus_se**2)  #Out[392]: 2.495408195140708
stats.norm.cdf(2.4954)      #Out[393]: 0.9937092393728792 ->0.994 이므로
#정규분포 양쪽 끝의 면적은 각각 1-0.994=0.006 이된다.
#즉 p의 값은 0.006*2=0.012 로 유의수준에 해당하는 0.05 보다 작다.. 
#따라서 영가설 기각,, 대립가설 지지->파이썬과 c++ 도서의 평균 대출건수 같지 않다.



#t검정으로 가설 검증하기 ttest_ind()함수
t, pvalue=stats.ttest_ind(python_books['대출건수'],cplus_books['대출건수'])

print(t,pvalue)         #2.1390005694958574 0.03315179520224784
#p 값은 0.05보다 작은 0.033이므로 영가설기각,,,두 도서의 대출건수 평균의 차이는 우연이 아님


#정규분포가 아닐때 가설 검증하기: 순열검정(비모수검정방법중 하나임)
#모집단의 분포가 정규분포를 따르지 않거나, 모집단의 분포를 알수 없을때 사용

def statistic(x,y):
    return np.mean(x)-np.mean(y)

def permutation_test(x,y):
    #표본의 평균차이를 계산
    obs_diff=statistic(x,y)
    #두표본 합침
    all=np.append(x,y)
    diffs=[]
    np.random.seed(42)
    #순열검정 1000번 반복
    for _ in range(1000):
        #전체 인덱스 섞음
        idx=np.random.permutation(len(all))
        #랜덤하게 두그룹으로 나눈 다음 평균차이 계산
        x_=all[idx[:len(x)]]
        y_=all[idx[len(x):]]
        diffs.append(statistic(x_,y_))
    #원본표본보다 작거나 큰 경우의 p-값을 계산
    less_pvalue=np.sum(diffs<obs_diff)/1000
    greater_pvalue=np.sum(diffs>obs_diff)/1000
    #둘중 작은 p-값을 선택하여 2를 곱하여 최종 p-값을 반환합니다
    return obs_diff,np.minimum(less_pvalue,greater_pvalue)*2

#표본의 평균차이보다 큰 경우와 작은경우의 비율을 계산하여 p값 계산,
#일반적으로 영가설을 기각하는 것이 목적이므로 둘중 작은값을 선택하여 
# 2를 곱하고, 양쪽꼬리에 해당하는 비율얻음->영가설이 옳다고 가정했을때 관측될 확률

#도서 대출건수 평균 비교하기1. 파이썬 vs c++

permutation_test(python_books['대출건수'],cplus_books['대출건수'])
#Out[4]: (3.1534983660862164, 0.022) ->표본의 평균차이,pvalue=0.022이므로 영가설 기각.
#-> 두 도서의 평균 대출건수에는 차이가 있다..!


#사이파이 1.8 버전 이상에서 제공하는 순열검정함수
res=stats.permutation_test((python_books['대출건수'], cplus_books['대출건수']),statistic,random_state=42)

print(res.statistic,res.pvalue)             #3.1534983660862164 0.0258  


#도서 대출건수 평균 비교하기1. 파이썬 vs 자바스크립트
java_books_indx=ns_book7['주제분류번호'].str.startswith('00')&\
    ns_book7['도서명'].str.contains('자바스크립트')
java_books=ns_book7[java_books_indx]
java_books.head()

print(len(java_books),np.mean(java_books['대출건수'])) # 105 15.533333333333333

permutation_test(python_books['대출건수'],java_books['대출건수'])
# Out[15]: (-0.7843293492695889, 0.566) -> p-value값이 0.566으로 0.05보다 큼
# -> 유의수준보다 p-값이 크므로 영가설 지지, 파이썬과 자바도서 사이의 평균 대출건수 차이없다.

