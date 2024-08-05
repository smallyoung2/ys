# 연습문제

# [문제]
# 벡터(vector) 1부터 n까지의 연속된 숫자의
# 홀수의 합과 짝수의 합을 각각 구하라.

n <- 10        # 벡터 n개
s <- 1         # 시작값
v <- c(s:n)    # 벡터
l <- length(v) # 벡터의 길이


# 홀수의 합
odd <- seq(s, l, 2) # 1 3 5 7 9
os <- sum(v[seq(s,l,2)]) # 25
sum(seq(s,l,2))    # 25
sum(odd)

# 짝수의 합
even <- seq(s+1, l, 2)     # 2  4  6  8 10
es <- sum(v[even]) # 30
sum(even)    # 30

# 총합 = 홀수의 합 + 짝수의 합
ss <- os + es
ss # 55