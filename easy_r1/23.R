# switch 문
# switch(비교문, 실행문 [, 실행문, ...])
# 비교문이 조건에 만족하는 실행문 중 하나를 선택
# 비교문이 가리키는 값에 해당하는 변수의 이름과 일치하는 값을 리턴

a <- 10
b <- 20
c <- 30

a1 <- switch('a', x=100, y=200, a=300)
a1 # 300

b1 <- switch('b', x=100, y=200, a=300)
b1 # NULL

what <- "c"
cx <- switch(what, x=100, y=200, a=300, c=400)
cx # 400

rx = NA
if(what == "c") {
  rx <- 400
}
rx

ry = switch("y", x=c(1,3,5), y=c(2,4,6))
ry

# which 문
# 특정 데이터를 선택
# 조건식에 만족하는 결과가 참인 위치를 리턴

no <- seq(10,50,10)
no
name <- c("홍", "이", "박", "최", "김")
score <- seq(60,100,10)

exam <- data.frame(학번=no, 이름=name, 성적=score)
exam

exam$이름
kim <- which(exam$이름 == '김')
kim # 5
exam[kim,]         # 50   김  100
exam[kim,c(1,2,3)] # 50   김  100
