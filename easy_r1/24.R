# for 문 : 반복문
#
# 처리순서:
#   1. 벡터의 원소를 하나씩 꺼내서 변수에 입력
#   2. 명령문을 실행
#   3. 다시 1번의 과정을 반복
#   4. 벡터에서 원소를 모두 꺼낼 때 까지 반복
#   *. 벡터의 갯수만큼 반복
#
# for(변수 in 벡터) {
#   명령문
# }

# 벡터(1,2,3,4,5)를 하나씩 꺼내서 변수(n)에 대입
# cat() 명령어로 콘솔창에 출력을 5번 반복
for(n in c(1:5)) { # 1,2,3,4,5
  cat('n=', n, '\n')
}

# 1부터 10까지의 합을 구하라
t <- 0
for(n in c(1:10)) { # n: 1, 2, 3,  4,  5  6,   7,  8,  9, 10
  t <- t + n        # t: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55
  print(t)
}

cat('1부터 10까지의 합은', t)

# [문제1]
# 1부터 10까지의 연속된 수에서 홀수의 합을 구하라?
# 1,2,3,4,5,6,7,8,9,10
t1 <- 0
for(n in c(1:10)) {
  if(n %% 2 == 1) { # 나머지가 1인 경우는 홀수
    t1 <- t1 + n
  }
}
cat("1부터 10까지의 홀수의 합은?", t1, '\n')

# [문제2]
# 1부터 10까지의 연속된 수에서 짝수의 합을 구하라?
# 1,2,3,4,5,6,7,8,9,10
t2 <- 0
for(n in 1:10) {
  if(n %% 2 == 0) { # 나머지가 0인 경우는 짝수
    t2 <- t2 + n
  }
}
cat("1부터 10까지의 짝수의 합은?", t2, '\n')

# [문제3]
# 1부터 10까지의 수에서 홀수의 합을 구하라?
# 1,3,5,7,9
t3 <- 0
for(n in seq(1,10,2)) {
  t3 <- t3 + n
}
cat("1부터 10까지의 수에서 홀수의 합을 구하라?", t3, '\n')
cat("1부터 10까지의 수에서 홀수의 합을 구하라?", sum(seq(1,10,2)), '\n')


# [문제4]
# 1부터 10까지의 수에서 짝수의 합을 구하라?
# 2,4,6,8,10
t4 <- 0
for(n in seq(2,10,2)) {
  t4 <- t4 + n
}
cat("1부터 10까지의 수에서 짝수의 합을 구하라?", t4, '\n')
cat("1부터 10까지의 수에서 짝수의 합을 구하라?", sum(seq(2,10,2)), '\n')