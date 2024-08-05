import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

# 데이터 불러오기
data = pd.read_csv('ML_DATA_0.1.csv')

# 특정 도시의 데이터 선택
city_data = data['서울특별시'].values.reshape(-1, 1)

# 데이터 정규화
scaler = MinMaxScaler()
city_data_scaled = scaler.fit_transform(city_data)

# 시계열 데이터셋 생성
def create_dataset(data, time_step=1):
    X, Y = [], []
    for i in range(len(data) - time_step - 1):
        a = data[i:(i + time_step), 0]
        X.append(a)
        Y.append(data[i + time_step, 0])
    return np.array(X), np.array(Y)

time_step = 12
X, Y = create_dataset(city_data_scaled, time_step)

# 데이터셋 나누기
train_size = int(len(X) * 0.7)
test_size = len(X) - train_size
X_train, X_test = X[0:train_size], X[train_size:len(X)]
Y_train, Y_test = Y[0:train_size], Y[train_size:len(Y)]

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