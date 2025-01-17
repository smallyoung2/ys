# matrix
# 참조
# 
# 3행 4열

mx <- matrix(1:12,3,byrow=T)  #행우선 값 지정
mx
# 
# 행 전체 선택: 열 인덱스 생략
# 매트릭스[행, ]
mx[1,]  #1행만출력
mx[2,]

# 열 전체 선택 : 행 인덱스 생략
mx[,1]  # 1 5 9
mx[,2]  # 2 6 10
 
# 열범위
# 2행의 2열부터 4열까지
mx[2,c(2:4)]

# 특정한 행열을 선택
# 매트릭스[행,열]
mx[2,4]
mx[3,4]
