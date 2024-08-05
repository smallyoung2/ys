# -*- coding: utf-8 -*-
"""
Created on Wed May  8 14:12:27 2024

@author: soyoung
"""


import pandas as pd
import matplotlib.pyplot as plt

# 한글 폰트 설정
from matplotlib import font_manager, rc
font_path = 'C:/Windows/Fonts/malgun.ttf'
font_name = font_manager.FontProperties(fname = font_path).get_name()
rc('font', family = font_name)

df = pd.read_excel('The elderly driver traffic accidents(suwon).xlsx')

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
       '도로형태1', '도로형태2'],
      dtype='object')
"""

df_table = df.loc[:, ['날짜', '연', '월', '일', '요일', '시간', 
                      '구', '동', '노면상태', '기상상태', '도로형태1', '도로형태2', 
                      '법규위반', '사고유형1', '사고유형2', '사고내용',
                      '가해운전자 차종', '가해운전자 성별', '가해운전자 연령', '가해운전자 상해정도', 
                      '피해운전자 차종', '피해운전자 성별', '피해운전자 연령', '피해운전자 상해정도',
                      '사망자수', '중상자수', '경상자수', '부상신고자수'
                      ]]

df_table['사고건수'] = 1
df_table.info()

#%% ECLO 계산 함수
def cal_eclo(df) :
    df['ECLO'] = df['사망자수']*10 + df['중상자수']*5 + df['경상자수']*3 + df['부상신고자수']*1
    df['ECLO/사고건수'] = df['ECLO']/df['사고건수']
    return df

#%% 막대그래프_사고건수, ECLO
def plot_bar(df, col) :
    df = df.reset_index()
    plt.figure(figsize=(15,5))
    plt.subplot(1, 2, 1)
    plt.bar(df[col], df['사고건수'], label ='사고건수')
    plt.legend(loc='best')
    plt.xticks(rotation='vertical')
    plt.subplot(1, 2, 2)
    plt.bar(df[col], df['ECLO/사고건수'], label ='ECLO')
    plt.legend(loc='best')
    plt.xticks(rotation='vertical')
    
    plt.savefig('./graph/'+ f'graph_{col}별 교통사고.png')
    plt.show()

#%% 연도별 교통사고 현황
year_table = df_table.groupby('연')[['사고건수', '사망자수', '중상자수', '경상자수', '부상신고자수']].sum()
year_table = cal_eclo(year_table)
print(year_table)
"""
      사고건수  사망자수  중상자수  경상자수  부상신고자수  ECLO  ECLO/사고건수
연                                                    
2021   569        6          123     589         67         2509    4.409490
2022   561        6          116     576         62         2430    4.331551
2023   750        4          168     844         69         3481    4.641333
"""

plot_bar(year_table, '연')

# -> 사고발생 : 2023년 > 2021년 
# -> ECLO : 2023년 > 2021년

#%% 월별 교통사고 현황

month_table = df_table.groupby('월')[['사고건수', '사망자수', '중상자수', '경상자수', '부상신고자수']].sum()
month_table = cal_eclo(month_table)
print(month_table)
"""
    사고건수  사망자수  중상자수  경상자수  부상신고자수  ECLO  ECLO/사고건수
월                                                  
1    130     2    23   138      12   561   4.315385
2    154     1    41   171      13   741   4.811688
3    146     2    29   140      15   600   4.109589
4    152     0    37   155      19   669   4.401316
5    179     2    42   196      17   835   4.664804
6    165     3    40   186      14   802   4.860606
7    130     0    26   144      19   581   4.469231
8    158     1    38   177      13   744   4.708861
9    156     1    28   173      17   686   4.397436
10   182     3    37   173      15   749   4.115385
11   161     0    28   165      21   656   4.074534
12   167     1    38   191      23   796   4.766467
"""

plot_bar(month_table, '월')
# -> 사고발생 : 10월 > 5월 
# -> ECLO : 6월 > 2월

#%% 요일별 교통사고 현황
weekly_table = df_table.groupby('요일')[['사고건수', '사망자수', '중상자수', '경상자수', '부상신고자수']].sum()
weekly_table = cal_eclo(weekly_table)
print(weekly_table)
"""
     사고건수  사망자수  중상자수  경상자수  부상신고자수  ECLO  ECLO/사고건수
요일                                                  
금요일   333     5    72   338      36  1460   4.384384
목요일   261     3    61   271      26  1174   4.498084
수요일   260     2    58   263      26  1125   4.326923
월요일   302     3    58   308      31  1275   4.221854
일요일   178     1    41   234      19   936   5.258427
토요일   264     2    59   295      30  1230   4.659091
화요일   282     0    58   300      30  1220   4.326241
"""

plot_bar(weekly_table, '요일')
# -> 사고발생 : 금요일 > 월요일 
# -> ECLO : 일요일 > 토요일

#%% 시간대별 교통사고 현황
time_table = df_table.groupby('시간')[['사고건수', '사망자수', '중상자수', '경상자수', '부상신고자수']].sum()
time_table = cal_eclo(time_table)
print(time_table)
"""
    사고건수  사망자수  중상자수  경상자수  부상신고자수  ECLO  ECLO/사고건수
시간                                                 
0     20     0     5    19       2    84   4.200000
1     11     0     5    11       0    58   5.272727
2     11     0     2    14       1    53   4.818182
3     15     0     2    21       0    73   4.866667
4     19     1     8    18       0   104   5.473684
5     34     1    11    23       5   139   4.088235
6     73     0    18    67       5   296   4.054795
7     61     1    12    58       4   248   4.065574
8     95     0    28   111      10   483   5.084211
9     96     1    27    87       7   413   4.302083
10   119     4    19   115      14   494   4.151261
11   130     2    28   137       9   580   4.461538
12   102     0    19   113      13   447   4.382353
13   134     1    25   164      19   646   4.820896
14   116     0    20   112      14   450   3.879310
15   132     1    25   152      14   605   4.583333
16   152     1    38   149      21   668   4.394737
17   132     0    32   157      18   649   4.916667
18   129     0    25   142      14   565   4.379845
19    97     0    17   112      11   432   4.453608
20    78     1    18    84      10   362   4.641026
21    53     2     9    62       2   253   4.773585
22    37     0     9    48       2   191   5.162162
23    34     0     5    33       3   127   3.735294
"""

plot_bar(time_table, '시간')
# -> 사고발생 : 16시 > 13시
# -> ECLO : 4시 > 1시

#%% 요일별.시간대별 교통사고 현황
weekly_time_pivot = df_table.pivot_table(index='시간', columns='요일', values='사고건수', aggfunc=sum)
print(weekly_time_pivot)
"""
요일   금요일   목요일   수요일   월요일   일요일   토요일   화요일
시간                                          
0    5.0   1.0   2.0   2.0   5.0   3.0   2.0
1    1.0   2.0   1.0   2.0   4.0   1.0   NaN
2    2.0   NaN   1.0   NaN   1.0   5.0   2.0
3    3.0   2.0   1.0   2.0   3.0   2.0   2.0
4    4.0   2.0   3.0   3.0   2.0   3.0   2.0
5    5.0   3.0   5.0   7.0   3.0   3.0   8.0
6   16.0  10.0   9.0  16.0   7.0   5.0  10.0
7   17.0  11.0   8.0  13.0   3.0   3.0   6.0
8   18.0  13.0  16.0  23.0   6.0   3.0  16.0
9   18.0  10.0  18.0  13.0   5.0  15.0  17.0
10  20.0  23.0   9.0  26.0   9.0  12.0  20.0
11  17.0  18.0  17.0  19.0  14.0  28.0  17.0
12  16.0   8.0  11.0  17.0  11.0  22.0  17.0
13  16.0  28.0  18.0  18.0  18.0  23.0  13.0
14  22.0  12.0  20.0  12.0  13.0  20.0  17.0
15  17.0  21.0  20.0  20.0  16.0  13.0  25.0
16  24.0  17.0  20.0  30.0  10.0  22.0  29.0
17  25.0  16.0  21.0  23.0  13.0  20.0  14.0
18  31.0  18.0  17.0  20.0   9.0  17.0  17.0
19  13.0  13.0  14.0  16.0   9.0  15.0  17.0
20  16.0  12.0  11.0  13.0   3.0  10.0  13.0
21  11.0  10.0   8.0   2.0   6.0   9.0   7.0
22   7.0   6.0   6.0   3.0   6.0   5.0   4.0
23   9.0   5.0   4.0   2.0   2.0   5.0   7.0
"""

import seaborn as sns
sns.heatmap(weekly_time_pivot, annot=True, cmap ='coolwarm', linewidth = .5, cbar = False)
plt.show()
# -> 사고발생 : 금요일18시 > 월요일16시

#%% 사고유형별 교통사고 현황
type_table = df_table.groupby(['사고유형1', '사고유형2'])[['사고건수', '사망자수', '중상자수', '경상자수', '부상신고자수']].sum()
type_table = cal_eclo(type_table)
print(type_table)
"""
                  사고건수  사망자수  중상자수  경상자수  부상신고자수  ECLO  ECLO/사고건수
사고유형1 사고유형2                                                      
차대사람  기타           174     2    48   120      15   635   3.649425
      길가장자리구역통행중    18     0     4    14       0    62   3.444444
      보도통행중         19     1     5    14       2    79   4.157895
      차도통행중         23     1     9    12       2    93   4.043478
      횡단중          113     1    48    65       4   449   3.973451
차대차   기타           533     1   103   551      68  2246   4.213884
      정면충돌          40     2    18    42       2   238   5.950000
      추돌           275     2    46   384      33  1435   5.218182
      측면충돌         604     5   102   736      60  2828   4.682119
      후진중충돌         34     0     0    47       6   147   4.323529
차량단독  공작물충돌         12     1     4     9       1    58   4.833333
      기타            32     0    17    15       5   135   4.218750
      전도전복           3     0     3     0       0    15   5.000000
"""

plot_bar(type_table, '사고유형1')
plot_bar(type_table, '사고유형2')

# -> 사고발생 : 차대차 > 차대사람 // 차대차(측면충돌) > 차대차(기타)
# -> ECLO : 차대차 > 차량단독     // 차대차(정면충돌) > 차대차(추돌)

#%% 가해운전자 연령별 교통사고 현황
age_table = df_table.groupby('가해운전자 연령')[['사고건수', '사망자수', '중상자수', '경상자수', '부상신고자수']].sum()
age_table = cal_eclo(age_table)
print(age_table)
"""
          사고건수  사망자수  중상자수  경상자수  부상신고자수  ECLO  ECLO/사고건수
가해운전자 연령                                                 
65         223     0    48   257      15  1026   4.600897
66         226     4    33   243      20   954   4.221239
67         193     1    37   229      18   900   4.663212
68         161     1    24   181      16   689   4.279503
69         184     3    51   208      12   921   5.005435
70         148     0    40   148      14   658   4.445946
71         120     3    28   139      11   598   4.983333
72          82     0    18    85      16   361   4.402439
73          90     0    20    95      10   395   4.388889
74          96     1    21    79      15   367   3.822917
75          73     1    15    78       3   322   4.410959
76          49     0    11    49       7   209   4.265306
77          47     0    10    48       5   199   4.234043
78          30     0    10    21       5   118   3.933333
79          36     0     6    28       6   120   3.333333
80          34     0    11    28       6   145   4.264706
81          18     1     9    21       2   120   6.666667
82          20     0     2    26       1    89   4.450000
83          18     1     3    16      10    83   4.611111
84           8     0     3     5       1    31   3.875000
85          10     0     3    13       2    56   5.600000
86           4     0     2     3       1    20   5.000000
87           6     0     1     6       2    25   4.166667
88           3     0     0     3       0     9   3.000000
93           1     0     1     0       0     5   5.000000
"""

plot_bar(age_table, '가해운전자 연령')
# -> 사고발생 : 66세 > 65세
# -> ECLO : 81세 > 85세

#%% 가해운전자 성별 교통사고 현황
sex_table = df_table.groupby('가해운전자 성별')[['사고건수', '사망자수', '중상자수', '경상자수', '부상신고자수']].sum()
sex_table = cal_eclo(sex_table)
print(sex_table)
"""
          사고건수  사망자수  중상자수  경상자수  부상신고자수  ECLO  ECLO/사고건수
가해운전자 성별                                                 
남         1615    15   367  1716     171  7304   4.522601
여          265     1    40   293      27  1116   4.211321
"""

plot_bar(sex_table, '가해운전자 성별')
# -> 사고발생 : 남 > 여
# -> ECLO : 남 > 여

#%% 법규위반별 교통사고 현황
violation_table = df_table.groupby('법규위반')[['사고건수', '사망자수', '중상자수', '경상자수', '부상신고자수']].sum()
violation_table = cal_eclo(violation_table)
print(violation_table)
"""
           사고건수  사망자수  중상자수  경상자수  부상신고자수  ECLO  ECLO/사고건수
법규위반                                                      
교차로운행방법위반   106     0    19   115      22   462   4.358491
기타           66     3    24    61       6   339   5.136364
보행자보호의무위반    51     0    14    39       2   189   3.705882
불법유턴         22     0     6    16       4    82   3.727273
신호위반        262     3    59   303      10  1244   4.748092
안전거리미확보     287     1    37   362      39  1320   4.599303
안전운전불이행     948     7   210   979      92  4149   4.376582
중앙선침범        60     2    27    47      15   311   5.183333
직진우회전진행방해    35     0     9    34       6   153   4.371429
차로위반         43     0     2    53       2   171   3.976744
"""

plot_bar(violation_table, '법규위반')
# -> 사고발생 : 안전운전불이행 > 안전거리미확보
# -> ECLO : 중앙선침범 > 기타

#%% 차종별 교통사고 현황
car_table = df_table.groupby('가해운전자 차종')[['사고건수', '사망자수', '중상자수', '경상자수', '부상신고자수']].sum()
car_table = cal_eclo(car_table)
print(car_table)
"""
             사고건수  사망자수  중상자수  경상자수  부상신고자수  ECLO  ECLO/사고건수
가해운전자 차종                                                    
개인형이동수단(PM)    11     0     1    10       1    36   3.272727
건설기계           19     0     2    20       1    71   3.736842
기타불명            3     0     0     3       0     9   3.000000
농기계             1     0     1     0       0     5   5.000000
사륜오토바이(ATV)     2     0     0     0       2     2   1.000000
승용           1301     8   258  1494     112  5964   4.584166
승합            171     1    46   174      16   778   4.549708
원동기            11     0     4     8       1    45   4.090909
이륜             61     0    19    57      12   278   4.557377
자전거           116     4    38    47      35   406   3.500000
특수              3     0     0     3       0     9   3.000000
화물            181     3    38   193      18   817   4.513812
"""

plot_bar(car_table, '가해운전자 차종')
# -> 사고발생 : 승용 > 화물
# -> ECLO : 농기계 > 승용

#%% 도로형태별 교통사고 현황
road_table = df_table.groupby(['도로형태1','도로형태2'])[['사고건수', '사망자수', '중상자수', '경상자수', '부상신고자수']].sum()
road_table = cal_eclo(road_table)
print(road_table)
"""
                 사고건수  사망자수  중상자수  경상자수  부상신고자수  ECLO  ECLO/사고건수
도로형태1 도로형태2                                                     
교차로   교차로부근       306     2    63   310      27  1292   4.222222
      교차로안        595     5   135   634      72  2699   4.536134
      교차로횡단보도내     96     2    34    64       4   386   4.020833
기타    기타           91     1    11   103       7   381   4.186813
단일로   고가도로위         6     0     6    12       0    66  11.000000
      교량            1     0     0     1       0     3   3.000000
      기타          746     5   146   831      87  3360   4.504021
      지하차도(도로)내    32     1     9    42       0   181   5.656250
      터널            5     0     3    10       1    46   9.200000
주차장   주차장           2     0     0     2       0     6   3.000000
"""

plot_bar(road_table, '도로형태1')
plot_bar(road_table, '도로형태2')
# -> 사고발생 : 단일로 > 교차로 // 단일로(기타) > 교차로(교차로안)
# -> ECLO : 단일로 > 교차로 // 단일로(고가도로위) > 단일로(터널)

#%% 기상상태별 교통사고 현황
weather_table = df_table.groupby('기상상태')[['사고건수', '사망자수', '중상자수', '경상자수', '부상신고자수']].sum()
weather_table = cal_eclo(weather_table)
print(weather_table)
"""
      사고건수  사망자수  중상자수  경상자수  부상신고자수  ECLO  ECLO/사고건수
기상상태                                                 
기타       6     0     1     8       0    29   4.833333
눈        7     0     1     6       2    25   3.571429
맑음    1684    13   364  1794     180  7512   4.460808
비      119     2    28   133      12   571   4.798319
흐림      64     1    13    68       4   283   4.421875
"""

plot_bar(weather_table, '기상상태')
# -> 사고발생 : 맑음 > 비
# -> ECLO : 기타 > 비

#%% 노면상태별 교통사고 현황
surface_table = df_table.groupby('노면상태')[['사고건수', '사망자수', '중상자수', '경상자수', '부상신고자수']].sum()
surface_table = cal_eclo(surface_table)
print(surface_table)
"""
       사고건수  사망자수  중상자수  경상자수  부상신고자수  ECLO  ECLO/사고건수
노면상태                                                  
건조     1711    14   362  1825     180  7605   4.444769
기타        6     0     1     7       2    28   4.666667
서리/결빙     8     0     3     7       3    39   4.875000
적설        4     0     1     4       0    17   4.250000
젖음/습기   151     2    40   166      13   731   4.841060
"""

plot_bar(surface_table, '노면상태')
# -> 사고발생 : 건조 > 젖음/습기
# -> ECLO : 서리/결빙 > 젖음/습기

#%% 지역별 교통사고 현황
area_table = df_table.groupby(['구','동'])[['사고건수', '사망자수', '중상자수', '경상자수', '부상신고자수']].sum()
area_table = cal_eclo(area_table)
print(area_table)
"""
           사고건수  사망자수  중상자수  경상자수  부상신고자수  ECLO  ECLO/사고건수
구   동                                                     
권선구 고색동      54     0     8    54      12   214   3.962963
    곡반정동     26     0     3    31       2   110   4.230769
    구운동      51     1    15    52      11   252   4.941176
    권선동     108     2    24   119       6   503   4.657407
    금곡동      39     0    11    33       3   157   4.025641
    당수동      13     0     1    17       3    59   4.538462
    대황교동      3     0     2     2       0    16   5.333333
    서둔동      38     0     9    42       9   180   4.736842
    세류동      87     3    30    81       8   431   4.954023
    오목천동     25     2     5    20       9   114   4.560000
    입북동      13     0     4    15       1    66   5.076923
    탑동       29     0     4    34       2   124   4.275862
    평동       28     0     0    50       1   151   5.392857
    평리동       2     0     0     2       0     6   3.000000
    호매실동     43     0     4    52       6   182   4.232558
영통구 망포동      28     0     3    39       1   133   4.750000
    매탄동      64     1    18    56       5   273   4.265625
    신동        7     0     3     5       1    31   4.428571
    영통동      57     1    13    61       4   262   4.596491
    원천동      50     0    13    57       4   240   4.800000
    이의동      71     0     5    90       5   300   4.225352
    하동        7     0     1    10       2    37   5.285714
장안구 송죽동      49     0     8    57       6   217   4.428571
    연무동      49     0    10    46       6   194   3.959184
    영화동     102     1    27    92      10   431   4.225490
    율전동      32     0     3    39       2   134   4.187500
    이목동      17     0     4    17       0    71   4.176471
    정자동     109     1    28   107      15   486   4.458716
    조원동      48     2    13    46       6   229   4.770833
    천천동      27     0    13    27       3   149   5.518519
    파장동      49     0     7    62       6   227   4.632653
    하광교동      5     0     1    12       0    41   8.200000
팔달구 고등동      22     0     2    24       5    87   3.954545
    교동        4     0     0     6       0    18   4.500000
    구천동       5     0     2     4       0    22   4.400000
    남수동       6     0     1     7       1    27   4.500000
    남창동       1     0     0     2       0     6   6.000000
    매교동      20     1     3    20       1    86   4.300000
    매산로1가    69     0     3   102       9   330   4.782609
    매산로2가    18     0     3    13       3    57   3.166667
    매산로3가     9     0     1     8       1    30   3.333333
    매향동       4     0     2     3       0    19   4.750000
    북수동      13     0     7     8       1    60   4.615385
    신풍동       3     0     0     3       0     9   3.000000
    영동        8     0     3     5       1    31   3.875000
    우만동      92     1    18    94       8   390   4.239130
    인계동     106     0    25   122       2   493   4.650943
    장안동       8     0     2     7       0    31   3.875000
    중동       10     0     1    13       1    45   4.500000
    지동       41     0    17    32       5   186   4.536585
    팔달로1가     6     0     2     4       0    22   3.666667
    팔달로2가    15     0     3    16       0    63   4.200000
    팔달로3가    12     0     2    14       2    54   4.500000
    화서동      78     0    20    75       9   334   4.282051
"""

plot_bar(area_table, '구')
plot_bar(area_table, '동')
# -> 사고발생 : 장안구 > 권선구 // 장안구(정자동) > 권선구(권선동)
# -> ECLO : 장안구 > 팔달구     // 장안동(하광교동) > 팔달구(남창동)


len(area_table)                     #Out[95]: 54    