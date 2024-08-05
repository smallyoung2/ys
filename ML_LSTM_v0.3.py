import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

# 엑셀 파일 경로
excel_file = 'C:/Users/YS702/ML_LSTM_test_v0.1.xlsx'

# 엑셀 파일 읽기
df = pd.read_excel(excel_file)

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

# 데이터셋 분할 (train, validation, test)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
X_train, X_val, Y_train, Y_val = train_test_split(X_train, Y_train, test_size=0.25, random_state=42)

# 데이터 형태 변환 (LSTM 모델에 맞게 3차원으로 변환)
X_train = X_train.reshape(X_train.shape[0], X_train.shape[1], 1)
X_val = X_val.reshape(X_val.shape[0], X_val.shape[1], 1)
X_test = X_test.reshape(X_test.shape[0], X_test.shape[1], 1)

# LSTM 모델 구성
model = Sequential()
model.add(LSTM(64, return_sequences=True, input_shape=(time_step, 1)))
model.add(LSTM(32, return_sequences=False))
model.add(Dense(16, activation='relu'))
model.add(Dense(1))

# 모델 컴파일 및 학습
model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(X_train, Y_train, validation_data=(X_val, Y_val), batch_size=32, epochs=50)

# 예측
train_predict = model.predict(X_train)
val_predict = model.predict(X_val)
test_predict = model.predict(X_test)

# 예측 결과 반정규화
train_predict = scaler.inverse_transform(train_predict)
val_predict = scaler.inverse_transform(val_predict)
test_predict = scaler.inverse_transform(test_predict)

# 실제값 반정규화
Y_train = scaler.inverse_transform([Y_train]).T
Y_val = scaler.inverse_transform([Y_val]).T
Y_test = scaler.inverse_transform([Y_test]).T

# 모델 평가
from sklearn.metrics import mean_squared_error, r2_score
train_mse = mean_squared_error(Y_train, train_predict)
val_mse = mean_squared_error(Y_val, val_predict)
test_mse = mean_squared_error(Y_test, test_predict)

train_r2 = r2_score(Y_train, train_predict)
val_r2 = r2_score(Y_val, val_predict)
test_r2 = r2_score(Y_test, test_predict)

print("Train MSE: {:.4f}".format(train_mse))
print("Validation MSE: {:.4f}".format(val_mse))
print("Test MSE: {:.4f}".format(test_mse))
print("Train R2: {:.4f}".format(train_r2))
print("Validation R2: {:.4f}".format(val_r2))
print("Test R2: {:.4f}".format(test_r2))