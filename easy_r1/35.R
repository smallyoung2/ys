# 문자열 처리 라이브러리

help(strsplit)

# [문제]
# 해당 문자열에서 '-' 문자를 '.'로 변경시켜라

data <- "010-1234-5678"

# 문자열 -> 문자벡터
vdata <- unlist(strsplit(data, ''))
vdata # "0" "1" "0" "-" "1" "2" "3" "4" "-" "5" "6" "7" "8"

ldata <- length(vdata)
ldata # 13

for(n in seq(1, ldata)) {
  if(vdata[n] == '-') {
    vdata[n] = '.'
  }
}

vdata # "0" "1" "0" "." "1" "2" "3" "4" "." "5" "6" "7" "8"
vdata <- paste(vdata, collapse = '') # 벡터를 문자열로 변환
vdata
class(vdata)
