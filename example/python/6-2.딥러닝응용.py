# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 10:58:22 2024

@author: soyoung
"""

#6-2 오토인코더: 차원 축소와 이미지 복원
#6.2.1 기본개념

#6.2.2 오토인코더 모델 만들기

import pandas as pd
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import random

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten,Dense,Dropout
from tensorflow.keras.layers import Conv2D,MaxPooling2D,Reshape

seed=12
random.seed(seed)
np.random.seed(seed)
tf.random.set_seed(seed)

    #케라스에서 불러오기
from tensorflow.keras import datasets
fashion_mnist=datasets.fashion_mnist
(x_train,y_train),(x_test,y_test)=fashion_mnist.load_data()

    #피처 스케일링(정규화)  ->픽셀 값이 0~255까지존재하므로 255로 나누어서 정규화
x_train=x_train/255
x_test=x_test/255

    #차원추가  : 3차원-> 4차원으로 차원추가
x_train=np.expand_dims(x_train,axis=-1)
x_test=np.expand_dims(x_test,axis=-1)


print(x_train.shape,y_train.shape,x_test.shape,y_test.shape)    
#(60000, 28, 28, 1) (60000,) (10000, 28, 28, 1) (10000,)

    #오토 인코더 모델 정의
def Autoencoder():
    model=Sequential()
    
    model.add(Conv2D(filters=16,kernel_size=(3,3),activation='relu',input_shape=[28,28,1]))
    model.add(MaxPooling2D(pool_size=(2,2)))
    model.add(Flatten())
    model.add(Dense(64,activation='relu'))
    
    model.add(Dense(units=28*28,activation='sigmoid'))
    model.add(Reshape((28,28)))
    
    model.compile(optimizer='adam',loss='mean_squared_error')
    
    return model

ae_model=Autoencoder()
ae_model.summary()

history=ae_model.fit(x_train,x_train,batch_size=64,epochs=20,validation_data=(x_test,x_test),verbose=0)

ae_images=ae_model.predict(x_test)
ae_images.shape                                     #Out[18]: (10000, 28, 28)


num=5
plt.figure(figsize=(20,8))

for i in range(num):
    ax=plt.subplot(2,num,i+1)
    plt.imshow(x_test[i].reshape((28,28)),cmap='gray')
    plt.title("original %s "%str(i))
    
    ax=plt.subplot(2,num,i+num+1)
    plt.imshow(ae_images[i],cmap='gray')
    plt.title("auto-encoded %s"%str(i))
    plt.axis('off')
    
plt.show()


#6-3 전이학습: 사전 학습 모델 활용
#6.3.1 GPU 런타임 설정

#6.3.2 CIFAR-10 데이터셋
import pandas as pd
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import random

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten,Dense,Dropout
from tensorflow.keras.layers import Conv2D,MaxPooling2D,Reshape
from tensorflow.keras.layers import BatchNormalization

seed=12
random.seed(seed)
np.random.seed(seed)
tf.random.set_seed(seed)

    #케라스에서 불러오기
from tensorflow.keras import datasets
cifar10=datasets.cifar10

(x_train,y_train),(x_test,y_test)=cifar10.load_data()

x_train=x_train/255
x_test=x_test/255

print(x_train.shape,y_train.shape,x_test.shape,y_test.shape)
#(50000, 32, 32, 3) (50000, 1) (10000, 32, 32, 3) (10000, 1)

plt.figure(figsize=(10,8))
for i in range(20):
    plt.subplot(4,5,i+1)
    plt.imshow(x_train[i])
    plt.axis('off')
plt.show()



#6.3.3 일반 합성곱 신경망(CNN)으로 분류예측
def build_cnn():
    model=Sequential()
    model.add(Conv2D(filters=32,kernel_size=(5,5),strides=(2,2),activation='relu',input_shape=[32,32,3]))
    
    model.add(BatchNormalization())
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(filters=64,kernel_size=(5,5),strides=(2,2),activation='relu'))
    
    model.add(BatchNormalization())
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Flatten())
    model.add(Dense(units=64,activation='relu'))
    model.add(Dropout(rate=0.5))
    model.add(Dense(units=32,activation='relu'))
    model.add(Dropout(rate=0.5))
    model.add(Dense(units=10,activation='softmax'))
    
    model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])
    
    return model

cnn_model=build_cnn()
cnn_model.summary()



cnn_history=cnn_model.fit(x_train,y_train,batch_size=256,epochs=20,validation_split=0.1,verbose=0)

def plot_metrics(history,start=1,end=20):
    
    fig,axes=plt.subplots(1,2,figsize=(10,5))
    
    axes[0].plot(range(start,end+1),history.history['loss'][start-1:end],label='train')
    axes[0].plot(range(start,end+1),history.history['val_loss'][start-1:end],label='validation')
    axes[0].set_title('loss')
    axes[0].legend()
    
    axes[1].plot(range(start,end+1),history.history['accuracy'][start-1:end],label='label')
    axes[1].plot(range(start,end+1),history.history['val_accuracy'][start-1:end],label='validation')
    axes[1].set_title('accuracy')
    axes[1].legend()
plt.show()

plot_metrics(history=cnn_history,start=1,end=20)



#6.3.4 전이 학습으로 분류예측
    #pre-trained 모델 가져오기

from tensorflow.keras.applications import ResNet50
cnn_base=ResNet50(include_top=False,weights='imagenet',input_shape=[32,32,3],classes=10)

def build_transfer():
    transfer_model=Sequential()
    transfer_model.add(cnn_base)
    transfer_model.add(Flatten())
    
    transfer_model.add(Dense(units=64,activation='relu'))
    transfer_model.add(Dropout(rate=0.5))
    transfer_model.add(Dense(units=32,activation='relu'))
    transfer_model.add(Dropout(rate=0.5))
    transfer_model.add(Dense(units=10,activation='softmax'))
    
    transfer_model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])
    
    return transfer_model

transfer_model=build_transfer()
transfer_model.summary()


tm_history=transfer_model.fit(x_train,y_train,batch_size=256,epochs=20,validation_split=0.1,verbose=0)

plot_metrics(history=tm_history,start=1,end=20)





#6-4 자연어 처리(NLP): IMDb 영화 리뷰 감성분석
#6.4.1 IMDb영화 리뷰 데이터셋
import pandas as pd
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import random
import seaborn as sns

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten,Dense,Dropout
from tensorflow.keras.layers import Conv2D,MaxPooling2D,Reshape
from tensorflow.keras.layers import BatchNormalization


seed=12
random.seed(seed)
np.random.seed(seed)
tf.random.set_seed(seed)

from tensorflow.keras import datasets
imdb=datasets.imdb
(x_train,y_train),(x_test,y_test)=imdb.load_data(num_words=10000,index_from=3)

print(x_train.shape,y_train.shape,x_test.shape,y_test.shape)
#(25000,) (25000,) (25000,) (25000,) 


print(x_train[0])
len(x_train[0])                         #Out[55]: 218

word_index=imdb.get_word_index()
word_index
    #숫자 벡터를 텍스트로 변환
def decode_review_vector(review_vector):
    index_to_word={value:key for key,value in word_index.items()}
    
    decoded_review=' '.join([index_to_word.get(idx -3,'?') for idx in review_vector])
    
    return decoded_review

    #첫번째 리뷰의 디코딩
decode_review_vector(x_train[0])

    #첫번째 리뷰의 정답 레이블
y_train[0]

    #각 리뷰의 단어 개수 분포
review_length=[len(review) for review in x_train]
sns.displot(review_length)


#6.4.2 제로패딩
    #padding
from tensorflow.keras.preprocessing import sequence

x_train_pad=sequence.pad_sequences(x_train,maxlen=250)
x_test_pad=sequence.pad_sequences(x_test,maxlen=250)

print(x_train_pad[0])



#6.4.3 단어 임베딩
from tensorflow.keras.layers import Embedding,SimpleRNN,LSTM,GRU

def build_model(model_type='RNN'):
    model=Sequential()
    
    model.add(Embedding(input_dim=10000,output_dim=128))
    
    if model_type=='RNN':
        model.add(SimpleRNN(units=64, return_sequences=True))
        model.add(SimpleRNN(units=64))
    elif model_type=='LSTM':
        model.add(LSTM(units=64,return_sequences=True))
        model.add(LSTM(units=64))
    elif model_type=='GRU':
        model.add(GRU(units=64, return_sequence=True))
        model.add(GRU(units=64))
    
    model.add(Dense(units=32, activation='relu'))
    model.add(Dropout(rate=0.5))
    model.add(Dense(units=1,activation='sigmoid'))
    
    model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])
    
    return model


#6.4.4 RNN
rnn_model=build_model('RNN')
rnn_model.summary()

rnn_history=rnn_model.fit(x_train_pad,y_train,batch_size=32,epochs=10,validation_split=0.1,verbose=2)


    #20 epoch까지 손시 함수와 정확도를 그래프로 나타내는 함수
def plot_metrics(history,start=1,end=20):
    fig,axes=plt.subplots(1,2,figsize=(10,5))
    
    axes[0].plot(range(start,end+1),history.history['loss'][start-1:end],label='train')
    axes[0].plot(range(start,end+1),history.history['val_loss'][start-1:end],label='validation')
    axes[0].set_title("loss")
    axes[0].legend()
    
    axes[1].plot(range(start,end+1),history.history['accuracy'][start-1:end],label='train')
    axes[1].plot(range(start,end+1),history.history['val_accuracy'][start-1:end],label='validation')
    axes[1].set_title("accuracy")
    axes[1].legend()
    
plt.show()

plot_metrics(history=rnn_history,start=1,end=10)


#6.4.5 LSTM
lstm_model=build_model('LSTM')
lstm_history=lstm_model.fit(x_train_pad,y_train,batch_size=32,epochs=10,validation_split=0.1,verbose=0)

plot_metrics(history=lstm_history,start=1,end=10)



#6.4.6 GRU
gru_model=build_model('GRU')
gru_model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])

gru_history=gru_model.fit(x_train_pad,y_train,batch_size=32,epochs=10,validation_split=0.2,verbose=0)

plot_metrics(history=gru_history,start=1,end=10)


#6-5 시계열 분석: 전력 거래 가격 예측

#6.5.1 데이터 탐색
import pandas as pd
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import random
import seaborn as sns

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten,Dense,Dropout
from tensorflow.keras.layers import Conv2D,MaxPooling2D,Reshape
from tensorflow.keras.layers import BatchNormalization


seed=12
random.seed(seed)
np.random.seed(seed)
tf.random.set_seed(seed)

smp=pd.read_csv(r'D:\Workspace\Python\example\python\smp.csv')

smp['date']=pd.to_datetime(smp['date'])
smp['day_of_week']=smp['date'].dt.dayofweek

print(smp.shape)                                                #(820, 5)
smp.head()

    #onehot encoding
smp['day_of_week']=smp['day_of_week'].astype('category')
smp=pd.get_dummies(smp,columns=['day_of_week'],prefix='W',drop_first=True)
smp.head()

    #그래프 그리기
fig,axes=plt.subplots(4,1,figsize=(20,20))

axes[0].plot(smp['date'],smp['smp_max'])
axes[0].set_title('smp_max')

axes[1].plot(smp['date'],smp['smp_mean'])
axes[1].set_title('smp_mean')

axes[2].plot(smp['date'],smp['smp_min'])
axes[2].set_title('smp_min')

axes[3].plot(smp['date'],smp['smp_max'],label='smp_max')
axes[3].plot(smp['date'],smp['smp_mean'],label='smp_mean')
axes[3].plot(smp['date'],smp['smp_min'],label='smp_min')
axes[3].set_title('smp')
axes[3].legend()

plt.show()


#6.5.2 데이터 전처리
    #setting
train_split_idx=729         #2020.1.1 행 인덱스 번호
window_size=10              #과거 10일 동안 시계열 데이터를 학습 데이터로 사용
future=3                    #3일 이후의 타깃 예측

    #features
x_train=smp.iloc[:train_split_idx-window_size-future,0:]

    #targets
y_train=smp.iloc[window_size+future:train_split_idx,[3]]        #smp_mean 열

print(x_train.shape,y_train.shape)                              #(716, 10) (716, 1)

x_train.head(15)
y_train.head(5)

    #x-test
test_start=train_split_idx-window_size-future                   #테스트 데이터 시작행
test_end=smp.shape[0]-window_size-future

x_test=smp.iloc[test_start:test_end,0:]
 
    #y-test
    #label_start= +future  //테스트 데이터의 첫번째 타깃 데이터 위치
y_test=smp.iloc[train_split_idx:,[3]]

print(x_test.shape,y_test.shape)                                #(91, 10) (91, 1)

x_test.head(15)
y_test.head(5)

    #feqture scaling

x_train_scaled=x_train.loc[:,'smp_max':]
x_test_scaled=x_test.loc[:,'smp_max':]

from sklearn.preprocessing import MinMaxScaler

scaler=MinMaxScaler()
scaler.fit(x_train_scaled.values)

x_train_scaled.loc[:,:]=scaler.transform(x_train_scaled.values)
x_test_scaled.loc[:,:]=scaler.transform(x_test_scaled.values)



    #mini batch 크기로 시계열 변환
from tensorflow.keras.preprocessing import timeseries_dataset_from_array    

train_data=timeseries_dataset_from_array(x_train_scaled,y_train,sequence_length=window_size,batch_size=16)    

test_data=timeseries_dataset_from_array(x_test_scaled,y_test,sequence_length=window_size,batch_size=16)

print(train_data)
print(test_data)
#-> shape:(none,none,9), (none,1)  typeds(tf.float64,tf.float64)   

for batch in test_data.take(1):
    inputs,targets=batch

print("input:",inputs.numpy().shape)                    #input: (16, 10, 9)
print("target:",targets.numpy().shape)                  #target: (16, 1)

inputs[0]               #10타임스탭, 9피처 형태 가지고있는것 확인가능 

targets[0]              #<tf.Tensor: shape=(1,), dtype=float64, numpy=array([81.46])





#6.5.3 LSTM모델로 시계열 예측
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Input, LSTM, Dense

model=Sequential()
model.add(Input(shape=[10,9]))

model.add(LSTM(units=32, return_sequences=False))
model.add(Dense(units=1, activation='linear'))

model.compile(optimizer='adam',loss='mse',metrics=['mae'])

model.summary()


history=model.fit(train_data,epochs=500,validation_data=test_data,verbose=0)

def plot_loss_curve(history,total_epoch=10,start=1):
    plt.figure(figsize=(5,5))
    plt.plot(range(start,total_epoch+1),history.history['loss'][start-1:total_epoch],label='train')
    
    plt.plot(range(start,total_epoch+1),history.history['val_loss'][start-1:total_epoch],label='validation')
    
    plt.xlabel('epochs')
    plt.ylabel('mse')
    plt.legend()
    plt.show()

plot_loss_curve(history=history,total_epoch=len(history.history['loss']),start=1)

y_pred=model.predict(test_data)
y_pred.shape                            #Out[71]: (82, 1)

plt.figure(figsize=(20,10))
plt.plot(range(len(y_pred)),y_test[window_size-1:],label='y_test')
plt.plot(range(len(y_pred)),y_pred,label='y_pred')
plt.legend()
plt.show()