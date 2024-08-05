# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 14:23:54 2024

@author: soyoung
"""

#6-2 맷플롯립의 고급기능 배우기
import matplotlib.pyplot as plt
plt.rcParams['font.family']         #Out[256]: ['Malgun Gothic']
plt.rc('font',family='Malgun Gothic')
plt.rcParams['figure.dpi']=100

import gdown
gdown.download('https://bit.ly/3pK7iuu','ns_book7.csv', quiet=False)

import pandas as pd
ns_book7=pd.read_csv('ns_book7.csv',low_memory=False)
ns_book7.head()

#하나의 피겨에 여러개의 선그래프 그리기
top30_pubs=ns_book7['출판사'].value_counts()[:30]
top30_pubs_idx=ns_book7['출판사'].isin(top30_pubs.index)

#book7에서 상위30개에 해당하는 출판사,발행년도,대출건수열만 추출하여 book9 만들어줌
ns_book9=ns_book7[top30_pubs_idx][['출판사','발행년도','대출건수']]

ns_book9=ns_book9.groupby(by=['출판사','발행년도']).sum() # 출판사,발행년도를 기준으로 대출건수열의 합 구하기
ns_book9=ns_book9.reset_index()             #인덱스 초기화
ns_book9[ns_book9['출판사']=='황금가지'].head()

#선그래프2개 그리기
line1=ns_book9[ns_book9['출판사']=='황금가지']
line2=ns_book9[ns_book9['출판사']=='비룡소']

fig,ax=plt.subplots(figsize=(8,6))
ax.plot(line1['발행년도'],line1['대출건수'])
ax.plot(line2['발행년도'],line2['대출건수'])
ax.set_title('연도별 대출건수')
fig.show()

#범례추가하기(legend메서드), label추가
fig,ax=plt.subplots(figsize=(8,6))
ax.plot(line1['발행년도'],line1['대출건수'],label='황금가지')
ax.plot(line2['발행년도'],line2['대출건수'],label='비룡소')
ax.set_title('연도별 대출건수')
ax.legend()
fig.show()


#선그래프 5개 그리기
fig,ax=plt.subplots(figsize=(8,6))
for pub in top30_pubs.index[:5]:            
    line=ns_book9[ns_book9['출판사']==pub]                 #top30에서 5개 출판사 선택됨
    ax.plot(line['발행년도'],line['대출건수'],label=pub)   #다섯개 출판사에대한 선그래프
ax.set_title('연도별 대출건수')
ax.legend()
ax.set_xlim(1985,2025)          #x축의 범위1985~2025
fig.show()

#y축의 범위도지정하라면
plt.axis([1985,2025,0,13000])   #x축의 범위 1985~2025, y축의 범위 0~13000


#스택영역 그래프: 선그래프위에 다른 선 그래프를 차례로 쌓는 그래프 stackplot()메서드
ns_book10=ns_book9.pivot_table(index='출판사',columns='발행년도')
ns_book10.head()

ns_book10.columns[:10]

top10_pubs=top30_pubs.index[:10] 
year_cols=ns_book10.columns.get_level_values(1)     #('대출건수',1947)에서 인덱스 1인 1947가져오기

fig,ax=plt.subplots(figsize=(8,6))
ax.stackplot(year_cols,ns_book10.loc[top10_pubs].fillna(0),labels=top10_pubs)
ax.set_title('연도별 대출건수')
ax.legend(loc='upper left')         #범례 왼쪽 상단에 표시 (기본값:best..최상의 위치 선택됨)
ax.set_xlim(1985,2025)
fig.show()



#하나의 피겨에 여러개의 막대 그래프 그리기
fig,ax=plt.subplots(figsize=(8,6))
ax.bar(line1['발행년도'],line1['대출건수'],label='황금가지')
ax.bar(line2['발행년도'],line2['대출건수'],label='비룡소')
ax.set_title('연도별 대출건수')
ax.legend()
fig.show()

#+- 0.2: 막대의 위치를 이동시킴, width=0.4: 막대의 너비 지정(기본값0.8->0.4)
fig,ax=plt.subplots(figsize=(8,6))
ax.bar(line1['발행년도']-0.2,line1['대출건수'],width=0.4,label='황금가지')
ax.bar(line2['발행년도']+0.2,line2['대출건수'],width=0.4,label='비룡소')
ax.set_title('연도별 대출건수')
ax.legend()
fig.show()

#스틱막대그래프 bottom 매개변수
height1=[5,4,7,9,8]
height2=[3,2,4,1,2]

plt.bar(range(5),height1,width=0.5)
plt.bar(range(5),height2,bottom=height1,width=0.5) #bottom=height1 height가 끝나는 위치에서 시작
plt.show()

height3=[a+b for a,b in zip(height1,height2)]

plt.bar(range(5),height3,width=0.5)
plt.bar(range(5),height1,width=0.5)
plt.show()

#데이터값 누적하여 그리기
ns_book10.loc[top10_pubs[:5],('대출건수',2013):('대출건수',2020)] #2013~2020 데이터 출력

ns_book10.loc[top10_pubs[:5],('대출건수',2013):('대출건수',2020)].cumsum() #누적됨

ns_book12=ns_book10.loc[top10_pubs].cumsum()        #모든 년도 누적대출건수


fig,ax=plt.subplots(figsize=(8,6))
for i in reversed(range(len(ns_book12))) :          #가장 큰막대부터 그려야하므로reserved
    bar=ns_book12.iloc[i]                   #행 추출
    label=ns_book12.index[i]                #출판사 이름 추출
    ax.bar(year_cols,bar,label=label)
ax.set_title('연도별 대출건수')
ax.legend(loc='upper left')
ax.set_xlim(1985,2025)
fig.show()


#원그래프 그리기 pie()메서드
data=top30_pubs[:10]                #상위 10개 출판사의 도서개수를 선택하여 저장
labels=top30_pubs.index[:10]        #상위 10개 출판사의 인덱스 저장

fig,ax=plt.subplots(figsize=(8,6))
ax.pie(data,labels=labels)
ax.set_title('출판사 도서비율')
fig.show()                      #3시방향부터 반시계방향으로 순서 정해짐,그려짐


plt.pie([10,9],labels=['A제품','B제품'],startangle=90)  #startangle 90으로 지정하여 12시방향부터 그림
plt.title('제품의 매출비율')
plt.show()



fig,ax=plt.subplots(figsize=(8,6))
ax.pie(data,labels=labels,startangle=90,autopct='%.1f%%',explode=[0.1]+[0]*9)
ax.set_title('출판사 도서비율')
fig.show()  


#여러종류의 그래프가 있는 서브플롯 그리기 (2,2)->4개 (3,2)->6개

fig,axes=plt.subplots(2,2,figsize=(20,16))
#산점도
ns_book8=ns_book7[top30_pubs_idx].sample(1000,random_state=42)
sc=axes[0,0].scatter(ns_book8['발행년도'],ns_book8['출판사'],linewidth=0.5,edgecolors='k'\
                     ,alpha=0.3,s=ns_book8['대출건수'],c=ns_book8['대출건수'],cmap='jet')
axes[0,0].set_title('출판사별 발행도서')
fig.colorbar(sc,ax=axes[0,0])

#스택영역 그래프
axes[0,1].stackplot(year_cols,ns_book10.loc[top10_pubs].fillna(0),labels=top10_pubs)
axes[0,1].set_title('연도별 대출건수')
axes[0,1].legend(loc='upper left')
axes[0,1].set_xlim(1985,2025)

#스택막대 그래프
for i in reversed(range(len(ns_book12))):
    bar=ns_book12.iloc[i]
    label=ns_book12.index[i]
    axes[1,0].bar(year_cols,bar,label=label)
axes[1,0].set_title('연도별 대출건수')
axes[1,0].legend(loc='upper left')
axes[1,0].set_xlim(1985,2025)

#원그래프
axes[1,1].pie(data,labels=labels,startangle=90,autopct='%.1f%%',explode=[0.1]+[0]*9)
axes[1,1].set_title('출판사 도서비율')

fig.savefig('all_in_one.png')               #저장하기
fig.show()



#좀더알아보기. 판다스로 여러개의 그래프 그리기 plot.area()메서드

ns_book11=ns_book9.pivot_table(index='발행년도',columns='출판사',values='대출건수')
ns_book11.loc[2000:2005]

import numpy as np
ns_book11=ns_book7[top30_pubs_idx].pivot_table(index='발행년도',columns='출판사',values='대출건수',aggfunc=np.sum)
ns_book11.loc[2000:2005]


fig,ax=plt.subplots(figsize=(8,6))
ns_book11[top10_pubs].plot.area(ax=ax, title='연도별 대출건수',xlim=(1985,2025))
ax.legend(loc='upper left')
fig.show()


fig,ax=plt.subplots(figsize=(8,6))
ns_book11.loc[1985:2025,top10_pubs].plot.bar(ax=ax,title='연도별 대출건수', stacked=True,width=0.8)
ax.legend(loc='upper left')
fig.show()