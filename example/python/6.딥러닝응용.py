# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 12:19:04 2024

@author: soyoung
"""

#6. 딥러닝 응용
#6-1 이미지분류:fashion MNIST 의류 클래스 판별

#6.1.1 데이터 전처리
import pandas as pd
import numpy as np
import tensorflow as tf
import random

seed=12
random.seed(seed)
np.random.seed(seed)
tf.random.set_seed(seed)

train=pd.read_csv(r'D:\Workspace\Python\example\python\fashion\fashion-mnist_train.csv')
test=pd.read_csv(r'D:\Workspace\Python\example\python\fashion\fashion-mnist_test.csv')

train['index']=0
for i in range(len(train)):
    train['index'][i]=i
    
print(train.shape,test.shape)

# 'index' 열을 변수로 저장
index_column = train['index']

# 'index' 열을 데이터프레임에서 삭제
train.drop(columns=['index'], inplace=True)

# 'index' 열을 원하는 위치(첫 번째 열)에 삽입
train.insert(0, 'index', index_column)

# 결과 확인
print(train.head())

train.head()

train_images=train.loc[:,'pixel1':].values.reshape(-1,28,28)
train_images.shape                                              #Out[70]: (60000, 28, 28)

import matplotlib.pyplot as plt
plt.imshow(train_images[0])                                     #첫번째 이미지 출력

y_train=train.loc[:,'label']
y_train.unique()                    #Out[74]: array([2, 9, 6, 0, 3, 4, 5, 8, 7, 1], dtype=int64)

target_values={0:'T-shirt/top',1:'Trouser',2:'Pullover',3:'Dress',4:'Coat',5:'Sandal',6:'Shirt',7:"Sneaker",8:'Bag',9:'Ankle boot'}
print(y_train[0])                                               # 2
print(target_values[y_train[0]])                                # Pullover

test_images=test.loc[:,'pixel1':].values.reshape(-1,28,28)
test_images.shape                                               #Out[80]: (10000, 28, 28)


    #500번째 test이미지 출력
plt.imshow(test_images[499])

    #피처 스케일 맞추기(정규화)
x_train=train_images/255
x_test=test_images/255

print("최소값:",x_train[0].min())
print("최대값:",x_train[0].max())

    #채널 차원 추가
print("변환 전:",x_train.shape,x_test.shape)            #변환전: (60000, 28, 28) (10000, 28, 28)
x_train=np.expand_dims(x_train,axis=-1)
x_test=np.expand_dims(x_test,axis=-1)
print("변환 후:",x_train.shape,x_test.shape)            #변환 후: (60000, 28, 28, 1) (10000, 28, 28, 1)


#6.1.2 폴드아웃 교차 검증을 위한 데이터셋 분할
    #train-validation 데이터 구분
from sklearn.model_selection import train_test_split
x_tr,x_val,y_tr,y_val=train_test_split(x_train,y_train,test_size=0.2,stratify=y_train,shuffle=True,random_state=seed)

print("학습 데이터셋 크기:",x_tr.shape,y_tr.shape)      #학습 데이터셋 크기: (48000, 28, 28, 1) (48000,)  
print("검증 데이터셋 크기:",x_val.shape,y_val.shape)    #검증 데이터셋 크기: (12000, 28, 28, 1) (12000,)


#6.1.3 MLP 모델 학습

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten, Dense

mlp_model=Sequential()
mlp_model.add(Flatten(input_shape=[28,28]))
mlp_model.add(Dense(units=64,activation='relu'))
mlp_model.add(Dense(units=10,activation='softmax'))

mlp_model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['acc'])

mlp_model.summary()

mlp_history=mlp_model.fit(x_tr,y_tr,batch_size=64,epochs=20,validation_data=(x_val,y_val),verbose=2)

    #손실 함수 그래프
def plot_loss_curve(history,total_epoch=10,start=1):
    plt.figure(figsize=(5,5))
    plt.plot(range(start,total_epoch+1),history.history['loss'][start-1:total_epoch],label='Train')
    
    plt.plot(range(start,total_epoch+1),history.history['val_loss'][start-1:total_epoch],label='Validation')
    plt.xlabel('epochs')
    plt.ylabel("loss")
    plt.legend()
    plt.show()

plot_loss_curve(history=mlp_history,total_epoch=20,start=1)


#6.1.4 합성곱 신경망(CNN)
from tensorflow.keras.layers import Conv2D, MaxPooling2D

cnn_model=Sequential()
cnn_model.add(Conv2D(filters=16,kernel_size=(3,3),activation='relu',input_shape=[28,28,1]))

cnn_model.add(MaxPooling2D(pool_size=(2,2)))
cnn_model.add(Flatten())
cnn_model.add(Dense(units=64,activation='relu'))
cnn_model.add(Dense(units=10,activation='softmax'))

cnn_model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['acc'])

cnn_model.summary()

cnn_history=cnn_model.fit(x_tr,y_tr,batch_size=64,epochs=20,validation_data=(x_val,y_val),verbose=2)

plot_loss_curve(history=cnn_history,total_epoch=20,start=1)



#6.1.5 과대적합 방지
from tensorflow.keras.layers import Dropout

def build_cnn():
    model=Sequential()
    model.add(Conv2D(filters=16,kernel_size=(3,3),activation='relu',input_shape=[28,28,1]))
    model.add(MaxPooling2D(pool_size=(2,2)))
    model.add(Flatten())
    model.add(Dense(units=64,activation='relu'))
    model.add(Dropout(rate=0.5))
    model.add(Dense(units=10,activation='softmax'))
    
    model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['acc'])
    
    return model

cnn_model=build_cnn()
cnn_model.summary()

from tensorflow.keras.callbacks import EarlyStopping

early_stopping=EarlyStopping(monitor='val_loss',patience=10)

cnn_history=cnn_model.fit(x_tr,y_tr,batch_size=64,epochs=100,validation_data=(x_val,y_val),callbacks=[early_stopping],verbose=0)

    #20 epoch까지 손실함수와 정확도를 그래프로 나타내기
start=1
end=20
fig,axes=plt.subplots(1,2,figsize=(10,5))
axes[0].plot(range(start,end+1),cnn_history.history['loss'][start-1:end],label='Train')
axes[0].plot(range(start,end+1),cnn_history.history['val_loss'][start-1:end],label='validataion')
axes[0].set_title('loss')
axes[0].legend()

axes[1].plot(range(start,end+1),cnn_history.history['acc'][start-1:end],label='Train')
axes[1].plot(range(start,end+1),cnn_history.history['val_acc'][start-1:end],label='validataion')
axes[1].set_title('accuracy')
axes[1].legend()

plt.show()

#-> 과대적합 상당히 해소된것 확인 가능

cnn_model.evaluate(x_val,y_val)                 #Out[48]: [0.2859656810760498, 0.9075000286102295]
#-> 손실함수인 mse는 0.29  보조평가지표인 정확도는 0.91로 확인 가능

y_pred_proba=cnn_model.predict(x_test)
y_pred_classes=np.argmax(y_pred_proba,axis=1)
y_pred_classes[:10]

import csv

# CSV 파일에 저장할 데이터
data = [
    ['index', 'label'],
    [0,0]
]

file_path = r'D:\Workspace\Python\example\python\fashion\submission.csv'


# 데이터프레임의 길이를 원하는 길이로 조절 (예: 10개로)
desired_length = 10000
submission = submission[:desired_length]

while len(submission) < desired_length:
    submission = pd.concat([submission, submission], ignore_index=True)
    
submission = submission[:desired_length]

submission.to_csv(file_path, index=False)

submission = pd.read_csv(file_path)


submission=pd.read_csv(r'D:\Workspace\Python\example\python\fashion\submission.csv')



submission['label']=y_pred_classes
submisiion_filpath=(r'D:\Workspace\Python\example\python\fashion\mnist_cnn_submission1.csv')
submission.to_csv(submisiion_filpath,index=False)


#6.1.6 사용자 정의 콜백 함수
from tensorflow.keras.callbacks import Callback

class my_callback(Callback):
    def on_epoch_end(self,epoch,logs={}):
        if(logs.get('val_acc')>0.91):
            self.model.stop_training=True
            print("\n목표정확도 달성:검증정확도 %.4f"%logs.get('val_acc'))
    
my_callback=my_callback()

    #best model 저장
from tensorflow.keras.callbacks import ModelCheckpoint

best_model_path=(r'D:\Workspace\Python\example\python\fashion\best_cnn_model.keras')
save_best_model=ModelCheckpoint(best_model_path,monitor='val_loss',save_best_only=True,save_weights_only=False)

    #cnn모델학습
cnn_model=build_cnn()
cnn_history=cnn_model.fit(x_tr,y_tr,batch_size=64,epochs=100,validation_data=(x_val,y_val),callbacks=[my_callback,save_best_model],verbose=2)


from tensorflow.keras.models import load_model

    #modelcheckpoint 에 저장해둔 모델 로딩
best_model=load_model(r'D:\Workspace\Python\example\python\fashion\best_cnn_model.keras')
best_model.summary()

y_pred_proba=best_model.predict(x_test)
y_pred_classes=np.argmax(y_pred_proba,axis=-1)
submission['label']=y_pred_classes
submission_filepath=(r'D:\Workspace\Python\example\python\fashion\mnist_cnn_submission2.csv')
submission.to_csv(submission_filepath,index=False)
