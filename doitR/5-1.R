exam <- read.csv("csv_exam.csv")

head(exam)
head(exam,10)

tail(exam)
tail(exam,10)

View(exam)

dim(exam)   #  20  5 (20행 5열)

str(exam)

summary(exam)

mpg <- as.data.frame(ggplot2::mpg)

head(mpg)
tail(mpg)
View(mpg)
dim(mpg)  # 234  11 (234행 11열 존재)
str(mpg)  # 속성

?mpg

summary(mpg)
