# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 11:15:51 2024

@author: soyoung
"""


import pandas as pd

# 한글 폰트 설정
from matplotlib import font_manager, rc
font_path = 'C:/Windows/Fonts/malgun.ttf'
font_name = font_manager.FontProperties(fname = font_path).get_name()
rc('font', family = font_name)

#%% 수원사고 데이터 
df = pd.read_excel('D:\Workspace\Python\mini\The elderly driver traffic accidents(suwon).xlsx')

# ## 전처리
# [사고일시] -> datetime
df['사고일시'] = pd.to_datetime(df['사고일시'], format='%Y년 %m월 %d일 %H시')  ## 2023-01-01 00:00:00
#   시간(int)
df['시간'] = df['사고일시'].dt.hour                                            ## 0

# [시군구] -> 구/ 동
gu = []
dong = []
for i in range(len(df)) :
    gu.append(df['시군구'].str.split(' ')[i][2])
    dong.append(df['시군구'].str.split(' ')[i][3])
df['구'] = gu 
df['동'] = dong

# 시간대 -> 주간/야간
"""
수도권:
주간: 오전 7시부터 오후 8시까지 (13시간)
야간: 오후 8시부터 다음 날 오전 7시까지 (11시간)
"""
df['주야간'] = df['시간'].apply(lambda x: '주간' if 7 <= x <= 20 else '야간')

# 사고건수
df['사고건수'] = 1


#%% ECLO 계산 함수
def cal_eclo(df) :
    df['ECLO'] = df['사망자수']*10 + df['중상자수']*5 + df['경상자수']*3 + df['부상신고자수']*1
    df['ECLO/사고건수'] = df['ECLO']/df['사고건수']
    return df

#%%
###############################################################################
# 요인별 ECLO 계산
###############################################################################
# ## 열 추출
accidents = df.loc[:, ['주야간', '구', '동', '노면상태', '기상상태', '사고건수',
                     '사망자수', '중상자수', '경상자수', '부상신고자수']]

# 주야간
time_group = accidents.groupby('주야간')[['사고건수', '사망자수', '중상자수', '경상자수', '부상신고자수']].sum()
cal_eclo(time_group)
"""
     사고건수  사망자수  중상자수  경상자수  부상신고자수  ECLO  ECLO/사고건수
주야간                                                 
야간    307     4    74   316      20  1378   4.488599
주간   1573    12   333  1693     178  7042   4.476796
"""

# 동
dong_group = accidents.groupby('동')[['사고건수', '사망자수', '중상자수', '경상자수', '부상신고자수']].sum()
cal_eclo(dong_group)
"""
       사고건수  사망자수  중상자수  경상자수  부상신고자수  ECLO  ECLO/사고건수
동                                                     
고등동      22     0     2    24       5    87   3.954545
고색동      54     0     8    54      12   214   3.962963
곡반정동     26     0     3    31       2   110   4.230769
교동        4     0     0     6       0    18   4.500000
구운동      51     1    15    52      11   252   4.941176
구천동       5     0     2     4       0    22   4.400000
권선동     108     2    24   119       6   503   4.657407
금곡동      39     0    11    33       3   157   4.025641
남수동       6     0     1     7       1    27   4.500000
남창동       1     0     0     2       0     6   6.000000
당수동      13     0     1    17       3    59   4.538462
대황교동      3     0     2     2       0    16   5.333333
망포동      28     0     3    39       1   133   4.750000
매교동      20     1     3    20       1    86   4.300000
매산로1가    69     0     3   102       9   330   4.782609
매산로2가    18     0     3    13       3    57   3.166667
매산로3가     9     0     1     8       1    30   3.333333
매탄동      64     1    18    56       5   273   4.265625
매향동       4     0     2     3       0    19   4.750000
북수동      13     0     7     8       1    60   4.615385
서둔동      38     0     9    42       9   180   4.736842
세류동      87     3    30    81       8   431   4.954023
송죽동      49     0     8    57       6   217   4.428571
신동        7     0     3     5       1    31   4.428571
신풍동       3     0     0     3       0     9   3.000000
연무동      49     0    10    46       6   194   3.959184
영동        8     0     3     5       1    31   3.875000
영통동      57     1    13    61       4   262   4.596491
영화동     102     1    27    92      10   431   4.225490
오목천동     25     2     5    20       9   114   4.560000
우만동      92     1    18    94       8   390   4.239130
원천동      50     0    13    57       4   240   4.800000
율전동      32     0     3    39       2   134   4.187500
이목동      17     0     4    17       0    71   4.176471
이의동      71     0     5    90       5   300   4.225352
인계동     106     0    25   122       2   493   4.650943
입북동      13     0     4    15       1    66   5.076923
장안동       8     0     2     7       0    31   3.875000
정자동     109     1    28   107      15   486   4.458716
조원동      48     2    13    46       6   229   4.770833
중동       10     0     1    13       1    45   4.500000
지동       41     0    17    32       5   186   4.536585
천천동      27     0    13    27       3   149   5.518519
탑동       29     0     4    34       2   124   4.275862
파장동      49     0     7    62       6   227   4.632653
팔달로1가     6     0     2     4       0    22   3.666667
팔달로2가    15     0     3    16       0    63   4.200000
팔달로3가    12     0     2    14       2    54   4.500000
평동       28     0     0    50       1   151   5.392857
평리동       2     0     0     2       0     6   3.000000
하광교동      5     0     1    12       0    41   8.200000
하동        7     0     1    10       2    37   5.285714
호매실동     43     0     4    52       6   182   4.232558
화서동      78     0    20    75       9   334   4.282051
"""

# 노면상태
road_group = accidents.groupby('노면상태')[['사고건수', '사망자수', '중상자수', '경상자수', '부상신고자수']].sum()
cal_eclo(road_group)
"""
       사고건수  사망자수  중상자수  경상자수  부상신고자수  ECLO  ECLO/사고건수
노면상태                                                  
건조     1711    14   362  1825     180  7605   4.444769
기타        6     0     1     7       2    28   4.666667
서리/결빙     8     0     3     7       3    39   4.875000
적설        4     0     1     4       0    17   4.250000
젖음/습기   151     2    40   166      13   731   4.841060
"""

# 기상상태
weather_group = accidents.groupby('기상상태')[['사고건수', '사망자수', '중상자수', '경상자수', '부상신고자수']].sum()
cal_eclo(weather_group)
"""
      사고건수  사망자수  중상자수  경상자수  부상신고자수  ECLO  ECLO/사고건수
기상상태                                                 
기타       6     0     1     8       0    29   4.833333
눈        7     0     1     6       2    25   3.571429
맑음    1684    13   364  1794     180  7512   4.460808
비      119     2    28   133      12   571   4.798319
흐림      64     1    13    68       4   283   4.421875
"""

#%%
###############################################################################
# 요인별 순위기준 위험지수(가중치부여) 데이터
###############################################################################

risk_score = pd.read_csv(r'D:\Workspace\Python\mini\요인별 위험지수_동(가중치부여).csv', index_col='Unnamed: 0')

element_risk = risk_score.copy()
    
# 동
dong_list = list(df['동'].unique())
for x in dong_list :
    element_risk.loc[element_risk['동'] == x, '동_eclo'] = dong_group.loc[x, 'ECLO/사고건수']

# 주야간
time_list = ['주간', '야간']
for x in time_list :
    element_risk.loc[element_risk['주야간'] == x, '주야간_eclo'] = time_group.loc[x, 'ECLO/사고건수']
    
# 노면상태
road_list = ['건조', '서리/결빙', '젖음/습기', '기타', '적설']
for x in road_list :
    element_risk.loc[element_risk['노면상태'] == x, '노면상태_eclo'] = road_group.loc[x, 'ECLO/사고건수']
    
# 기상상태
weather_list = ['맑음', '눈', '흐림', '기타', '비']
for x in weather_list :
    element_risk.loc[element_risk['기상상태'] == x, '기상상태_eclo'] = weather_group.loc[x, 'ECLO/사고건수']

print(element_risk)
"""
        구    동 주야간   노면상태  ...    동_eclo  주야간_eclo  노면상태_eclo  기상상태_eclo
0     장안구  정자동  주간     건조  ...  4.458716  4.476796   4.444769   4.460808
1     권선구  권선동  주간     건조  ...  4.657407  4.476796   4.444769   4.460808
2     장안구  정자동  주간  젖음/습기  ...  4.458716  4.476796   4.841060   4.460808
3     장안구  정자동  주간     건조  ...  4.458716  4.476796   4.444769   4.798319
4     장안구  정자동  야간     건조  ...  4.458716  4.488599   4.444769   4.460808
  ...  ...  ..    ...  ...       ...       ...        ...        ...
2695  팔달구  남창동  야간     적설  ...  6.000000  4.488599   4.250000   3.571429
2696  권선구  평리동  야간     적설  ...  3.000000  4.488599   4.250000   4.833333
2697  팔달구  남창동  야간     기타  ...  6.000000  4.488599   4.666667   4.833333
2698  팔달구  남창동  주간     적설  ...  6.000000  4.476796   4.250000   4.833333
2699  팔달구  남창동  야간     적설  ...  6.000000  4.488599   4.250000   4.833333

[2700 rows x 15 columns]
"""

# 요인별 (순위지수 + ECLO) = eclo_risk_sum
element_risk['eclo_risk_sum'] = element_risk.iloc[:, [5,6,7,8,11,12,13,14]].sum(axis=1) 


# 요인별 (순위지수 * ECLO) = eclo_risk_mul

element_risk['eclo_risk_mul'] = 0

for i, j in [(5,11),(6,12),(7,13),(8,14)] :
    val = element_risk.iloc[:, i]*element_risk.iloc[:, j]
    element_risk['eclo_risk_mul'] = element_risk['eclo_risk_mul'] + val
    

element_risk.to_csv('요인별 위험지수_동(ECLO 추가).csv')


#%%
# 위험지수 기초통계
# - 순위지수

element_risk.iloc[:, -12:-8].describe()

"""
            동_risk     주야간_risk    노면상태_risk    기상상태_risk
count  2700.000000  2700.000000  2700.000000  2700.000000
mean     27.370370     1.500000     3.000000     3.000000
std      15.718316     0.500093     1.414476     1.414476
min       1.000000     1.000000     1.000000     1.000000
25%      13.000000     1.000000     2.000000     2.000000
50%      27.500000     1.500000     3.000000     3.000000
75%      41.000000     2.000000     4.000000     4.000000
max      54.000000     2.000000     5.000000     5.000000
"""

# - eclo 값
element_risk.iloc[:, -6:-2].describe()

"""
            동_eclo     주야간_eclo    노면상태_eclo    기상상태_eclo
count  2700.000000  2700.000000  2700.000000  2700.000000
mean      4.489934     4.482698     4.615499     4.417153
std       0.762943     0.005903     0.238193     0.455204
min       3.000000     4.476796     4.250000     3.571429
25%       4.200000     4.476796     4.444769     4.421875
50%       4.479358     4.482698     4.666667     4.460808
75%       4.750000     4.488599     4.841060     4.798319
max       8.200000     4.488599     4.875000     4.833333
"""

# - total, corr, eclo_sum, eclo_mul
element_risk.iloc[:, [-8,-7,-2,-1]].describe()

"""
        total_risk    corr_risk  eclo_risk_sum  eclo_risk_mul
count  2700.000000  2700.000000    2700.000000    2700.000000
mean     34.870370    62.590904      52.875654     156.358083
std      15.852981    31.383087      15.857259      72.212811
min       4.000000     5.201500      21.310028      19.571933
25%      21.000000    35.246604      39.034050      93.121681
50%      35.000000    62.556027      53.037661     157.169251
75%      48.000000    89.534820      66.542452     217.579462
max      66.000000   120.496625      83.841088     300.324068
""" 


# element_rist 의 columns
element_risk.iloc[:,:].columns

"""
Index(['구', '동', '주야간', '노면상태', '기상상태', '동_risk', '주야간_risk', '노면상태_risk',
       '기상상태_risk',  'total_risk',  'corr_risk',  '동_eclo',  '주야간_eclo',
       '노면상태_eclo',  '기상상태_eclo',  'eclo_risk_sum',  eclo_risk_mul'],
      dtype='object')  """
