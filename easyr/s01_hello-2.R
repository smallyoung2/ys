#데이터 셋 보기
data()

#히스토그램 : 빈도수
# Flow of the River Nile
hist(Nile)

Nile
#히스토그램 : 밀도 F : False
hist(Nile, freq=F)

# 분포곡선(Line)
lines(density(Nile))

hist(Nile,
     col="skyblue",  #color 설정
     main="나일강의 유량")  # 제목 설정
