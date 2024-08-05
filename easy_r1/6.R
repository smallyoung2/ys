#matrix: 2차원 배열구조
#행렬자료 구조의 특징
#동일한 자료형, 데이터만 저장
#생성함수 : matrix(), rbind(), cbind()
#처리함수 : apply()
#행 우선으로 행렬 객체 생성
#행의 값이 채워지고 다음 행으로 이동하여 채움
#byrow : TRUE

#10개 = 2행 5열
m25 <- matrix(c(1:10),nrow=2,byrow=T)   # byrow=T 디폴트
m25

#매트릭스 시퀀스(sequence)을 이용하여 생성
m45 <- matrix(seq(2,20,2),nrow=4,byrow=T)
m45
