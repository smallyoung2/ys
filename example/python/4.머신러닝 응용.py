# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 12:39:08 2024

@author: soyoung
"""
#4.2 데이터 탐색
#4.2.1 데이터 로딩

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

train=pd.read_csv(r'D:\Workspace\Python\example\python\titanic\train.csv')
test=pd.read_csv(r'D:\Workspace\Python\example\python\titanic\test.csv')
submission=pd.read_csv(r'D:\Workspace\Python\example\python\titanic\gender_submission.csv')

print(train.shape,test.shape,submission.shape)              #(891, 12) (418, 11)  (418, 2)

train.head(3)
test.head(3)
submission.head()

#4.2.2 데이터 구조
train.info()
train.describe(include='all')

#4.2.3 결측값 확인
import missingno as msno

msno.bar(test,figsize=(10,5),color=(0.7,0.2,0.2))
plt.show()

msno.matrix(test,figsize=(10,5),color=(0.7,0.2,0.2))
plt.show()

#4.2.4 상관관계 분석
train=train.drop(columns=['Name','Sex','Ticket','Cabin','Embarked'])

plt.figure(figsize=(8,8))
sns.set(font_scale=0.8)
sns.heatmap(train.corr(), annot=True,cbar=True)
plt.show()

train=pd.read_csv(r'D:\Workspace\Python\example\python\titanic\train.csv')

#4.3 베이스라인 모델
#4.3.1 데이터 결합
train['TrainSplit']='Train'
test['TrainSplit']='Test'
data=pd.concat([train,test],axis=0)
print(data.shape)                                          #(1309, 13)  -> 891+418 인덱스0,1,...891,0,1,2,...418

#4.3.2 데이터 전처리
data_num=data.loc[:,['Pclass','Age','SibSp','Parch','Fare','Survived']]

data_num['Age']=data_num['Age'].fillna(data_num['Age'].mean())              #평균으로 결측값 대체
data_num['Fare']=data_num['Fare'].fillna(data_num['Fare'].mode()[0])        #최빈값으로 결측값 대체

selected_features=['Pclass','Age','SibSp','Parch','Fare']

x_train=data_num.loc[data['TrainSplit']=='Train',selected_features]
y_train=data_num.loc[data['TrainSplit']=='Train','Survived']

x_test=data_num.loc[data['TrainSplit']=='Test',selected_features]

print("train 데이터셋 크기:",x_train.shape,y_train.shape)         #train 데이터셋 크기: (891, 5) (891,)
print("test 데이터셋 크기:",x_test.shape)                         #test 데이터셋 크기: (418, 5)


#4.3.3 모델 학습 및 검증
    #훈련-검증 데이터 분할
from sklearn.model_selection import train_test_split

x_tr,x_val,y_tr,y_val=train_test_split(x_train,y_train,test_size=0.2,shuffle=True,random_state=20)


    #로지스틱 회귀 모델
from sklearn.linear_model import LogisticRegression

lr_model=LogisticRegression()
lr_model.fit(x_tr,y_tr)

y_val_pred=lr_model.predict(x_val)


    #confusion matrix (혼동행렬)
from sklearn.metrics import confusion_matrix

sns.heatmap(confusion_matrix(y_val,y_val_pred),annot=True,cbar=False,square=True)
plt.show()


    #평가지표
from sklearn.metrics import accuracy_score,precision_score,recall_score
from sklearn.metrics import f1_score,roc_auc_score

print("accuracy:%.4f"%accuracy_score(y_val,y_val_pred))             #accuracy:0.7207        정확도
print("precision:%.4f"%precision_score(y_val,y_val_pred))           #precision:0.6889       정밀도
print("recall:%.4f"%recall_score(y_val,y_val_pred))                 #recall:0.4627          재현율
print("f1:%.4f"%f1_score(y_val,y_val_pred))                         #f1:0.5536              f1 지표
print("auc:%.4f"%roc_auc_score(y_val,y_val_pred))                   #auc:0.6688             area under curve



#4.3.4 모델예측

    #test데이터에 대한 예측값 정리
y_test_pred=lr_model.predict(x_test)

    #제출 양식에 맞게 정리
submission['Survived']=y_test_pred.astype(int)

    #제출파일 저장
submission.to_csv(r'D:\Workspace\Python\example\python\titanic\baseline_num_lr_submission_001.csv')
submission.head(5)

#4.3.5 데이콘 리더보드 점수확인



#4.4 피처 엔지니어링(+EDA)

#4.4.1 Survived :생존 여부
train['Survived'].value_counts(dropna=False)

sns.countplot(x='Survived',data=data[data['TrainSplit']=='Train'])
plt.show()

#4.4.2 Pclass :객실 등급
train['Pclass'].value_counts(dropna=False)

sns.countplot(x='Pclass',hue='TrainSplit',data=data)
plt.show()

sns.countplot(x='Pclass',hue='Survived',data=data[data['TrainSplit']=='Train'])
plt.show()

sns.barplot(x='Pclass',y='Fare',hue='Survived',data=data[data['TrainSplit']=='Train'],estimator=np.median)
plt.show()

#4.4.3 Sex :성별
train['Sex'].value_counts(dropna=False)

sns.histplot(x='Sex',hue='Survived',multiple='dodge',data=data[data['TrainSplit']=='Train'])
plt.show()

sns.histplot(x='Sex',hue='Survived',multiple='stack',data=data[data['TrainSplit']=='Train'])
plt.show()

sns.histplot(x='Sex',hue='Survived',multiple='fill',data=data[data['TrainSplit']=='Train'])
plt.show()

    #레이블 인코딩(female:0, male:1)
data.loc[data['Sex']=='female','Sex']=0
data.loc[data['Sex']=='male','Sex']=1
data['Sex']=data['Sex'].astype(int)

data['Sex'].value_counts(dropna=False)

#4.4.4 Name : 이름
data['Name'].unique()

title_name=data['Name'].str.split(", ",expand=True)[1]
title_name

title=title_name.str.split(".",expand=True)[0]
title.value_counts(dropna=False)

title=title.replace(['Ms'],'Miss')
title=title.replace(['Mlle','the Countess','Lady','Don','Dona','Mme','Sir','Jonkheer'],'Noble')
title=title.replace(['Col','Major','Capt'],'Officer')
title=title.replace(['Dr','Rev'],'Priest')

data['Title']=np.array(title)
data['Title'].value_counts(dropna=False)

sns.violinplot(x='Title',y='Age',hue='Survived',data=data,split=True)
plt.show()

data=data.drop('Name',axis=1)
data.columns

#4.4.5 Age : 나이
data['Age'].unique()                            #nan 존재

for title in data['Title'].unique():
    print("%s 결측값 개수:"%title,data.loc[data['Title']==title,'Age'].isnull().sum())
    
    age_med=data.loc[data['Title']==title,'Age'].median()
    data.loc[data['Title']==title,'Age']=data.loc[data['Title']==title,'Age'].fillna(age_med)
    
print("\nAge열의 값의 결측값 개수:",data['Age'].isnull().sum())

sns.displot(x='Age',kind='hist',hue='Survived',data=data[data['TrainSplit']=='Train'])
plt.show()

bins=[0,4,8,12,16,32,36,48,56,67,100]
labels=['Infant','Child1','Child2','Youth1','Youth2','Adult1','Adult2','Middle Aged','Senior','Elderly']

data['AgeBin']=pd.cut(data['Age'],bins=bins,labels=labels)

sns.countplot(x='AgeBin',hue='Survived',data=data[data['TrainSplit']=='Train'])
plt.xticks(rotation=45)
plt.show()

#4.4.6 SibSp :형제자매/배우자

sns.boxplot(x='SibSp',y='Age',hue='Survived',data=data[data['TrainSplit']=='Train'])
plt.show()


#4.4.7 Parch :부모/자식

sns.boxplot(x='Parch',y='Age',hue='Survived',data=data[data['TrainSplit']=='Train'])
plt.show()

data['FamilySize']=data['SibSp']+data['Parch']+1        #가족구성원수=형제자매,배우자+부모,자식+본인(1)
 
sns.barplot(x='FamilySize',y='Survived',hue='Pclass',estimator=np.mean,data=data[data['TrainSplit']=='Train'])

#4.4.8 Fare : 요금
data.loc[data['Fare'].isnull(),:]

p3_fare_mean=data.loc[data['Pclass']==3,'Fare'].mean()
print(p3_fare_mean)

data['Fare']=data['Fare'].fillna(p3_fare_mean)
data.loc[data['PassengerId']==1044,:'Fare']

sns.displot(x='Fare',kind='kde',hue='Survived',data=data[data['TrainSplit']=='Train'])
plt.show()

data['FareLog']=np.log1p(data['Fare'])

sns.displot(x='FareLog',kind='hist',hue='Survived',data=data[data['TrainSplit']=='Train'])

sns.stripplot(x='Pclass',y='FareLog',hue='Survived',data=data[data['TrainSplit']=='Train'])

#4.4.9 Embarked :탑승항구
data.loc[data['Embarked'].isnull(),:]

print("embarked 열의 최빈값:",data['Embarked'].mode()[0])
data['Embarked']=data['Embarked'].fillna(data['Embarked'].mode()[0])
data['Embarked'].value_counts(dropna=False)

sns.catplot(x='Embarked',y='Survived',kind='point',data=data[data['TrainSplit']=='Train'])
plt.show()

#4.4.10 Cabin : 객실구역
data['Cabin'].unique()

data['Cabin'].str.slice(0,1).value_counts(dropna=False)

data['Cabin']=data['Cabin'].str.slice(0,1)
data['Cabin']=data['Cabin'].fillna('U')

sns.catplot(x='Cabin',y='Survived',kind='bar',data=data[data['TrainSplit']=='Train'])
plt.show()


#4.4.11 Ticket: 탑승권
data['Ticket'].value_counts(dropna=False)

data['Ticket']=data['Ticket'].str.replace(".","").str.replace("/","")
data['Ticket']=data['Ticket'].str.strip().str.split(' ').str[0]
data['Ticket'].value_counts(dropna=False)

data.loc[data['Ticket'].str.isdigit(),'Ticket']='NUM'
data['Ticket'].value_counts(dropna=False)[:10]

sns.catplot(x='Ticket',y='Survived',kind='bar',data=data[data['TrainSplit']=='Train'])
plt.xticks(rotation=90)
plt.show()



#4.5 데이터 전처리
#4.5.1 레이블 인코딩
from sklearn.preprocessing import LabelEncoder
for col in ['Title','AgeBin']:
    encoder=LabelEncoder()
    data[col]=encoder.fit_transform(data[col])

data.loc[:,['Title','AgeBin']].head()



#4.5.2 원핫 인코딩
onehot_prefix=[]

for col in ['Embarked','Cabin','Ticket']:
    data[col]=data[col].astype('category')
    data=pd.get_dummies(data,columns=[col],prefix=col[:3],drop_first=True)
    onehot_prefix.append(col[:3])

data.loc[:,[col for col in data.columns if col[:3] in onehot_prefix]].head()


#4.5.3 피처스케일링
from sklearn.preprocessing import MinMaxScaler
scaler=MinMaxScaler()

scaled_cols=[col for col in data.loc[:,'Pclass':].columns if col!='TrainSplit']

data_scaled=data.loc[:,scaled_cols]
data_scaled=scaler.fit_transform(data_scaled)

data.loc[:,scaled_cols]=data_scaled[:,:]
data.head()


#4.6 모델 학습
#4.6.1 피처 선택

data.columns
# 'PassengerId', 'Survived','Age','Fare','TrainSplit' 열 제외

selected_features=['Pclass', 'Sex', 'SibSp', 'Parch',\
         'Title', 'AgeBin', 'FamilySize', 'FareLog',\
       'Emb_Q', 'Emb_S', 'Cab_B', 'Cab_C', 'Cab_D', 'Cab_E', 'Cab_F', 'Cab_G',\
       'Cab_T', 'Cab_U', 'Tic_A4', 'Tic_A5', 'Tic_AQ3', 'Tic_AQ4', 'Tic_AS',\
       'Tic_C', 'Tic_CA', 'Tic_CASOTON', 'Tic_FC', 'Tic_FCC', 'Tic_Fa',\
       'Tic_LINE', 'Tic_LP', 'Tic_NUM', 'Tic_PC', 'Tic_PP', 'Tic_PPP',\
       'Tic_SC', 'Tic_SCA3', 'Tic_SCA4', 'Tic_SCAH', 'Tic_SCOW', 'Tic_SCPARIS',\
       'Tic_SCParis', 'Tic_SOC', 'Tic_SOP', 'Tic_SOPP', 'Tic_SOTONO2',\
       'Tic_SOTONOQ', 'Tic_SP', 'Tic_STONO', 'Tic_STONO2', 'Tic_STONOQ',\
       'Tic_SWPP', 'Tic_WC', 'Tic_WEP']
    
len(selected_features)                                          #Out[427]: 54

    #학습용 데이터와 예측대상인 테스트 데이터 구분
y_train=data.loc[data['TrainSplit']=='Train','Survived']
x_train=data.loc[data['TrainSplit']=='Train',selected_features]
x_test=data.loc[data['TrainSplit']=='Test',selected_features]

print("train 데이터셋 크기:",x_train.shape,y_train.shape)       #train 데이터셋 크기: (891, 54) (891,)
print("test 데이터셋 크기:",x_test.shape)                       #test 데이터셋 크기: (418, 54)

print(len(data.loc[data['TrainSplit']=='Train']))               #891
print(len(data.loc[data['TrainSplit']=='Test']))                #418

    #훈련-검증 데이터 분할
from sklearn.model_selection import train_test_split
x_tr,x_val,y_tr,y_val=train_test_split(x_train,y_train,test_size=0.2,shuffle=True,random_state=20)

print("훈련 데이터셋 크기:",x_tr.shape,y_tr.shape)             #훈련 데이터셋 크기: (712, 54) (712,)
print("검증 데이터셋 크기:",x_val.shape,y_val.shape)           #검증 데이터셋 크기: (179, 54) (179,)

    #로지스틱 회귀모델
lr_model=LogisticRegression()
lr_model.fit(x_tr,y_tr)

y_tr_pred=lr_model.predict(x_tr)
print("훈련 accuracy:%.4f"%accuracy_score(y_tr,y_tr_pred))     #훈련 accuracy:0.7978
print("훈련 auc:%.4f"%roc_auc_score(y_tr,y_tr_pred))           #훈련 auc:0.7833

y_val_pred=lr_model.predict(x_val)
print("검증 accuracy:%.4f"%accuracy_score(y_val,y_val_pred))   #검증 accuracy:0.8268
print("검증 auc:%.4f"%roc_auc_score(y_val,y_val_pred))         #검증 auc:0.7926

#-> 훈련<검증 데이터의 점수가 높으므로 모델학습이 더 필요한 과소 적합 상태임을 확인..

    #테스트 데이터 예측 및 제출파일 저장
y_test_pred=lr_model.predict(x_test)
submission['Survived']=y_test_pred.astype(int)
submission_filepath=(r'D:\Workspace\Python\example\python\titanic\baseline_lr_submission_001.csv')
submission.to_csv(submission_filepath,index=False)

    #랜덤 포레스트
from sklearn.ensemble import RandomForestClassifier    
rf_model=RandomForestClassifier(random_state=2020)    

    #cross_val_score 함수 (5-fold 교차검증)
from sklearn.model_selection import cross_val_score
auc_scores=cross_val_score(lr_model,x_train,y_train,cv=5,scoring='roc_auc')         #5으로 교차검증(cv=5)
print("개별 fold의 auc 점수:",np.round(auc_scores,4))        #개별 fold의 auc 점수: [0.837  0.8162 0.8773 0.8531 0.871 ]
print("평균 auc 점수:",np.round(np.mean(auc_scores),4))      #평균 auc 점수: 0.8509

    #제출 파일
rf_model.fit(x_train,y_train)
y_test_pred=rf_model.predict(x_test)
submission['Survived']=y_test_pred.astype(int)
submission_filepath=(r'D:\Workspace\Python\example\python\titanic\baseline_rf_submission_001.csv')
submission.to_csv(submission_filepath,index=False)


#4.6.2 피처 중요도
    #tree 계열 알고리즘의 feature importance 그래프
    
def plot_importance(model,features):
    importances=model.feature_importances_
    indices=np.argsort(importances)
    feature_names=[features[i] for i in indices]
    feature_imp=importances[indices]
    
    plt.figure(figsize=(10,12))
    plt.title("feature importances")
    plt.barh(range(len(indices)),feature_imp,align='center')
    plt.yticks(range(len(indices)),feature_names)
    plt.xlabel("relative importancd")
    
    print("피처:",list(reversed(feature_names)))
    print("중요도:",list(reversed(feature_imp)))
    
    return list(reversed(feature_names)),list(reversed(feature_imp))

imp_features,imp_scores=plot_importance(rf_model,selected_features)


    #상위 10개 피처만 선택
selected_features=imp_features[:10]
print(selected_features)
y_train=data.loc[data['TrainSplit']=='Train','Survived']
x_train=data.loc[data['TrainSplit']=='Train',selected_features]
x_test=data.loc[data['TrainSplit']=='Test',selected_features]

print("train 데이터셋 크기:",x_train.shape,y_train.shape)     #train 데이터셋 크기: (891, 10) (891,)
print("test 데이터셋 크기:",x_test.shape)                     #test 데이터셋 크기: (418, 10)

    #랜덤 포레스트
rf_model=RandomForestClassifier(random_state=2020)
auc_scores=cross_val_score(rf_model,x_train,y_train,cv=5,scoring='roc_auc')
print("개별 fold의 auc 점수:",np.round(auc_scores,4))        #개별 fold의 auc 점수: [0.8548 0.8035 0.9021 0.8405 0.8891]
print("평균 auc 의 점수: ",np.round(np.mean(auc_scores),4))  #평균 auc 의 점수:  0.858

rf_model.fit(x_train,y_train)
y_test_pred=rf_model.predict(x_test)
submission['Survived']=y_test_pred.astype(int)

submission_filepath=(r'D:\Workspace\Python\example\python\titanic\baseline_rf_submission_002.csv')
submission.to_csv(submission_filepath,index=False)


    #XGBoost
from xgboost import XGBClassifier
xgb_model=XGBClassifier(max_depth=3,random_state=2020)
auc_scores=cross_val_score(xgb_model,x_train,y_train,cv=3,scoring='roc_auc')

print("개별 fold 의 auc 점수:",np.round(auc_scores,4))       #개별 fold 의 auc 점수: [0.8316 0.89   0.8864]
print("평균 auc 점수: ",np.round(np.mean(auc_scores),4))     #평균 auc 점수:  0.8693

#->랜덤 포레스트의 auc점수보다 xgboost의 auc점수가 올라간것 확인 가능.. 0.858 <0.8693

xgb_model.fit(x_train,y_train)
y_test_pred=xgb_model.predict(x_test)
submission['Survived']=y_test_pred.astype(int)

submission_filepath=(r'D:\Workspace\Python\example\python\titanic\baseline_xgb_submission_001.csv')
submission.to_csv(submission_filepath,index=False)



#4.6.3 분류 확률값
    #확률값 예측
y_xgb_proba=xgb_model.predict_proba(x_test)[:, 1]
y_rf_proba=rf_model.predict_proba(x_test)[:,1]

    #앙상블 기법
y_proba=(y_xgb_proba+y_rf_proba)/2
submission['Survived']=y_proba

submission_filepath=(r'D:\Workspace\Python\example\python\titanic\baseline_proba_submission_001.csv')
submission.to_csv(submission_filepath,index=False)

#-> auc 스코어를 계산할떄 분류레이블(사망:0, 생존:1)을 사용하는 대신, 생존으로 분류할 확률값(0~1)을 사용한다.
#--> 저장된 엑셀의 survived의 값이 0또는 1이 아니라 생존으로 분류할 확률값으로 입력됨을 확인 가능.








