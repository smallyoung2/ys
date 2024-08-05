#요인형(Factor)
#같은 성격의 값의 목롤을 범주로 갖는 벡터자료

#[유형]
#norminal(명목): 순서가 없음, 알파벳 순서로 정렬 (성별, 혈액형)
#ordianl(서열): 순서가 있음, 사용자가 지정한 순서 (학점(A,B,C,D),설문조사(매우만족,만족,보통 ..))

#벡터
gender <- c("man","woman","woman","man","man")

#요인형:factor ordinal 
#벡터를 요인형으로 변환
# factor(x, levels, ordered)
norminal_gender <- factor(gender, levels=c("woman","man"),ordered=TRUE)
    # ->  woman 이 1번째, man 이 2번째로 설정함 ( "woman" < "man" )
norminal_gender   #Levels: man woman

#빈도수 : 수치형
table(norminal_gender)  # man 3  woman 2

#빈도수 : 그래프
plot(norminal_gender)

#mode() : 자료형
mode(norminal_gender)   # numeric

#class() : 자료형
class(norminal_gender)  # factor

#차트 그리기
nominal_gender <- as.factor(gender)

par(mfrow=c(1,2))
plot(nominal_gender)
plot(ordinal_gender)
