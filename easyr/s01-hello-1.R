# 주석
# 현재 라인실행 ctrl + enter
# 설치된 패키지 
available.packages()
dim(available.packages())
# 20406 행 17 열 로 구성됨

# R session 보기
sessionInfo()

#패키지 설치
install.packages("stringr")

#패키지 로딩 :사용
library("stringr")

#현재 로드된 패키지 확인
search()

#패키지 제거
remove.packages("stringr")
