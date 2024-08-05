# 행렬처리함수
# apply()

?apply()
# apply(X, MARGIN, FUN, ..., simplify = TRUE)
# x:행렬객체
# margin: 1: 행단위, 2: 열단위
# fun: 행렬 자료에 적용할 함수

mx <- matrix(1:12,nrow=3,ncol=4,byrow=F) #열우선
mx

# 행단위로 최대값을 구하라
apply(mx,1,max)   # 10 11 12 
<- 