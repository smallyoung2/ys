# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 14:16:42 2024

@author: soyoung
"""

#1. 판다스 자료구조
import pandas as pd
print(pd.__version__)
data1=['a','b','c','d','e']
print(data1)
type(data1)                     #Out[5]: list

sr1=pd.Series(data1)
type(sr1)                       #Out[7]: pandas.core.series.Series
print(sr1)
sr1.loc[0]
sr1.loc[1:3]

data2=[1,2,3.14,100,-10]
sr2=pd.Series(data2)
print(sr2)

dict_data={'c0':sr1,'c1':sr2}   #시리즈를 여러개 결합하면 데이터프레임 생성가능
df1=pd.DataFrame(dict_data)
df1
type(df1)                       #Out[18]: pandas.core.frame.DataFrame
df1.columns                     #Out[20]: Index(['c0', 'c1'], dtype='object')

df1.columns=['string','number']              #열이름 바꾸기
df1
df1.index                       #Out[24]: RangeIndex(start=0, stop=5, step=1)
df1.index=['r0','r1','r2','r3','r4']         #인덱스 이름 바꾸기
df1

df1.loc['r2','number']
df1.loc['r2':'r3','string':'number']
df1.loc['r2':'r3','number']
df1.loc['r2','string':'number']
df1.loc[:,'string']
df1.loc['r2':'r3',:]

#2. 머신러닝

#3. 일차함수 관계식 찾기

#3.1 문제파악
x=[-3,31,-11,4,0,22,-2,-5,-25,-14]
y=[-2,32,-10,5,1,23,-1,-4,-24,-13]

#3.2 데이터 탐색
import matplotlib.pyplot as plt
plt.plot(x,y)
plt.show()

#3.3 데이터 전처리
import pandas as pd
df=pd.DataFrame({'x':x,'y':y})
df.head()
df.tail()
df.shape                        #Out[43]: (10, 2) ->10행2열의 구조

train_features=['x']
target_cols=['y']
x_train=df.loc[:,train_features]        #x열의 데이터 x_train에 저장
y_train=df.loc[:,target_cols]           #y열의 데이터 y_train에 저장
print(x_train.shape,y_train.shape)      #(10, 1) (10, 1) ->각각 10행 1열 구조

#3.4 모델학습
from sklearn.linear_model import LinearRegression
lr=LinearRegression()
lr.fit(x_train,y_train)                 #Out[56]: LinearRegression()
lr.coef_,lr.intercept_                  #Out[57]: (array([[1.]]), array([1.])) -> y=1x+b 형태
print("기울기:",lr.coef_[0][0])         #기울기: 0.9999999999999999
print("y절편:",lr.intercept_[0])        #y절편: 0.9999999999999999

#3.5 예측
import numpy as np
x_new=np.array(11).reshape(1,1)
lr.predict(x_new)                       #Out[62]: array([[12.]])

x_test=np.arange(11,16,1).reshape(-1,1) #11~15까지  step 1  ->  11,12,13,14,15
x_test
"""
Out[69]: 
array([[11],
       [12],
       [13],
       [14],
       [15]]) """
y_pred=lr.predict(x_test)               #예측 값 y=1x+1이므로-> 12,13,14,15,16
y_pred
"""
Out[71]: 
array([[12.],
       [13.],
       [14.],
       [15.],
       [16.]]) """


#4. 분류(classfication)-붓꽃의 품종 판별

#4.1 데이터 로딩
import pandas as pd
import numpy as np

from sklearn import datasets
iris=datasets.load_iris()
iris.keys()    
#Out[6]: dict_keys(['data','target','frame','target_names','DESCR','feature_names','filename','data_module'])
print(iris['DESCR'])            #descr 키를 이용하여 데이터셋 설명 출력

#4.1.1 target 속성
print("데이터셋 크기:",iris['target'].shape)      #데이터셋 크기: (150,)
print("데이터셋 내용:",iris['target'])
#4.1.2 data속성
print("데이터셋 크기:",iris['data'].shape)        #데이터셋 크기: (150, 4)
print("데이터셋 내용:\n",iris['data'][:7,:])      #꽃받침길이,꽃받침폭,꽃잎길이,꽃잎폭
#4.1.3 데이터프레임변환
df=pd.DataFrame(iris['data'],columns=iris['feature_names'])  #행이름 설정
print("데이터 프레임의 형태:",df.shape)          #데이터 프레임의 형태: (150, 4)
df.head()

df.columns=['sepal_length','sepla_width','petal_length','petal_width']  #행이름 간결하게 변경
df.head()

df['target']=iris['target']                      #데이터 프레임에 아이리스의 target속성 추가
print("데이터셋의 크기:",df.shape)               #데이터셋의 크기: (150, 5)
df.head()
df.tail()

#4.2 데이터 탐색

#4.2.1 데이터셋의 기본정보
df.info()
#4.2.2 통계정보 요약(개수,평균,표준편차,최소값,4분위수,최대값)
df.describe()
#4.2.3 결측값 확인
df.isnull().sum()                                #결측값 없음
#4.2.4 중복데이터 확인
df.duplicated().sum()                            #Out[29]: 1  -> 중복데이터 1개 발견

df.loc[df.duplicated(),:]
df.loc[(df.sepal_length==5.8) &(df.petal_width==1.9)]   #101인덱스와 142인덱스 중복됨

df=df.drop_duplicates()                          # 중복되는 데이터 제거함
df.duplicated().sum()                            #Out[35]: 0 -> 중복되는 데이터 없음

df.info()                                        #150개 행에서 중복되는 1행 제거-> 149행이됨
#4.2.5 상관관계분석
df.corr()                                        #상관계수행렬 출력(변수간 상관관계분석)
#4.2.6 데이터 시각화
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(font_scale=1.2)                         #시본의 글씨 크기배율 1.2배로 설정

sns.heatmap(data=df.corr(),square=True, annot=True,cbar=True)   #상관계수행렬을 히트맵으로 보여줌
plt.show()

df['target'].value_counts()
"""
Out[44]: 
target
0    50
1    50
2    49
Name: count, dtype: int64 """
plt.hist(x='sepal_length',data=df)                  #sepal_length 값의 분포-hist
plt.show()
sns.displot(x='sepla_width',kind='hist',data=df)    #sepal_width 값의 분포-displot(hist)
plt.show()
sns.displot(x='petal_width',kind='kde',data=df)     #petal_width 값의 분포-displot(kde밀도함수)
plt.show()
sns.displot(x='sepal_length',hue='target',kind='kde',data=df) #target(품종)별로 sepal_length 값의 분포
plt.show()

for col in ['sepla_width','petal_length','petal_width']:
    sns.displot(x=col,hue='target',kind='kde',data=df)
    plt.show()
    
sns.pairplot(df,hue='target',size=2.5,diag_kind='kde')  #target 별로 16개 그래프 출력


#4.3 train-test 데이터셋 분할
from sklearn.model_selection import train_test_split
x_data=df.loc[:,'sepal_length':'petal_width']
y_data=df.loc[:,'target']

x_train,x_test,y_train,y_test=train_test_split(x_data,y_data,test_size=0.2,shuffle=True,random_state=20)
print(x_train.shape,y_train.shape)                  #(119, 4) (119,)
print(x_test.shape,y_test.shape)                    #(30, 4) (30,)

#4.4 분류 알고리즘 1.KNN
from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier(n_neighbors=7)
knn.fit(x_train,y_train)              #Out[68]: KNeighborsClassifier(n_neighbors=7)

y_knn_pred=knn.predict(x_test)
print("예측값:",y_knn_pred[:5])                 #예측값: [0 1 1 2 1]

from sklearn.metrics import accuracy_score
knn_acc=accuracy_score(y_test,y_knn_pred)
print("accuracy: %.4f"%knn_acc)                 #accuracy: 0.9667
#n_neighbors=3일때 accuracy: 0.9333 ,n_neighbors=10 일때 accuracy: 1.0000
#-> n_neighbors가 클수록 정확도(붓꽃 품종을 정확히 분류한 비율) 올라간다.

#4.5 분류 알고리즘 2. SVM
#RBF(방사형 기저 함수): 값이 원점,특정 지점으로부터의 거리에 따라 달라지는 실수 값 함수
from sklearn.svm import SVC
svc=SVC(kernel='rbf')
svc.fit(x_train,y_train)                        #Out[120]: SVC()

y_svc_pred=svc.predict(x_test)
print("예측값:",y_svc_pred[:5])                 #예측값: [0 1 1 2 1]

svc_acc=accuracy_score(y_test,y_svc_pred)
print("accuracy:%.4f"%svc_acc)                  #accuracy:1.0000

#4.6 분류 알고리즘 3. 로지스틱 회귀
from sklearn.linear_model import LogisticRegression
lrc=LogisticRegression()
lrc.fit(x_train,y_train)                        #Out[128]: LogisticRegression()

y_lrc_pred=lrc.predict(x_test)
print("예측값:",y_lrc_pred[:5])                 #예측값: [0 1 1 2 1]
lrc_acc=accuracy_score(y_test,y_lrc_pred)
print("accuracy:%.4f"%lrc_acc)                  #accuracy:1.0000

y_lrc_prob=lrc.predict_proba(x_test)
y_lrc_prob
"""
array([[9.83139400e-01, 1.68605422e-02, 5.74319118e-08],
       [4.60559855e-03, 8.41673551e-01, 1.53720850e-01],
       [1.03263225e-02, 9.20317332e-01, 6.93563457e-02], """
#각 열은 target의 0,1,2
#첫번째 행에서 9.83,1.68,5.74 로 0번째열의 확률이 가장 크기때문에 첫번째샘플은 0으로 분류됨

#4.7 분류 알고리즘 4.의사결정나무
from sklearn.tree import DecisionTreeClassifier
dtc=DecisionTreeClassifier(max_depth=3,random_state=20)
dtc.fit(x_train,y_train)    #Out[137]: DecisionTreeClassifier(max_depth=3, random_state=20)

y_dtc_pred=dtc.predict(x_test)
print('예측값:',y_dtc_pred[:5])                 #예측값: [0 1 1 2 1]
dtc_acc=accuracy_score(y_test,y_dtc_pred)
print("accuracy:%.4f"%dtc_acc)                  #accuracy:0.9333

#4.8 앙상블 모델 1.보팅 100%정확도 
from sklearn.ensemble import VotingClassifier
hvc=VotingClassifier(estimators=[('KNN',knn),('SVM',svc),('DT',dtc)],voting='hard')
hvc.fit(x_train,y_train)

y_hvc_pred=hvc.predict(x_test)
print("예측값:",y_hvc_pred[:5])                 #예측값: [0 1 1 2 1]
hvc_acc=accuracy_score(y_test,y_hvc_pred)
print("accuracy:%.4f"%hvc_acc)                  #accuracy:1.0000

#4.9 앙상블 모델 2.배깅
from sklearn.ensemble import RandomForestClassifier
rfc=RandomForestClassifier(n_estimators=50,max_depth=3,random_state=20)
rfc.fit(x_train,y_train)

y_rfc_pred=rfc.predict(x_test)
print("예측값:",y_rfc_pred[:5])                 #예측값: [0 1 1 2 1]
rfc_acc=accuracy_score(y_test,y_rfc_pred)
print("accuracy:%.4f"%rfc_acc)                  #accuracy:0.9667

#4.10 앙상블 모델 3. 부스팅
from xgboost import XGBClassifier
xgbc=XGBClassifier(n_estimators=50,max_depth=3,random_state=20)
xgbc.fit(x_train,y_train)

y_xgbc_pred=xgbc.predict(x_test)
print("예측값:",y_xgbc_pred[:5])                #예측값: [0 1 1 2 1]
xgbc_acc=accuracy_score(y_test,y_xgbc_pred)
print("accuracy:%.4f"%xgbc_acc)                 #accuracy:0.9333

#4.11 교차검증 1.Hold-out -> train 된 데이터 다시 나눔. 119->(83,36)
x_tr,x_val,y_tr,y_val=train_test_split(x_train,y_train,test_size=0.3,shuffle=True,random_state=20)
print(x_tr.shape,y_tr.shape)                  #(83, 4) (83,)
print(x_val.shape,y_val.shape)                #(36, 4) (36,)

rfc=RandomForestClassifier(max_depth=3,random_state=20)
rfc.fit(x_tr,y_tr)

y_tr_pred=rfc.predict(x_tr)
y_val_pred=rfc.predict(x_val)

tr_acc=accuracy_score(y_tr,y_tr_pred)
val_acc=accuracy_score(y_val,y_val_pred)
print("train accuracy:%.4f"%tr_acc)             #train accuracy:0.9880
print("validation acuuracy:%.4f"%val_acc)       #validation acuuracy:0.9167

y_test_pred=rfc.predict(x_test)
test_acc=accuracy_score(y_test,y_test_pred)
print("test accuracy:%.4f"%test_acc)            #test accuracy:0.9000

#4-12 교차검증 2. K-fold
from sklearn.model_selection import KFold
kfold=KFold(n_splits=5,shuffle=True,random_state=20)

num_fold=1
for tr_idx,val_idx in kfold.split(x_train):
    print("%s fold---------------------------------------"%num_fold)
    print("훈련:",len(tr_idx),tr_idx[:10])
    print("검증:",len(val_idx),val_idx[:10])
    num_fold+=1
    
val_scores=[]
num_fold=1
for tr_idx,val_idx in kfold.split(x_train,y_train):
    x_tr,x_val=x_train.iloc[tr_idx,:],x_train.iloc[val_idx,:]
    y_tr,y_val=y_train.iloc[tr_idx],y_train.iloc[val_idx]
    
    rfc=RandomForestClassifier(max_depth=5,random_state=20)
    rfc.fit(x_tr,y_tr)
    
    y_val_pred=rfc.predict(x_val)
    val_acc=accuracy_score(y_val,y_val_pred)
    print("%d fold accuracy:%.4f"%(num_fold,val_acc))
    val_scores.append(val_acc)
    num_fold+=1
"""
1 fold accuracy:0.8750
2 fold accuracy:1.0000
3 fold accuracy:0.9167
4 fold accuracy:0.9583
5 fold accuracy:0.9565 """
import numpy as np
mean_score=np.mean(val_scores)
print("평균 검증 accuracy:",np.round(mean_score,4))     #평균 검증 accuracy: 0.9413
