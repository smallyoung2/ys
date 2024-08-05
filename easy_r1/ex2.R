# 연습문제

# [문제2]
# 1부터 16까지 벡터 값을 Matrix 4행 4열 생성하라.
# 행 단위로 각 행의 최대값 구하기 
# 열단위로 각 열의 최대값 구하기 
# 행 단위 합계
# 열 단위 합계
# 행 단위 평균
# 열 단위 평균

# 4행 4열의 메트릭스
mx <- matrix(c(1:16), nrow=4, ncol=4)
mx

# 요소의 수
length(mx) # 16
nrow(mx)   # 4행
ncol(mx)   # 4열

# 행 단위로 각 행의 최대값 구하기 
apply(mx, MARGIN=1, max) # 13 14 15 16

# 열단위로 각 열의 최대값 구하기 
apply(mx, MARGIN=2, max) #  4  8 12 16

# 행 단위 합계
apply(mx, MARGIN=1, sum) # 28 32 36 40

# 열 단위 합계
apply(mx, MARGIN=2, sum) # 10 26 42 58

# 행 단위 평균
apply(mx, MARGIN=1, mean) #  7  8  9 10

# 열 단위 평균
apply(mx, MARGIN=2, mean) # 2.5  6.5 10.5 14.5