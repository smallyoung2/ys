#파일 입출력

#read.table()
#칼럼 : 공백,탭, 콜론(:),세미콜론(;),콤마 등으로 구분된 자료를 파일에서 읽음
#옵션: header=T or F , sep=''

#파일이 존재하지 않으면 에러
#파일 'student.txt' 를 여는데 실패했습니다.: No such file or directory
student <- read.table(file="./student.txt")
student

# txt에서 커서를 마지막에 두지 않으면 아래와 같은 오류 발생
#'./student.txt'에서 readTableHeader에 의하여 발견된 완성되지 않은 마지막 라인입니다

student <- edit(student)
student

#파일 저장
#row.names :행이름 지정 유무, TRUE, FALSE
#col.names :열이름 지정 유무, TRUE, FALSE
?write.table
write.table(student,"./student_wt.txt", row.names=F, col.names=F)
