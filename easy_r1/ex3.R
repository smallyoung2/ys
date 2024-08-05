# 연습문제

# [문제3]
# 벡터 1부터 12까지 12개 요소로 구성된 
# 3행 * 2열 * 2면의 array 만들고 아래의 계산을 하라.
# 각면의 행의 합계
# 각면의 열의 합계
# 각면의 총합
# 각면의 총합

cx <- c(1:12)       # 벡터
cl <- c(3,2,2)      # 차원: 3행 * 2열 * 2면
ar <- array(cx, cl) # 배열
ar

# 면 참조
a1 <- ar[,,1] # 1면
a2 <- ar[,,2] # 2면

# 각면의 행의 합계
apply(a1, MARGIN=1, sum) # 1면의 행의 합계:  5 7 9
apply(a2, MARGIN=1, sum) # 2면의 행의 합계:  17 19 21

# 각면의 열의 합계
apply(a1, MARGIN=2, sum) # 1면의 행의 합계:  6 15
apply(a2, MARGIN=2, sum) # 2면의 행의 합계:  24 33

# 각면의 총합: 행기준
sum(apply(a1, MARGIN=1, sum)) # 1면의 총합: 5 7 9 -> 21
sum(apply(a2, MARGIN=1, sum)) # 2면의 총합: 17 19 21 -> 57

# 각면의 총합: 열기준
sum(apply(a1, MARGIN=2, sum)) # 1면의 총합: 6 15 -> 21
sum(apply(a2, MARGIN=2, sum)) # 2면의 총합: 24 33 -> 57