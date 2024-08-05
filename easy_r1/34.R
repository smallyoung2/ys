# 문자열 처리 라이브러리

# 패키지 설치
install.packages("stringr")

# 패키지 제거
#remove.packages("stringr")

# 사용 : 메모리로 로딩
 library(stringr)

# 문자열 교체
# help(str_replace)
# str_replace(string, pattern, replacement)
#str_replace(문자열, 교체대상문자열, 새로운문자열)
sid <- "980120-1234567"
sid

# 처음 만나는 문자열('-')를 새로운 문자열('.')으로 교체
xid <- str_replace(sid, '-', '.')
xid

# 전화번호
tel <- "010-1234-5678"

# 처음 만나는 문자열만 변경 됨
str_replace(tel, '-', '.') # "010.1234-5678"

# 전체 문자열을 대상으로 교체
str_replace_all(tel, '-', '.') # "010.1234.5678"

# 문자열 결합
# str_c(...)
# str_c(..., sep = "", collapse = NULL)
help(str_c)
t1 <- '010'
t2 <- '1234'
t3 <- '5678'
tel <- str_c(t1, '-', t2, '-', t3)

# 문자열 분할 : 결과는 리스트(list)
telx <- str_split(tel, '-')
telx # "010"  "1234" "5678"
class(telx)  # "list"
telx[[1]]    # "010"  "1234" "5678"
telx[[1]][1] # "010"
telx[[1]][2] # "1234"
telx[[1]][3] # "5678"

# 분할 함수 str_split()의 결과 list형을 벡터 변환
# telv <- unlist(telx)
telv <- unlist(str_split(tel, '-'))
telv # 
class(telv) # "character"
telv[1] # "010"
telv[2] # "1234"
telv[3] # "5678"

# 벡터를 문자열로 결합
telp <- paste(telv, collapse='.')
telp

# [문제]
# 문자열: "010-1234-5678", "123456-7654321"
# 위 문자열 예시처럼 데이터가 문자('-')으로 n개로 연결되어 있다.
# str_c() 함수를 사용하여 임의의 새로운 연결문자('.')로 결합하라.
# 단, paste() 함수를 사용하지 않고
# str_c(문자열, 연결문자)와 같이 사용하여 해결하라.

# [해결방안1]
data <- "010-1234-5678-9090"
# data <- "123456-7654321"
vdata <- unlist(str_split(data, '-'))
vdata # "010"  "1234" "5678"

ldata <- length(vdata)
ldata # 3
vdata[1] # "010"
vdata[2] # "1234"
vdata[3] # "5678

xdata <- vdata[1]   # "010"
# for(n in seq(2, ldata)) {
for(n in 2:ldata) {
  cat(xdata, '\n')
  xdata <- str_c(xdata, '.')
  xdata <- str_c(xdata, vdata[n])
}
xdata # "010.1234.5678"