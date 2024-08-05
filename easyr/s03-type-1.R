#자료형
#숫자형(Numeric): 0, 1234, -1234
#문자형(String) : "a", "abc", "ABC"
#논리형(Logiccal): TRUE, FALSE, T, F

#결측 : NA(Not a Available), NaN(Not a Number)
#무한값 : Inf, NULL

#숫자형
n <- 22
is.numeric(n) 

#문자형
#문자열 안에 포함된 따옴표는 데이터 간주한다

s1 <- "홍길동"  #큰따옴표
s2 <- '홍사덕'  #작은따옴표
s3 <- "홍길동은 '홍사덕'의 조상이다."
s4 <- '홍사덕은 "홍길동"의 후손이다.'
is.character(s1)
is.character(s2)
is.character(s3)
is.character(s4)

#논리형
t1 <- TRUE
t2 <- T
t3 <- FALSE
t4 <- F
is.logical(t1)
is.logical(t2)
is.logical(t3)
is.logical(t4)
