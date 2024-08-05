# 산술 연산자

a <- c(0, 2, 4)
b <- c(1, 2, 3)

# 벡터 연산은 같은 인덱스의 요소끼리 연산을 수행하여
# 요소의 갯수 만큼 벡터를 리턴한다.
c <- a + b
c # 1 4 7

d <- a - b
d # -1  0  1

land <- a & b
land # FALSE  TRUE  TRUE

lor<- a | b
lor # TRUE TRUE TRUE