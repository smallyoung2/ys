# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 12:10:43 2024

@author: soyoung
"""

#5.딥러닝 입문

#5-1 인공신경망의 구조

#5-2 간단한 딥러닝 모델 만들기

#Sequential API

import tensorflow as tf
print(tf.__version__)

import pandas as pd
import numpy as np

x=[-3,31,-11,4,0,22,-2,-5,-25,-14]
y=[-2,32,-10,5,1,23,-1,-4,-24,-13]

x_train=np.array(x).reshape(-1,1)
y_train=np.array(y)

print(x_train.shape,y_train.shape)

from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense

model=Sequential()
model.add(Dense(units=1, activation='linear',input_dim=1))          #선형회귀모델

model.summary()

#모델 컴파일
model.compile(optimizer='adam',loss='mse',metrics=['mae'])

#모델 학습 및 예측
model.fit(x_train,y_train,epochs=3000,verbose=0)

model.weights


x_input = np.array([[11], [12], [13]])
predictions = model.predict(x_input)

print(predictions)


#5-3 딥러닝을 활용한 회귀분석: 보스턴 주택가격예측

#5.3.1 데이터 전처리
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random
import tensorflow as tf
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

SEED=12
random.seed(SEED)
np.random.seed(SEED)
tf.random.set_seed(SEED)
print("시드 고정: ",SEED)

housing=df
x_data=housing.loc[:,:'LSTAT']
y_data=housing.Target

print(x_data.shape, y_data.shape)                       #(506, 13)  (506, )


from sklearn.preprocessing import MinMaxScaler

scaler=MinMaxScaler()
x_data_scaled=scaler.fit_transform(x_data)
x_data_scaled[0]

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x_data,y_data,test_size=0.2,shuffle=True,random_state=SEED)
print(x_train.shape, y_train.shape)                    #(404, 13) (404,)
print(x_test.shape, y_test.shape)                      #(102, 13) (102,)


#5.3.2 MLP모델 아키텍처 정의

#심층신경망

#완전연결(dense)레이어만 사용하여 5개 레이어(128,64,32,16,1)를 갖는 다층신경망 만들기(MLP)

from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense

def build_model(num_input=1):
        #입력층
    model=Sequential()
    
        #은닉층
    model.add(Dense(128,activation='relu',input_dim=num_input))
    model.add(Dense(64,activation='relu'))
    model.add(Dense(32,activation='relu'))
    model.add(Dense(16,activation='relu'))
    
        #출력층
    model.add(Dense(1,activation='linear'))
    
        #옵티마이저, 손실함수, 측정지표 등을 지정
    model.compile(optimizer='adam',loss='mse',metrics=['mae'])
    
    return model

model=build_model(num_input=13)
model.summary()                             # Total params: 12,673 (49.50 KB)

#5.3.3 미니배치학습

model.fit(x_train,y_train,epochs=100,batch_size=12,verbose=2)

model.evaluate(x_test,y_test)               #Out[12]: [25.515363693237305, 3.447108745574951]


#-> 검증손실:25.51, 훈련손실: 3.44  검증>훈련 :과대적합으로 판단됨


#5.3.4 교차검증

model=build_model(num_input=13)
history=model.fit(x_train,y_train,batch_size=32,epochs=200,validation_split=0.25,verbose=2)

import matplotlib.pyplot as plt
def plot_loss_curve(total_epoch=10,start=1):
    
    plt.figure(figsize=(5,5))
    plt.plot(range(start,total_epoch+1),history.history['loss'][start-1:total_epoch],label='Train')
    
    plt.plot(range(start,total_epoch+1),history.history['val_loss'][start-1:total_epoch],label='Validation')
    
    plt.xlabel('Epochs')
    plt.ylabel('mse')
    plt.legend()
    plt.show()
    
plot_loss_curve(total_epoch=200,start=1)

plot_loss_curve(total_epoch=200,start=20)


#5-4 딥러닝을 활용한 분류예측 : 와인 품질 등급 판별

#5.4.1 데이터 전처리

#와인데이터

import pandas as pd
import numpy as np
import random
import tensorflow as tf

SEED=12
random.seed(SEED)
np.random.seed(SEED)
tf.random.set_seed(SEED)
print("시드고정:",SEED)

train=pd.read_csv(r'D:\Workspace\Python\example\python\wine\train.csv')
test=pd.read_csv(r'D:\Workspace\Python\example\python\wine\test.csv')
submission=pd.read_csv(r'D:\Workspace\Python\example\python\wine\sample_submission.csv')

print(train.shape, test.shape, submission.shape)            # (5497, 14) (1000, 13) (1000, 2)

train.head(2)
train.info()
submission.head()

train['type'].value_counts()
"""
type
white    4159
red      1338
Name: count, dtype: int64 """


train['type']=np.where(train['type']=='white',1,0).astype(int)  #white이면 1,red이면 0
test['type']=np.where(test['type']=='white',1,0).astype(int)

train['type'].value_counts()
"""
type
1    4159
0    1338
Name: count, dtype: int64 """

train['quality'].value_counts()                                 #와인 등급 
"""
quality
6    2416
5    1788
7     924
4     186
8     152
3      26
9       5
Name: count, dtype: int64 """




from tensorflow.keras.utils import to_categorical

y_train=to_categorical(train.loc[:,'quality']-3)        #등급이 3~9 로 이루어져있으므로 -3
y_train


x_train=train.loc[:,'fixed acidity':]                   #index, quality 열 제외한 나머지 열
x_test=test.loc[:,'fixed acidity':]


from sklearn.preprocessing import MinMaxScaler

scaler=MinMaxScaler()
scaler.fit(x_train)

x_train_scaled=scaler.fit_transform(x_train)
x_test_scaled=scaler.fit_transform(x_test)

print(x_train_scaled.shape,y_train.shape)   #(5497, 12) (5497, 7) 전체 14개행-index,quality=12, 와인등급 7개
print(x_test_scaled.shape)                  #(1000, 12)


#5.4.2 모델설계: 드랍아웃 활용

from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense,Dropout


def build_model(train_data,train_target):
    
    #입력층
    model=Sequential()
    
    #은닉층
    model.add(Dense(128,activation='tanh', input_dim=train_data.shape[1]))
    model.add(Dropout(0.2))
    model.add(Dense(64,activation='tanh'))
    model.add(Dropout(0.2))
    model.add(Dense(32,activation='tanh'))
    
    #출력층
    model.add(Dense(train_target.shape[1],activation='softmax'))
    
    #옵티마이저, 손실함수
    model.compile(optimizer='RMSProp',loss='categorical_crossentropy',metrics=['acc','mae'])
    
    return model

model=build_model(x_train_scaled,y_train)
model.summary()


#5.4.3 콜백함수: Early Stopping 기법

from sklearn.model_selection import train_test_split
from tensorflow.keras.callbacks import EarlyStopping

x_tr,x_val,y_tr,y_val=train_test_split(x_train_scaled,y_train,test_size=0.15,shuffle=True,random_state=SEED)

early_stopping=EarlyStopping(monitor='val_loss',patience=10)
history=model.fit(x_tr,y_tr,batch_size=64,epochs=200,validation_data=(x_val,y_val),callbacks=[early_stopping],verbose=2)

model.evaluate(x_val,y_val)                     #54에포크가 종료된 상태에서의 평가지표값과 동일
#  26/26 ━━━━━━━━━━━━━━━━━━━━ 0s 625us/step - acc: 0.5508 - loss: 1.0619 - mae: 0.1632
#  Out[57]: [1.0205198526382446, 0.5696969628334045, 0.1598848849534988      #[ val_loss, val_acc, val_mae ]


#5.4.4 예측값 정리 및 파일 제출

y_pred_proba=model.predict(x_test)
y_pred_proba[:5]

y_pred_label=np.argmax(y_pred_proba,axis=-1)+3
y_pred_label[:5]

submission['quality']=y_pred_label.astype(int)
submission.head()

submission.to_csv(r'D:\Workspace\Python\example\python\wine\wine_dnn_001.csv',index=False)
