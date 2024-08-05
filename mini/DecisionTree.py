# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 14:56:59 2024

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

## ECLO 계산
df['ECLO'] = df['사망자수']*10 + df['중상자수']*5 + df['경상자수']*3 + df['부상신고자수']*1

#%%
from sklearn.model_selection import train_test_split

# 독립변수 선택
X = df[['location', 'weather', 'surface', 'road', 'car', 'sex', '가해운전자 연령']]

# 종속변수 ECLO
y = df['ECLO']

# train data와 test data 구분(8:2)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 10)

print('훈련 데이터 : ', X_train.shape)
print('검증 데이터 : ', X_test.shape)
"""
훈련 데이터 :  (22768, 7)
검증 데이터 :  (5692, 7)
"""


#%%
#모형객체 생성 decision tree
from sklearn import tree

tree_model=tree.DecisionTreeClassifier(criterion='entropy',max_depth=5)

tree_model.fit(X_train,y_train)

y_hat=tree_model.predict(X_test)

print(y_hat[0:10])
print(y_test.values[0:10])
"""
[3 3 3 3 3 3 3 3 3 3]
[3 3 3 3 3 3 3 3 3 3]   """


#%%
#모델 성능평가 -cofusion matrix 계산
from sklearn import metrics

tree_matrix=metrics.confusion_matrix(y_test,y_hat)
print(tree_matrix)
"""
[[   0    0  295    0    0    0    0    0    0    0    0    0    0    0
     0    0    0    0    0    0    0    0    0    0    0    0    0    0]
 [   0    0   17    0    0    0    0    0    0    0    0    0    0    0
     0    0    0    0    0    0    0    0    0    0    0    0    0    0]
 [   0    0 2965    0    1    0    0    0    0    0    0    0    0    0
     0    0    0    0    0    0    0    0    0    0    0    0    0    0]
 [   0    0   92    0    0    0    0    0    0    0    0    0    0    0
     0    0    0    0    0    0    0    0    0    0    0    0    0    0]
 [   0    0  963    0    0    0    0    0    0    0    0    0    0    0
     0    0    0    0    0    0    0    0    0    0    0    0    0    0]
 [   0    0  640    0    1    0    0    0    0    0    0    0    0    0
     0    0    0    0    0    0    0    0    0    0    0    0    0    0]
 [   0    0   30    0    0    0    0    0    0    0    0    0    0    0
     0    0    0    0    0    0    0    0    0    0    0    0    0    0]
 [   0    0  151    0    0    0    0    0    0    0    0    0    0    0
     0    0    0    0    0    0    0    0    0    0    0    0    0    0]
 [   0    0  201    0    1    0    0    0    0    0    0    0    0    0
     0    0    0    0    0    0    0    0    0    0    0    0    0    0]
 [   0    0   60    0    0    0    0    0    0    0    0    0    0    0
     0    0    0    0    0    0    0    0    0    0    0    0    0    0]
 [   0    0   46    0    0    0    0    0    0    0    0    0    0    0
     0    0    0    0    0    0    0    0    0    0    0    0    0    0]
 [   0    0   84    0    0    0    0    0    0    0    0    0    0    0
     0    0    0    0    0    0    0    0    0    0    0    0    0    0]
 [   0    0   26    0    0    0    0    0    0    0    0    0    0    0
     0    0    0    0    0    0    0    0    0    0    0    0    0    0]
 [   0    0   19    0    0    0    0    0    0    0    0    0    0    0
     0    0    0    0    0    0    0    0    0    0    0    0    0    0]
 [   0    0   38    0    0    0    0    0    0    0    0    0    0    0
     0    0    0    0    0    0    0    0    0    0    0    0    0    0]
 [   0    0   13    0    0    0    0    0    0    0    0    0    0    0
     0    0    0    0    0    0    0    0    0    0    0    0    0    0]
 [   0    0    9    0    0    0    0    0    0    0    0    0    0    0
     0    0    0    0    0    0    0    0    0    0    0    0    0    0]
 [   0    0   17    0    0    0    0    0    0    0    0    0    0    0
     0    0    0    0    0    0    0    0    0    0    0    0    0    0]
 [   0    0    2    0    0    0    0    0    0    0    0    0    0    0
     0    0    0    0    0    0    0    0    0    0    0    0    0    0]
 [   0    0    7    0    0    0    0    0    0    0    0    0    0    0
     0    0    0    0    0    0    0    0    0    0    0    0    0    0]
 [   0    0    3    0    0    0    0    0    0    0    0    0    0    0
     0    0    0    0    0    0    0    0    0    0    0    0    0    0]
 [   0    0    2    0    0    0    0    0    0    0    0    0    0    0
     0    0    0    0    0    0    0    0    0    0    0    0    0    0]
 [   0    0    1    0    0    0    0    0    0    0    0    0    0    0
     0    0    0    0    0    0    0    0    0    0    0    0    0    0]
 [   0    0    3    0    0    0    0    0    0    0    0    0    0    0
     0    0    0    0    0    0    0    0    0    0    0    0    0    0]
 [   0    0    2    0    0    0    0    0    0    0    0    0    0    0
     0    0    0    0    0    0    0    0    0    0    0    0    0    0]
 [   0    0    1    0    0    0    0    0    0    0    0    0    0    0
     0    0    0    0    0    0    0    0    0    0    0    0    0    0]
 [   0    0    1    0    0    0    0    0    0    0    0    0    0    0
     0    0    0    0    0    0    0    0    0    0    0    0    0    0]
 [   0    0    1    0    0    0    0    0    0    0    0    0    0    0
     0    0    0    0    0    0    0    0    0    0    0    0    0    0]]   """

# 모델 성능평가- 평가 지표계산 
tree_report=metrics.classification_report(y_test,y_hat)
print(tree_report)
"""
              precision    recall  f1-score   support

           1       0.00      0.00      0.00       295
           2       0.00      0.00      0.00        17
           3       0.52      1.00      0.69      2966
           4       0.00      0.00      0.00        92
           5       0.00      0.00      0.00       963
           6       0.00      0.00      0.00       641
           7       0.00      0.00      0.00        30
           8       0.00      0.00      0.00       151
           9       0.00      0.00      0.00       202
          10       0.00      0.00      0.00        60
          11       0.00      0.00      0.00        46
          12       0.00      0.00      0.00        84
          13       0.00      0.00      0.00        26
          14       0.00      0.00      0.00        19
          15       0.00      0.00      0.00        38
          16       0.00      0.00      0.00        13
          17       0.00      0.00      0.00         9
          18       0.00      0.00      0.00        17
          19       0.00      0.00      0.00         2
          20       0.00      0.00      0.00         7
          21       0.00      0.00      0.00         3
          23       0.00      0.00      0.00         2
          27       0.00      0.00      0.00         1
          28       0.00      0.00      0.00         3
          29       0.00      0.00      0.00         2
          30       0.00      0.00      0.00         1
          35       0.00      0.00      0.00         1
          70       0.00      0.00      0.00         1

    accuracy                           0.52      5692
   macro avg       0.02      0.04      0.02      5692
weighted avg       0.27      0.52      0.36      5692  """

