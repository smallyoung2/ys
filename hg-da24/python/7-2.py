# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 09:41:24 2024

@author: soyoung
"""

#7-2 머신러닝으로 예측하기
#머신러닝: 컴퓨터 프로그램을 사용해 데이터에서 패턴을 학습하는 방법
#인공지능> 머신러닝> (지도학습,비지도학습)
#사이킷런: 파이썬의 대표적인 머신러닝 패키지 pip install scikit-learn
#모델: 머신러닝으로 학습된 패턴을 저장하는 소프트웨어 객체(ex.선형회귀모델)
#지도학습: 데이터에있는 각 샘플에 대한 정답을 알고있는 경우 (정답->타깃) (재료->입력)
#비지도학습: 입력데이터는 있지만 타깃은 없는경우, ex.군집알고리즘
#딥러닝: 머신러닝>딥러닝,, 신경망 알고리즘 사용

#훈련세트와 테스트세트로 나누기
import gdown
gdown.download('https://bit.ly/3pK7iuu','ns_book7.csv', quiet=False)

import pandas as pd
ns_book7=pd.read_csv('ns_book7.csv',low_memory=False)
ns_book7.head()

from sklearn.model_selection import train_test_split

train_set, test_set=train_test_split(ns_book7,random_state=42)

print(len(train_set),len(test_set))         # 282577 94193  (75%와 25%로 나뉘어짐)

#사이킷런에 있는 선형회귀모델 훈련 (train_set에 있는 도서권수열을 사용해 대출건수 예측)

X_train=train_set[['도서권수']]
y_train=train_set['대출건수']
print(X_train.shape, y_train.shape)         # (282577, 1) (282577,) ->(2차원배열, 1차원배열)

#선형회귀모델 훈련하기
from sklearn.linear_model import LinearRegression   #선형회귀 알고리즘

lr=LinearRegression()
lr.fit(X_train, y_train)                    # Out[29]: LinearRegression()



#훈련된 모델을 평가하기: 결정계수R**2 (0~1사이의 값,, 낮을수록 예측 어려움)
X_test=test_set[['도서권수']]
y_test=test_set['대출건수']

lr.score(X_test, y_test)    #0.1002567624933 점수 낮음->도서권수로 대출건수 예측하기 어려움
# 결정계수의 값이 1에 가까울수록 도서권수와 대출건수간에 관계가 깊다고 볼수있다.

#y_train 과 y_train 의 관계 예측

lr.fit(y_train.to_frame(),y_train)          # Out[34]: LinearRegression()
lr.score(y_test.to_frame(),y_test)          # Out[35]: 1.0   두값이 동일하므로 결정계수 1



#연속적인 값 예측하기: 선형회귀: y-ax+b ->x:입력,y타깃
print(lr.coef_,lr.intercept_)           # [1.] -1.2647660696529783e-12
#기울기 1이고, y절편은 0에가까운 매우작은 음수-> y=1x+0 이므로 결정계수 1.




#카테고리 예측하기: 로지스틱회귀 < 분류알고리즘  로지스틱함수(시그모이드함수)
#타깃이 연속적인 실수..회귀
#정수이기때문에 카테고리로,,,분류->(이진분류(0(음성클래스),1(양성클래스)),다중분류)
#분류 알고리즘엥서 타깃 카테고리: 클래스
#선형함수의 결과값 실수z를 로지스틱함수에 통과시키면 y는 0~1->0.5이상(양성클래스),-.5이하(음성클래스)로 예측


#로지스틱 회귀모델 훈련하기
#y_train과y_test를 이진분류에 맞게 바꿔야함
#도서권수로 대출건수가 평균보다 높은지 아닌지를 예측하는 이진분류 문제
borrow_mean=ns_book7['대출건수'].mean()
y_train_c=y_train>borrow_mean           #대출건수 평균보다 높으면 양성 클래스
y_test_c=y_test>borrow_mean             #대출건수 평균보다 높으면 양성 클래스

from sklearn.linear_model import LogisticRegression

logr=LogisticRegression() 
logr.fit(X_train,y_train_c)             #Out[43]: LogisticRegression()
logr.score(X_test,y_test_c)             #Out[44]: 0.7106154385145393
#정확도 약 71%이므로 나쁘지않은 결과


y_test_c.value_counts()             #음성클래스가 더 많음->불균형데이터
"""
대출건수
False    65337
True     28856
Name: count, dtype: int64 """       #음성클래스 약 69% ,양성클래스 약 31%

#더미 모델: 회귀일경우 무조건 타깃의 평균예측, 분류일경우 많은 크래스를 예측으로 출력
from sklearn.dummy import DummyClassifier

dc=DummyClassifier()
dc.fit(X_train,y_train_c)     #Out[48]: DummyClassifier()
dc.score(X_test,y_test_c)     #Out[49]: 0.6936502712515792 ->69%(모델을 만들때 기준점이됨)
#적어도 69%(기준점)보다 높지않으면 유용한 모델이라고 하기 어려움


#평균제곱오차와 평균절댓값오차로 모델 평가하기(선형회귀모델)

lr.fit(X_train,y_train)         #Out[50]: LinearRegression()
y_pred=lr.predict(X_test)       #입력데이터에대한 예측->테스트세트에대한 모델의 예측

from sklearn.metrics import mean_absolute_error

mean_absolute_error(y_test,y_pred)  #Out[53]: 10.358091752853873
#예측이 평균적으로 10 이나 차이난다.

import numpy as np
np.mean(y_test)                     #Out[62]: 11.577558841952163


#y_test에 담긴 대출건수 평균을 계산해보면 11에 가깝다.
#따라서 예측이 타깃과 10이나 차이나는 것은 좋은 결과가 아니다.
#score()메서드 점수가 낮은 것을 보아도 도서권수는 대출건수를 예측하는데 좋은 특성 아니다.

X_test=test_set[['도서권수']]
y_test=test_set['대출건수']

lr.score(X_test, y_test)  #0.1002567624933 점수 낮음->도서권수로 대출건수 예측하기 어려움
# 결정계수의 값이 1에 가까울수록 도서권수와 대출건수간에 관계가 깊다고 볼수있다.



