#기본함수

#함수 도움말  help(함수명), ?(함수명)

help(par)   #multiple plot 그리는 함수
help(sum)

# args(함수명)
args(sum)   #인수와 초깃값 알려주는 함수

#sum
sum(1,3,5,7,9)  #25

#NA 가 있으면 연산 결과는 NA(NA는 연산할수 없는 값)
sum(2,4,6,8,NA)   #NA
sum(2,4,6,8,NA,na.rm=T)   #20

#함수예제
#example(함수명)
example(sum)

sum(1:10)         #55
sum(1:5, 7:10)    #49
