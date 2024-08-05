# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 14:51:11 2024

@author: soyoung
"""

import pandas as pd

## 2018~2023년 수원 전체 교통사고 현황
df = pd.read_excel(r'D:\Workspace\Python\mini\accidentInfoList_18-23.xlsx')

df.info()
"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 28460 entries, 0 to 28459
Data columns (total 30 columns):
 #   Column      Non-Null Count  Dtype         
---  ------      --------------  -----         
 0   Unnamed: 0  28460 non-null  int64         
 1   index       28460 non-null  int64         
 2   사고번호        28460 non-null  int64         
 3   사고일시        28460 non-null  datetime64[ns]
- 4   요일          28460 non-null  object        
- 5   시군구         28460 non-null  object               
 6   사고내용        28460 non-null  object        
* 7   사망자수        28460 non-null  int64         
* 8   중상자수        28460 non-null  int64         
* 9   경상자수        28460 non-null  int64         
* 10  부상신고자수      28460 non-null  int64         
 11  사고유형        28460 non-null  object        
 12  법규위반        28460 non-null  object        
- 13  노면상태        28460 non-null  object        
- 14  기상상태        28460 non-null  object        
- 15  도로형태        28460 non-null  object        
- 16  가해운전자 차종    28460 non-null  object        
- 17  가해운전자 성별    28460 non-null  object        
- 18  가해운전자 연령    28460 non-null  int64         
 19  가해운전자 상해정도  28460 non-null  object        
 20  피해운전자 차종    27614 non-null  object        
 21  피해운전자 성별    27614 non-null  object        
 22  피해운전자 연령    27614 non-null  object        
 23  피해운전자 상해정도  27614 non-null  object        
 24  연           28460 non-null  int64         
 25  월           28460 non-null  int64         
 26  일           28460 non-null  int64         
- 27  시간          28460 non-null  int64         
 28  구           28460 non-null  object        
 29  동           28460 non-null  object        
dtypes: datetime64[ns](1), int64(12), object(17)
memory usage: 6.5+ MB
"""

#%%
## 라벨인코딩
from sklearn import preprocessing

label_encoder = preprocessing.LabelEncoder()
onehot_encoder = preprocessing.OneHotEncoder()

onehot_location = label_encoder.fit_transform(df['시군구'])
onehot_weathre = label_encoder.fit_transform(df['기상상태'])
onehot_surface = label_encoder.fit_transform(df['노면상태'])
onehot_road = label_encoder.fit_transform(df['도로형태'])
onehot_car = label_encoder.fit_transform(df['가해운전자 차종'])
onehot_sex = label_encoder.fit_transform(df['가해운전자 성별'])
onehot_week = label_encoder.fit_transform(df['요일'])

df['location'] = onehot_location
df['weather'] = onehot_weathre
df['surface'] = onehot_surface
df['road'] = onehot_road
df['car'] = onehot_car
df['sex'] = onehot_sex
df['week'] = onehot_week

#%%
# 치사율(%) = 사망자수/교통사고 발생건수 x 100 

df['sum']=df['사망자수']+df['중상자수']+df['경상자수']+df['부상신고자수']

df['lethality']=df['사망자수']/df['sum']*100

print(df['sum'].unique())
"""
[ 1  4  3  2  5  6 16 11  8  7 10 12  9 13 19 24 15 20 23 21 14]  """

print(df['lethality'].unique())
"""
[  0.         100.          20.          33.33333333  50.
  25.          66.66666667  14.28571429  12.5          4.76190476      5.26315789]  
"""
#%%
from sklearn.model_selection import train_test_split

# 독립변수 선택
X = df[['location', 'weather', 'surface', 'road', 'car', 'sex', '가해운전자 연령']]

# 종속변수 :치사율
y = df['lethality']

# train data와 test data 구분(8:2)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 10)

print('훈련 데이터 : ', X_train.shape)
print('검증 데이터 : ', X_test.shape)
"""
훈련 데이터 :  (22768, 7)
검증 데이터 :  (5692, 7)
"""

#%%
## 다항회귀분석 : 복잡한 곡선 형태의 회귀선
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures         # 다항식 변환

poly = PolynomialFeatures(degree=2)                          # 2차항 적용
X_train_poly = poly.fit_transform(X_train)

print('원 데이터 : ', X_train.shape)
print('2차항 변환 데이터 : ', X_train_poly.shape)


"""
원 데이터 :  (22768, 7)
2차항 변환 데이터 :  (22768, 36)
"""

#%%
# train data를 가지고 모형 학습
pr = LinearRegression()

pr.fit(X_train_poly, y_train)

# 학습을 마친 모형에 test data 적용하여 결정계수(R-제곱) 계산
## 결정계수 값이 클수록 모형의 예측 능력이 좋다고 판단

X_test_poly = poly.fit_transform(X_test)
r_square = pr.score(X_test_poly, y_test)
print(r_square)
## -0.0008734415470224022


#%%
import matplotlib.pyplot as plt
import seaborn as sns

# 한글 폰트 설정
from matplotlib import font_manager, rc
font_path = 'C:/Windows/Fonts/malgun.ttf'
font_name = font_manager.FontProperties(fname = font_path).get_name()
rc('font', family = font_name)

## train data의 산점도와 test data의 회귀선을 그래프로 출력
y_hat_test = pr.predict(X_test_poly)

fig = plt.figure(figsize = (10,5))
ax = fig.add_subplot(1,1,1)
ax.plot(X_train, y_train, 'o', label='Train Data')
ax.plot(X_test, y_hat_test, 'r+', label='Predicted Value')
ax.legend(loc='best')
plt.xlabel('ECLO')
plt.show()

#%%
# 모형에 전체 데이터 X를 입력하여 예측한 값 y_hat을 실제 값 y와 비교

X_poly = poly.fit_transform(X)
y_hat = pr.predict(X_poly)

plt.figure(figsize=(10,5))
ax1 = sns.kdeplot(y, label = 'y')
ax2 = sns.kdeplot(y_hat, label = 'y_hat', ax=ax1)
plt.legend()
plt.show()

#%%
## 함수화(3차항)
def letha_poly(df, col_ls) :
    X = df[col_ls]    
    y = df['lethality']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 10)

    print('훈련 데이터 : ', X_train.shape)
    print('검증 데이터 : ', X_test.shape)

    poly = PolynomialFeatures(degree=3)                         # 3차항 적용
    X_train_poly = poly.fit_transform(X_train)

    print('원 데이터 : ', X_train.shape)
    print('3차항 변환 데이터 : ', X_train_poly.shape)


    pr = LinearRegression()
    
    pr.fit(X_train_poly, y_train)
    
    X_test_poly = poly.fit_transform(X_test)
    r_square = pr.score(X_test_poly, y_test)
    print("결정계수",r_square)
    
    X_poly = poly.fit_transform(X)
    y_hat = pr.predict(X_poly)
    
    plt.figure(figsize=(10,5))
    ax1 = sns.kdeplot(y, label = 'y')
    ax2 = sns.kdeplot(y_hat, label = 'y_hat', ax=ax1)
    plt.legend()
    plt.show()
    
#%%
                                                                                     
letha_poly(df, ['location', 'weather', 'surface', 'road', 'car', 'sex', '가해운전자 연령', '시간'])    
## 결정계수 -0.013069998393069548

#%%
# 노인 운전자 데이터 기준
old_df = df.loc[df['가해운전자 연령'] >= 65,:]

ml_poly(old_df, ['location', 'weather', 'road', 'car', 'sex', '가해운전자 연령', '시간', 'week'])
## 결정계수 -0.15752347508109765