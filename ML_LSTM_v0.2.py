# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 12:09:31 2024

@author: YS702
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense


#%%

#%%
# 엑셀 파일 경로
excel_file = 'C:/Users/YS702/ML_LSTM_test_v0.1.xlsx'

# 엑셀 파일 읽기
df = pd.read_excel(excel_file)


#%%

# 특정 도시의 데이터 선택
city_data = df['전국'].values.reshape(-1, 1)

# 데이터 정규화
scaler = MinMaxScaler()
city_data_scaled = scaler.fit_transform(city_data)

# 시계열 데이터셋 생성
def create_dataset(df, time_step=1):
    X, Y = [], []
    for i in range(len(df) - time_step - 1):
        a = df[i:(i + time_step), 0]
        X.append(a)
        Y.append(df[i + time_step, 0])
    return np.array(X), np.array(Y)

time_step = 12
X, Y = create_dataset(city_data_scaled, time_step)

# 데이터셋 나누기
train_size = int(len(X) * 0.7)
test_size = len(X) - train_size
X_train, X_test = X[0:train_size], X[train_size:len(X)]
Y_train, Y_test = Y[0:train_size], Y[train_size:len(Y)]

# 데이터 형태 변환 (LSTM 모델에 맞게 3차원으로 변환)
X_train = X_train.reshape(X_train.shape[0], X_train.shape[1], 1)
X_test = X_test.reshape(X_test.shape[0], X_test.shape[1], 1)

# LSTM 모델 구성
model = Sequential()
model.add(LSTM(50, return_sequences=True, input_shape=(time_step, 1)))
model.add(LSTM(50, return_sequences=False))
model.add(Dense(25))
model.add(Dense(1))

# 모델 컴파일 및 학습
model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(X_train, Y_train, batch_size=1, epochs=1)

# 예측
train_predict = model.predict(X_train)
test_predict = model.predict(X_test)

# 예측 결과 반정규화
train_predict = scaler.inverse_transform(train_predict)
test_predict = scaler.inverse_transform(test_predict)

# 실제값 반정규화
Y_train = scaler.inverse_transform([Y_train])
Y_test = scaler.inverse_transform([Y_test])

print("Train Predict: ", train_predict)
print("Test Predict: ", test_predict)

#%%

# Train Predict 결과를 DataFrame으로 만들기
train_pred_df = pd.DataFrame({
    'Actual': Y_train, 
    'Predicted': train_predict
})

# Test Predict 결과를 DataFrame으로 만들기 
test_pred_df = pd.DataFrame({
    'Actual': Y_test,
    'Predicted': test_predict
})

# Train Predict 결과를 엑셀 파일로 저장하기
train_pred_df.to_excel('train_predict_results.xlsx', index=False)

# Test Predict 결과를 엑셀 파일로 저장하기
test_pred_df.to_excel('test_predict_results.xlsx', index=False)


