#15-1
exam <- read.csv("csv_exam.csv")

exam[]
exam[1,]
exam[,1]
exam[exam$class==1,]
exam[exam$math>=80,]

exam[,"class"]
exam[,c("class","math","english")]

#혼자서 해보기
mpg <- as.data.frame(ggplot2::mpg)

mpg$tot <- (mpg$cty+mpg$hwy)/2
df_comp <- mpg[mpg$class=="compact",]
df_suv <- mpg[mpg$class=="suv",]

mean(df_comp$tot)
mean(df_suv$tot)

#15-2 혼자서 해보기
class(mpg$drv)

mpg$drv <- as.factor(mpg$drv)
class(mpg$drv)

levels(mpg$drv)
