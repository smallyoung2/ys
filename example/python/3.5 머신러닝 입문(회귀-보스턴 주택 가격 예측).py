# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 17:01:08 2024

@author: soyoung
"""
#chap3-5
#회귀-보스턴 주택가격 예측
#3.5.1 데이터 로딩
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn import datasets


data_url = "http://lib.stat.cmu.edu/datasets/boston"
raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)
data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
target = raw_df.values[1::2, 2]

columns = ['CRIM','ZN','INDUS','CHAS','NOX','RM','AGE','DIS','RAD','TAX','PTRATIO','B','LSTAT']
data = pd.DataFrame(data, columns = columns)
target = pd.DataFrame(target, columns = ['Target'])

df = pd.concat([data, target], axis=1)

print(data.shape)
print(target.shape)

df=pd.concat([data,target],axis=1)
df.head(2)

#3.5.2 데이터 탐색
df.info()

df.isnull().sum()

df_corr=df.corr()                               #상관관계행렬

plt.figure(figsize=(10,10))                     #히트맵 그리기
sns.set(font_scale=0.8)
sns.heatmap(df_corr,annot=True,cbar=True)
plt.show()

    #변수간의 상관관계 분석-Target변수와 상관관계가 높은 순서대로 정리
corr_order=df.corr().loc[:'LSTAT','Target'].abs().sort_values(ascending=False)
corr_order

plot_cols=['Target','LSTAT','RM','PTRATIO','INDUS']     #target변수와 상관관계 높은 4개의 피처 추출
plot_df=df.loc[:,plot_cols]
print(plot_df)

plt.figure(figsize=(10,10))                             # LSTAT와 RM의 선형관계 뚜렷한것 확인 가능
for idx,col in enumerate(plot_cols[1:]):
    ax1=plt.subplot(2,2,idx+1)
    sns.regplot(x=col,y=plot_cols[0],data=plot_df,ax=ax1)
plt.show()

sns.displot(x='Target',kind='hist',data=df)
plt.show()

#3.5.3 데이터 전처리
from sklearn.preprocessing import MinMaxScaler
scaler=MinMaxScaler()

df_scaled=df.iloc[:,:-1]                                # target 열을 제외한 나머지 13개 열 추출
scaler.fit(df_scaled)
df_scaled=scaler.transform(df_scaled)                   #정규화시킨 데이터

df.iloc[:,:-1]=df_scaled[:,:]
df.head()

from sklearn.model_selection import train_test_split
x_data=df.loc[:,['LSTAT','RM']]                         # x -> LSTAT:저소득층, RM:방 개수
y_data=df.loc[:,'Target']                               # Y -> Target:주택 가격

# 80% : 20% 로 분류
x_train,x_test,y_train,y_test=train_test_split(x_data,y_data,test_size=0.2,shuffle=True,random_state=42)  

print(x_train.shape,y_train.shape)                      #(404, 2) (404,)
print(x_test.shape,y_test.shape)                        #(102, 2) (102,)


#3.5.4 베이스라인모델- 선형회귀
from sklearn.linear_model import LinearRegression

lr=LinearRegression()
lr.fit(x_train,y_train)

print("coef:",np.round(lr.coef_,1))                     #coef: [-22.9  28.5]
print("intercept:",np.round(lr.intercept_,1))           #intercept: 14.5

y_test_pred=lr.predict(x_test)

plt.figure(figsize=(10,5))
plt.scatter(x_test['LSTAT'],y_test,label='y_test')
plt.scatter(x_test['LSTAT'],y_test_pred,c='r',label='y_pred')
plt.legend(loc='best')
plt.show()

#3.5.5 모델성능평가
from sklearn.metrics import mean_squared_error
y_train_pred=lr.predict(x_train)

train_mse=mean_squared_error(y_train,y_train_pred)
print('train mse: %.4f'%train_mse)                       #train mse: 30.3919

test_mse=mean_squared_error(y_test,y_test_pred)
print('test mse: %.4f'%test_mse)                         #rest mse: 31.2433


from sklearn.model_selection import cross_val_score
lr=LinearRegression()
mse_scores=-1*cross_val_score(lr,x_train,y_train,cv=5,scoring='neg_mean_squared_error')

print('개별 fold의 mse: ',np.round(mse_scores,4))   #개별 fold의 mse: [27.5837 40.9142 31.2975 27.3362 30.8936]
print('평균 mse: %.4f'%np.mean(mse_scores))         #평균 mse: 31.6050


#3.5.6 과대적합 회피 (L2/L1규제) //과대적합x, 과소적합x -> 균형점 찾는 것 중요

#5-6-1
#2차항 함수식으로 변환
from sklearn.preprocessing import PolynomialFeatures
pf=PolynomialFeatures(degree=2)
x_train_poly=pf.fit_transform(x_train)
print('원본 학습 데어터셋:',x_train.shape)              #원본 학습 데어터셋: (404, 2)
print('2차 다항식 변환데이터셋:',x_train_poly.shape)    #2차 다항식 변환데이터셋: (404, 6)

lr=LinearRegression()
lr.fit(x_train_poly,y_train)

y_train_pred=lr.predict(x_train_poly)
train_mse=mean_squared_error(y_train,y_train_pred)

print("train mse: %.4f"%train_mse)                      #train mse: 21.0568

x_test_poly=pf.fit_transform(x_test)
y_test_pred=lr.predict(x_test_poly)
test_mse=mean_squared_error(y_test,y_test_pred)

print("test mse: %.4f"%test_mse)                        #test mse: 18.4338

#-> 1차항 선형 회귀 모델보다 성능이 좋아진것 확인

#15차항 다항식으로 변환
pf=PolynomialFeatures(degree=15)
x_train_poly=pf.fit_transform(x_train)

lr=LinearRegression()
lr.fit(x_train_poly,y_train)

y_train_pred=lr.predict(x_train_poly)
train_mse=mean_squared_error(y_train,y_train_pred)

print("train mse: %.4f"%train_mse)                      #train mse: 10.0201

x_test_poly=pf.fit_transform(x_test)
y_test_pred=lr.predict(x_test_poly)
test_mse=mean_squared_error(y_test,y_test_pred)

print("test mse: %.4f"%test_mse)                        #test mse: 47789459623763.1016

#-> train_mse는 10.02 로 줄어들었지만, test_mse 는 급격하게 증가 -> 과대적합상태로 신규데이터에대한 예측력 상실

#다항식 차수에따른 선형회귀모델의 LSTAT열에 대한 적합도를 산점도로 그림
plt.figure(figsize=(15,5))
for n,deg in enumerate([1,2,15]):
    ax1=plt.subplot(1,3,n+1)
    
    pf=PolynomialFeatures(degree=deg)
    x_train_poly=pf.fit_transform(x_train.loc[:,['LSTAT']])
    x_test_poly=pf.fit_transform(x_test.loc[:,['LSTAT']])
    lr=LinearRegression()
    lr.fit(x_train_poly,y_train)
    y_test_pred=lr.predict(x_test_poly)
    
    plt.scatter(x_test.loc[:,['LSTAT']],y_test,label='Targets')
    
    plt.scatter(x_test.loc[:,['LSTAT']],y_test_pred,label='predictions')
    
    plt.title("degree %d"%deg)
    
    plt.legend()
plt.show()

#5-6-2

from sklearn.linear_model import Ridge
rdg=Ridge(alpha=2.5)
rdg.fit(x_train_poly,y_train)

y_train_pred=rdg.predict(x_train_poly)
train_mse=mean_squared_error(y_train,y_train_pred)
print("train mse: %.4f"%train_mse)                       #train mse: 38.2439

y_test_pred=rdg.predict(x_test_poly)
test_mse=mean_squared_error(y_test,y_test_pred)
print('test mse: %.4f'%test_mse)                         #test mse: 31.3674


#lasso
from sklearn.linear_model import Lasso
las=Lasso(alpha=0.05)
las.fit(x_train_poly,y_train)

y_train_pred=las.predict(x_train_poly)
train_mse=mean_squared_error(y_train,y_train_pred)
print('train mse: %.4f'%train_mse)                      #train mse: 34.2005

y_test_pred=las.predict(x_test_poly)
test_mse=mean_squared_error(y_test,y_test_pred)
print('test_mse: %.4f'%test_mse)                        #test_mse: 28.4249


#elasticnet
from sklearn.linear_model import ElasticNet
ela=ElasticNet(alpha=0.01, l1_ratio=0.7)
ela.fit(x_train_poly,y_train)

y_train_pred=ela.predict(x_train_poly)
train_mse=mean_squared_error(y_train,y_train_pred)
print('train mse: %.4f'%train_mse)                      #train mse: 35.8147

y_test_pred=ela.predict(x_test_poly)
test_mse=mean_squared_error(y_test,y_test_pred)
print('test_mse: %.4f'%test_mse)                        #test_mse: 29.6416


#3.5.7 트리 기반 모델 : 비선형 회귀
#의사결정나무
from sklearn.tree import DecisionTreeRegressor
dtr=DecisionTreeRegressor(max_depth=3,random_state=12)
dtr.fit(x_train,y_train)

y_train_pred=dtr.predict(x_train)
train_mse=mean_squared_error(y_train,y_train_pred)
print('train mse : %.4f'%train_mse)                     #train mse : 17.5164

y_test_pred=dtr.predict(x_test)
test_mse=mean_squared_error(y_test,y_test_pred)
print("test mse: %.4f"%test_mse)                        #test mse : 24.3525


#랜덤포레스트

from sklearn.ensemble import RandomForestRegressor
rfr=RandomForestRegressor(max_depth=3,random_state=12)
rfr.fit(x_train,y_train)

y_train_pred=rfr.predict(x_train)
train_mse=mean_squared_error(y_train,y_train_pred)
print('train mse : %.4f'%train_mse)                     #train mse : 15.1164

y_test_pred=rfr.predict(x_test)
test_mse=mean_squared_error(y_test,y_test_pred)
print("test mse: %.4f"%test_mse)                        #test mse : 19.2789


#XGBoost

from xgboost import XGBRegressor
xgbr=XGBRegressor(objective='reg:squarederror',max_depth=3,random_state=12)
xgbr.fit(x_train,y_train)


y_train_pred=xgbr.predict(x_train)
train_mse=mean_squared_error(y_train,y_train_pred)
print('train mse : %.4f'%train_mse)                     #train mse : 3.5127

y_test_pred=xgbr.predict(x_test)
test_mse=mean_squared_error(y_test,y_test_pred)
print("test mse: %.4f"%test_mse)                        #test mse : 23.1290




