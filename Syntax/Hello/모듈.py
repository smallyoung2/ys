# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 13:56:03 2024

@author: soyoung
"""

#모듈
#일반적으로 컴퓨터 소프트웨어에서는 기능의 단위
#파이썬에서 함수나 변수, 클래스들을 모아 놓은 파이썬 코드파일

#함수
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
PI=3.141592
#%%
#모듈 테스트
# __name__ :파이썬 시스템 변수
# __name__ ("__main__"): 해당 모듈이 독립적으로 실행
print("[모듈.py] 테스트")
a=10
b=20
print("더하기: ",add(a,b))
print("빼기: ",sub(b,a))



##파일 입출력
#함수: open(), close(), read(), write(), readline(), readlines()
#파일 입출력 순서:
    # 오픈 읽거나쓰기 닫기
#파일의 종류 : 텍스트(ASCII, UTF-8), 바이너리(Binary)
    #텍스트:txt,csv,py,java,c,cpp,xml,html,sql,json
    #바이너리:doc,hwp,xls,pdf,jpg,gif,exe,dll
    
#%%
#텍스트 파일 처리
#파일 객체 얻기: 쓰기용
score_file=open("./score.txt",'w',encoding="utf8")

#문제
#1.국어 영어 수학 과학 점수를 텍스트 파일로 생성
#이름,국어,영어,수학,과학
#홍길동,100,90,80,70
#이순신,100,90,80,70
#강감찬,100,90,80,70

#2.생성된 파일을 읽어서 총점,평균을 구한다
#이름,국어,영어,수학,과학,총점,평균
#홍길동,100,90,80,70,340,85
#이순신,100,90,80,70,340,85
#강감찬,100,90,80,70,340,85

#3.위에서처리한 성적을 새로운 파일에 저장한다
#4.파일이 없는 경우 예외처리를 한다.
#5.해당 코드를 일반함수를 만들어 코딩한다
#6.위 5번의 함수를 클래스로 변경한다.
#7.처리한 파일 이름을 외부에서 임의로 지정하여 처리한다.(p.183참조)
#     -파일(score.txt) 읽어서 성적처리 결과 파일 (score_result.txt) 생성
#     -python score.txt score_result.txt

f=open("score.txt",'w')
data="""이름,국어,영어,수학,과학
홍길동,100,90,80,70
이순신,100,90,80,70
강감찬,100,90,80,70 """
f.write(data)
f.close()

with open("score.txt",'a') as f:
    new_data="""총점,평균"""
    f.write(new_data)

with open("score.txt", 'w') as f:
    data = """이름,국어,영어,수학,과학
홍길동,100,90,80,70
이순신,100,90,80,70
강감찬,100,90,80,70 """
    f.write(data)

# 기존 데이터의 첫 번째 줄을 읽어옵니다.
with open("score.txt", 'r') as f:
    first_line = f.readline().strip()

# 마지막에 "총점,평균"을 추가합니다.
first_line += ",총점,평균\n"

# 파일에 쓰기
with open("score.txt", 'w') as f:
    f.write(first_line)