# 데이터프레임 

# [실습]
# 임의의 데이터프레임을 만들어 apply() 함수를 이용하여 처리

df <- data.frame(x=c(1:5), y=seq(2,10,2), z=letters[1:5])
df
summary(df)

# 모든 행의 컬럼(1,2) 즉 x, y의 요소를 선택
xy <- c(1,2)
df[, c(1,2)]

# x, y의 행 단위
# 합계
apply(df[, c(1,2)], 1, sum)        # 3  6  9 12 15
apply(df[, c(1,2)], MARGIN=1, sum) # 3  6  9 12 15
apply(df[, xy], MARGIN=1, sum)     # 3  6  9 12 15

# 평균
apply(df[, c(1,2)], MARGIN=1, mean) # 1.5 3.0 4.5 6.0 7.5

# x,y의 열 단위
apply(df[, c(1,2)], MARGIN=2, sum)  # 합계: 15 30 
apply(df[, c(1,2)], MARGIN=2, mean) # 평균: 3 6 