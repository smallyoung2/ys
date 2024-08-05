# 문자열 처리

# 패키지 제거
remove.packages("stringr")

# 패키지 설치
install.packages("stringr")

# 사용 : 메모리로 로딩
library(stringr)

# 문자열의 길이
# 스칼라형으로 전체 문자열 단위를 하나 본다.
s1 <- "Hello, World."
s1_len <- length(s1) 
s1_len # 1L

# 문자열에서 논리적인 문자로 구성된 길이
sl <- str_length(s1)
sl # 13

# 
# 한글, 숫자, 공백
# 특수문자: '\n'은 한 개의 문자로 처리
shn <- "한글 12345\n"
shl <- str_length(shn)
shl # 9: 한글(2) + 공백(1) + 숫자(5) + 특수문자(1)

# 문자열 내에서 특정 문자열의 위치
sp1 <- "일이삼사오육칠팔구십"
l10 <- str_locate(sp1, "육")
l10 # 6 6

l38 <- str_locate(sp1, "삼사오육칠팔")
l38 # start:3, end:8
#      start end
# [1,]     3   8

class(l38) # "matrix" "array" 

l38[1,1] # 시작위치: 3
l38[1,2] # 종료위치: 8

# 
l3 <- str_locate(sp1, "삼")
l8 <- str_locate(sp1, "팔구")
l3 # 3 3
l8 # 8 9

# 부분 문자열 만들기
# help(str_sub)
# str_sub(string, start = 1L, end = -1L)
s39 <- str_sub(sp1, l3[1,1], l8[1,2])
s39 # "삼사오육칠팔구"

# [문제]
# 이메일: abc@ysit.ac.kr, admin@ysit.ac.kr
# 위 이메일 주소에서 아이디와 주소를 분리 추출하라.
# 조건: 다양한 이메일 주소를 처리 가능하도록 하라.
# 아이디: abc
# 주소: ysis.ac.kr
# email <- "abc@ysit.ac.kr"
email <- "admin@ysit.ac.kr"
eloc <- str_locate(email, '@')    # 구분문자('@')의 위치
el <- str_length(email)           # 이메일의 전체 길이
es <- eloc[1,1]                   # 구분자의 시작 위치
ee <- eloc[1,2]                   # 구분자의 종료 위치
eid <- str_sub(email, 1, es - 1)  # 아이디 추출
eha <- str_sub(email, ee + 1, el) # 주소 추출
eid
eha

# 대문자로 변환
# 문자열을 대문자로 변환하여 결과를 리턴, 원본은 변경되지 않는다.
EMAIL <- str_to_upper(email) 
EMAIL # "ADMIN@YSIT.AC.KR"
email

# 소문자로 변환
small <- str_to_lower(EMAIL)
small
