# 함수정의
calc <- function(a, b, c) {
  d <- (a - b) * c
  return(d)
}

# 순서대로 인자가 전달
calc(10, 20, 4) # -40 <- (10 - 20) * 4

# 권고하지 않음
calc(c=4, 10, 20) # -40

# 가능하면 순서를 맞춰서 호출
calc(10, 20, c=4)     # -40
calc(a=10, b=20, c=4) # -40


# 함수정의
calc <- function(a, b) {
  d <- (a - b)
  return(d)
}

# 에러: 사용되지 않은 인자 (4)
# 함수(calc)는 인자를 2개 받을 수 있도록 정의 되어 있으므로
# 인자의 갯수가 일치하지 않으면 에러가 발생
calc(10, 20, 4) 