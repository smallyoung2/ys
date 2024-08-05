# 문제1
# 벡터 n 개를 만들고 홀수의 합과 짝수의 합을 각각 구하여라
v <- c(1:16)
vsum1=sum(seq(1,16,2))
vsum2=sum(seq(2,16,2))

# 문제2
# 1부터 16까지 벡터 값을 matrix 4행 4열 생성하라
m44=matrix(c(1:16),nrow=4)
m44
# 행 단위로 각 행의 최대값 구하기
apply(m44,1,max)
# 열 단위로 각 열의 최대값 구하기
apply(m44,2,max)
# 행 단위 합계
apply(m44,1,sum)
# 열 단위 합계
apply(m44,2,sum)
# 행 단위 평균
apply(m44,1,mean)
# 열 단위 평균
apply(m44,2,mean)

# 문제3
# 벡터 1부터 12까지 12개 요소로 구성된 3행 2열 2면의 array를 만들고 아래를 계산하라
ex3 <- array(c(1:12),c(3,2,2))
ex3
# 각면의 행의 합계
apply(ex3[, ,1],1,sum)  # 5 7 9
apply(ex3[, ,2],1,sum)  # 17 19 21
# 각면의 열의 합계# 각면의 열의sum 합계
apply(ex3[, ,1],2,sum)  # 6 15
apply(ex3[, ,2],2,sum)  # 24 33
