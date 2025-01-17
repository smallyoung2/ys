# while 문 : 반복문

# [문제] 아래의 문제를 while문을 사용하여 처리하라.
n <- 10

# [문제1]
# 1부터 10까지의 연속된 수에서 홀수의 합을 구하라?
# 1,2,3,4,5,6,7,8,9,10
c <- 1
t1 <- 0
while(c <= n) {
  if(c %% 2 == 1) {
    t1 <- t1 + c
  }
  c <- c + 1
}
cat("1부터 10까지의 홀수의 합은?", t1, '\n') # 25

# [문제2]
# 1부터 10까지의 연속된 수에서 짝수의 합을 구하라?
# 1,2,3,4,5,6,7,8,9,10
c <- 1
t2 <- 0
while(c <= n) {
  if(c %% 2 == 0) {
    t2 <- t2 + c
  }
  c <- c + 1
}
cat("1부터 10까지의 짝수의 합은?", t2, '\n') # 30

# [문제3]
# 1부터 10까지의 연속된 수에서 홀수와 짝수의 각각의 합을
# 하나의 반복문(while)으로 구하라?
# 1,2,3,4,5,6,7,8,9,10
c <- 1
t3 <- 0 # 홀수
t4 <- 0 # 짝수
while(c <= n) {
  if(c %% 2 == 1) { # 홀수
    t3 <- t3 + c
  } else { # 짝수
    t4 <- t4 + c
  }
  c <- c + 1
}
cat("1부터 10까지의 홀수의 합은?", t3, '\n') # 25
cat("1부터 10까지의 짝수의 합은?", t4, '\n') # 30
