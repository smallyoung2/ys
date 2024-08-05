# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 09:28:03 2024

@author: soyoung
"""

#1-3 이도서가 얼마나 인기가 좋을까?

#pip install gdown

import gdown

gdown.download('https://bit.ly/3eecMKZ','남산도서관 장서 대출목록 (2021년 04월).csv',quiet=False)

with open('남산도서관 장서 대출목록 (2021년 04월).csv') as f:
    print(f.readline())

import chardet

with open('./data/남산도서관 장서 대출목록 (2021년 04월).csv', mode='rb') as f:
    d=f.readline()
    
print(chardet.detect(d))
# {'encoding': 'EUC-KR', 'confidence': 0.99, 'language': 'Korean'}

with open('남산도서관 장서 대출목록 (2021년 04월).csv', encoding='euc-kr') as f:
    print(f.readline())
    print(f.readline())
    
import os
import glob
import unicodedata

for filename in glob.glob('*.csv'):
    nfc_filename=unicodedata.normalize('NFC', filename)
    os.rename(filename,nfc_filename)
    
import pandas as pd

df=pd.read_csv('남산도서관 장서 대출목록 (2021년 04월).csv', encoding='euc-kr')

df=pd.read_csv('남산도서관 장서 대출목록 (2021년 04월).csv', encoding='euc-kr',
               low_memory=False)

df.head()

df=pd.read_csv('남산도서관 장서 대출목록 (2021년 04월).csv',encoding='euc-kr',
               dtype={'ISBN':str, '세트 ISBN':str,'주제분류번호':str})

df.head()

df.to_csv('ns_202104.csv')

with open('ns_202104.csv', encoding='utf-8') as f:
    for i in range(3):
        print(f.readline(),end='')
        
ns_df=pd.read_csv('ns_202104.csv',low_memory=False)
ns_df.head()

ns_df=pd.read_csv('ns_202104.csv',index_col=0, low_memory=False)
ns_df.head()

df.to_csv('ns_202104.csv',index=False)

ns_df.to_excel('ns_202104.xlsx',index=False, engine='xlsxwriter')

