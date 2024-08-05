# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 15:51:28 2024

@author: soyoung
"""

import pandas as pd
import matplotlib.pyplot as plt

# 한글 폰트 설정
from matplotlib import font_manager, rc
font_path = 'C:/Windows/Fonts/malgun.ttf'
font_name = font_manager.FontProperties(fname = font_path).get_name()
rc('font', family = font_name)

df = pd.read_excel(r'D:\Workspace\Python\mini\The elderly driver traffic accidents(suwon).xlsx')

#%% 전처리
# [사고일시] -> datetime
df['사고일시'] = pd.to_datetime(df['사고일시'], format='%Y년 %m월 %d일 %H시')  ## 2023-01-01 00:00:00
#   날짜(object)                   
df['날짜'] = df['사고일시'].dt.date                                            ## 2023-01-01
#   연(int)
df['연'] = df['사고일시'].dt.year                                              ## 2023
#   월(int)
df['월'] = df['사고일시'].dt.month                                             ## 1
#   일(int)
df['일'] = df['사고일시'].dt.day                                               ## 1
#   시간(int)
df['시간'] = df['사고일시'].dt.hour                                            ## 0
# 시간대 -> 주간/야간
""" 기준
주간: 오전 7시부터 오후 8시까지 (13시간)
야간: 오후 8시부터 다음 날 오전 7시까지 (11시간)
"""
df['주야간'] = df['시간'].apply(lambda x: '주간' if 7 <= x <= 20 else '야간')

# [시군구] -> 구/ 동
gu = []
dong = []
for i in range(len(df)) :
    gu.append(df['시군구'].str.split(' ')[i][2])
    dong.append(df['시군구'].str.split(' ')[i][3])
df['구'] = gu 
df['동'] = dong

# [사고유형] '차대사람 - 기타' -> '차대사람', '기타'
dep1 = []
dep2 = []
for i in range(len(df)) :
    dep1.append(df['사고유형'].str.split(' - ')[i][0])
    dep2.append(df['사고유형'].str.split(' - ')[i][1])
df['사고유형1'] = dep1
df['사고유형2'] = dep2

# [도로형태] '단일로 - 기타' -> '단일로', '기타'
dep1 = []
dep2 = []
for i in range(len(df)) :
    dep1.append(df['도로형태'].str.split(' - ')[i][0])
    dep2.append(df['도로형태'].str.split(' - ')[i][1])
df['도로형태1'] = dep1
df['도로형태2'] = dep2

# [피해운전자] nan -> 0
""" df.iloc[:, 18:22].columns 
Index(['피해운전자 차종', '피해운전자 성별', '피해운전자 연령', '피해운전자 상해정도'], dtype='object')
"""
df.iloc[:, 18:22] = df.iloc[:, 18:22].fillna(0)

# [연령] 00세(object) -> 00(int)
# '가해운전자'
df['가해운전자 연령'] = df['가해운전자 연령'].str[:-1]
# int 변환
df['가해운전자 연령'] = df['가해운전자 연령'].astype('int64')
#
# '피해운전자'
df['피해운전자 연령'] = df['피해운전자 연령'].str[:-1]
## -> nan(0->nan), '미분'('미분류') 존재
#       -> '미분류' : 0
df['피해운전자 연령'] = df['피해운전자 연령'].replace('미분', 0)
#       -> nan : 0
df['피해운전자 연령'] = df['피해운전자 연령'].fillna(0)
# int 변환
df['피해운전자 연령'] = df['피해운전자 연령'].astype('int64')

#%%
df.columns
"""
Index(['사고번호', '사고일시', '요일', '시군구', '사고내용', '사망자수', '중상자수', '경상자수', '부상신고자수',
       '사고유형', '법규위반', '노면상태', '기상상태', '도로형태', '가해운전자 차종', '가해운전자 성별',
       '가해운전자 연령', '가해운전자 상해정도', '피해운전자 차종', '피해운전자 성별', '피해운전자 연령',
       '피해운전자 상해정도', '날짜', '연', '월', '일', '시간', '구', '동', '사고유형1', '사고유형2',
       '도로형태1', '도로형태2', '주야간'],
      dtype='object')
"""

df_table = df.loc[:, ['날짜', '연', '월', '일', '요일', '시간', '주야간',
                      '구', '동', '노면상태', '기상상태', '도로형태1', '도로형태2', 
                      '법규위반', '사고유형1', '사고유형2', '사고내용',
                      '가해운전자 차종', '가해운전자 성별', '가해운전자 연령', '가해운전자 상해정도', 
                      '피해운전자 차종', '피해운전자 성별', '피해운전자 연령', '피해운전자 상해정도',
                      '사망자수', '중상자수', '경상자수', '부상신고자수'
                      ]]

df_table['사고건수'] = 1

#%% ECLO 계산 함수
def cal_eclo(df) :
    df['ECLO'] = df['사망자수']*10 + df['중상자수']*5 + df['경상자수']*3 + df['부상신고자수']*1
    df['ECLO/사고건수'] = df['ECLO']/df['사고건수']
    return df

#%%
accident_cnt = df_table.groupby(['주야간', '구', '노면상태', '기상상태', '도로형태1', 
                      '가해운전자 차종', '가해운전자 성별'])[['사고건수', '사망자수', '중상자수', '경상자수', '부상신고자수']].sum()
accident_cnt = accident_cnt.reset_index()
cal_eclo(accident_cnt) 
print(accident_cnt)


accident_cnt.info()


#%%
## 원핫 인코딩
#################

from sklearn.preprocessing import OneHotEncoder

# OneHotEncoder 객체 생성
encoder = OneHotEncoder(handle_unknown='ignore')

# 원핫인코딩을 적용할 열 리스트 
#날짜,일,시간 제외

columns_to_encode = [ '연', '월', '요일', '주야간',
                      '구', '동', '노면상태', '기상상태', '도로형태1', '도로형태2', 
                      '법규위반', '사고유형1', '사고유형2', '사고내용',
                      '가해운전자 차종', '가해운전자 성별', '가해운전자 연령', '가해운전자 상해정도', 
                      '피해운전자 차종', '피해운전자 성별', '피해운전자 연령', '피해운전자 상해정도',
                      '사망자수', '중상자수', '경상자수', '부상신고자수']

df_table = df_table[columns_to_encode].astype(str)

# 원핫인코딩 적용
encoded_data = encoder.fit_transform(df_table)

# 인코딩된 데이터를 데이터프레임으로 변환
encoded_df = pd.DataFrame(encoded_data.toarray(), columns=encoder.get_feature_names_out(columns_to_encode))

df_table_encoded = pd.concat([df_table.drop(columns=columns_to_encode), encoded_df], axis=1)


print(df_table_encoded.head())

print(encoded_df.head())

