# matrix :2차원 배열구조
# 행렬자료 구조의 특징
# 동일한 자료형 데이터만 저장
# 함수: matrix(), rbind(), cbind(), apply()

mx <- matrix(c(1:6))
mx

# nrow :행의 갯수
m23 <- matrix(c(1:6),nrow=2)    # 2행 3열
m23
m32 <- matrix(c(1:6),nrow=3)    # 3행 2열
m32

#배수가 맞지 않으면?
#처음 시작값부터 반복
m42 <- matrix(c(1:6),nrow=4)
m42    #  1    5
      #   2    6
      #   3    1
      #   4    2

# 4행 5열 :20개
cv <- c(1:18,30,40)
cv
m45 <- matrix(cv,nrow=4)
m45
