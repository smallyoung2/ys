# 조건문 : if, switch, which
# if: 참과 거짓인 경우 처리를 분기
# if(조건문) {
#   명령문
# }
?cat

a <- 30
b <- 20
c <- 0

# a가 b보다 크면 블록 안에 명령문을 실행
if(a > b) {
  cat('a는 b보다 크다')
  c <- a + b
}

cat('c=', c) # 50

# 조건문 : if, switch, which
# if: 참과 거짓인 경우 처리를 분기
# if(조건문) {
#   명령문
# } else {
#   명령문
#}

a <- 10
b <- 20
c <- 0

# a가 b보다 크면 블록 안에 명령문을 실행
if(a > b) {
  cat('a는 b보다 크다')
  c <- a + b
} else { # 위의 if 조건이 만족하지 않으면 실행: FALSE 이면, a가 b보다 작거나 같으면 실행
  cat('a는 b보다 크지 않다')
  c <- b - a
}


cat('c=', c) # 10