#ggplot2 패키지 설치
install.packages("ggplot2")
library(ggplot2)

x <- c("a","a","b","c")
x

qplot(x)

qplot(data=mpg,x=hwy)
qplot(data=mpg,x=cty)
qplot(data=mpg,x=drv,y=hwy)
qplot(data=mpg,x=drv,y=hwy,geom="line")
qplot(data=mpg,x=drv,y=hwy,geom="boxplot")
qplot(data=mpg,x=drv,y=hwy,geom="boxplot",colour=drv)

?qplot

#혼자서 해보기
data=c(80,60,70,50,90)
data
mean_data <- mean(data)
mean_data
