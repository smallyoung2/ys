#
# [데이터 유형과 구조]
# 1. vector: 1차원 배열
# 2. matrix: 2차원 배열
# 3. array: 다차원 배열
# 4. data frame: 2차원 테이블 구조
# 5. list: 자료 구조 중첩

# vector :1차원 배열, 같은 자료형, 참자(index)는 1부터 시작,
#          시작, 종료 인덱스 포함(시작:종료)

#combine valule
c1 <- c(1,2,3,4,5)  #num.. = double(실수)
c2 <- c(1:5)        #integer(정수)
cn <- c(1L,2L,3L,4L,5L) # L:Long -> integer

is.double(c1)   #TRUE
is.double(c2)   #FALSE
is.integer(c2)  #TRUE
is.integer(cn)  #TRUE

#sequence value
#seq(시작값, 종료값, 증가값)
s1 <- seq(1,10,1)   # 1부터 10까지 1의 간격으로 출력
s2 <- seq(1,10,2)   # 1,3,5,7,9
s3 <- seq(2,10,2)
s0 <- seq(1,10)     # 증가값 없으면 default 값 =1

#replicate value : 반복
#rep(값, 반복횟수)
r1 <- rep(3,5)      # 3을 다섯번 출력 3,3,3,3,3 (num)
r2 <- rep(2:6,2)    # 2부터 6가지 2번 출력 2,3,4,5,6,2,3,4,5,6 (int)

r3 <- rep(c('a','b','c'),3)   # a,b,c,a,b,c,a,b,c

r4 <- rep(1:3,3)
r5 <- rep(c(1:3),3)
r6 <- rep(c(1,2,3),3)         # r4,r5,r6 결과 동일(r4,r5: int, r6: num(double))

r7 <- rep(seq(2,8,2),2)       # 2,4,6,8,2,4,6,8

#
cr1 <- c(rep(seq(2,8,2),2),10)  # 2,4,6,8,2,4,6,8,10

# 위 최종 결과를 분해
cx1 <- seq(2,8,2)
cx2 <- rep(cx1,2)
cx3 <- c(cx2,10)
