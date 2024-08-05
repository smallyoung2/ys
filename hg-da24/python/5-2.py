# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 11:52:29 2024

@author: soyoung
"""

#5-2선그래프와 막대그래프 그리기
#연도별 발행도서 개수 구하기

import gdown
gdown.download('https://bit.ly/3pK7iuu','ns_book7.csv', quiet=False)

import pandas as pd
ns_book7=pd.read_csv('ns_book7.csv',low_memory=False)
ns_book7.head()

count_by_year=ns_book7['발행년도'].value_counts()
count_by_year

count_by_year=count_by_year.sort_index()
count_by_year

count_by_year=count_by_year[count_by_year.index<=2030]
count_by_year


#주제별 도서개수 구하기
# 앞자리 숫자에따라 분류가능 ex) 1로시작하면 철학, 2로시작하면 종교
# nan 값은 -1로 분류함

import numpy as np

def kdc_1st_char(no):
    if no is np.nan:
        return -1
    else:
        return no[0]
    
count_by_subject=ns_book7['주제분류번호'].apply(kdc_1st_char).value_counts()
count_by_subject


#선그래프 그리기
import matplotlib.pyplot as plt
plt.rcParams['figure.dpi']=100          #해상도를 높이기위하여 기본 dpi 100으로 설정

#연도별 발행도서의 추세
plt.plot(count_by_year.index, count_by_year.values)
plt.title('books by year')
plt.xlabel('year')
plt.ylabel('number of books')
plt.show()

plt.plot(count_by_year, marker='.',linestyle=':',color='red')
plt.title('books by year')
plt.xlabel('year')
plt.ylabel('number of books')
plt.show()

plt.plot(count_by_year,'.:r')       #줄여서 marker ., linestyle :, color red  '.:r'

plt.plot(count_by_year,'*-g')       #marker *, linestyle -, color green
plt.title('books by year')
plt.xlabel('year')
plt.ylabel('number of books')
plt.show()


plt.plot(count_by_year,'*-g')       
plt.title('books by year')
plt.xlabel('year')
plt.ylabel('number of books')
plt.xticks(range(1945,2030,10))             #x축이 1945~2030까지 10개로 나누어서 출력
for idx,val in count_by_year[::5].items():  #슬라이스 연산자의 5개마다  ,,스텝옵션
    plt.annotate(val,(idx,val))   #val:그래프에 나타낼문자열,(idx,val):텍스트가 나타날 x,y좌표
plt.show()


plt.plot(count_by_year,'*-g')       
plt.title('books by year')
plt.xlabel('year')
plt.ylabel('number of books')
plt.xticks(range(1945,2030,10))             
for idx,val in count_by_year[::5].items():  
    plt.annotate(val,(idx,val),xytext=(idx+3,val+10))  #xytext x축으로 3이동,y축으로 10이동
plt.show()

plt.plot(count_by_year,'*-g')       
plt.title('books by year')
plt.xlabel('year')
plt.ylabel('number of books')
plt.xticks(range(1945,2030,10))             
for idx,val in count_by_year[::5].items():  
    plt.annotate(val,(idx,val),xytext=(2,2),textcoords='offset points')     #상대위치
plt.show()



#막대그래프 그리기
count_by_subject.index = [str(idx) for idx in count_by_subject.index]#x축이 숫자여서 문자열로 변환

plt.bar(count_by_subject.index, count_by_subject.values)
plt.title('books by subject')
plt.xlabel('subject')
plt.ylabel('number of books')
for idx,val in count_by_subject.items():
    plt.annotate(val,(idx,val),xytext=(0,2),textcoords='offset points')
plt.show()

#막대의 두께 width=0.7조절 color='blue'
#텍스트 사이즈 8, 위치ha='center', color='green'
plt.bar(count_by_subject.index, count_by_subject.values,width=0.7,color='blue')
plt.title('books by subject')
plt.xlabel('subject')
plt.ylabel('number of books')
for idx,val in count_by_subject.items():
    plt.annotate(val,(idx,val),xytext=(0,2),textcoords='offset points',fontsize=8,ha='center',color='green')
plt.show()

#가로막대그래프 그리기 
#width->height, (inx,val)->(val,idx)  ha->va
plt.barh(count_by_subject.index, count_by_subject.values,height=0.7,color='blue')
plt.title('books by subject')
plt.xlabel('subject')
plt.ylabel('number of books')
for idx,val in count_by_subject.items():
    plt.annotate(val,(val,idx),xytext=(2,0),textcoords='offset points',fontsize=8,va='center',color='green')
plt.show()



#맷플롯립으로 선그래프와 막대그래프 그리기
#좀더알아보기1. 이미지 출력하고 저장하기
#좀더알아보기2. 그래프를 이미지로 저장하기

plt.rcParams['savefig.dpi']

plt.barh(count_by_subject.index, count_by_subject.values,height=0.7,color='blue')
plt.title('books by subject')
plt.xlabel('subject')
plt.ylabel('number of books')
for idx,val in count_by_subject.items():
    plt.annotate(val,(val,idx),xytext=(2,0),textcoords='offset points',fontsize=8,va='center',color='green')
plt.savefig('books_by_subject.png')
plt.show()

from PIL import Image
pil_img=Image.open('books_by_subject.png') #저장한 파일 불러오기

plt.figure(figsize=(8,6))
plt.imshow(pil_img)
plt.axis('off')
plt.show()

