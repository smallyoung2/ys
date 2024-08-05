library(dplyr)
exam <- read.csv("csv_exam.csv")
exam

exam %>% filter(class==1)
exam %>% filter(class==2)

exam %>% filter(class!=1)
exam %>% filter(class!=3)

exam %>% filter(math>50)
exam %>% filter(math<50)
exam %>% filter(english>=80)
exam %>% filter(english<=80)

exam %>% filter(class==1 & math>=50)
exam %>% filter(class==2 & english>=80)

exam %>% filter(math>=90 | english>=90)
exam %>% filter(english<90|science<50)

exam %>% filter(class==1|class==3|class==5)
exam %>% filter(class %in% c(1,3,5))

class1 <- exam %>% filter(class==1)
class2 <- exam %>% filter(class==2)

mean(class1$math)
mean(class2$math)

#혼자서 해보기
#1
mpg <- as.data.frame(ggplot2::mpg)
displ4 <- mpg %>% filter(displ<=4)
displ5 <- mpg %>% filter(displ>=5)

mean(displ4$hwy)
mean(displ5$hwy)

#2
manu_audi <- mpg %>% filter(manufacturer=="audi")
manu_toyota <- mpg %>% filter(manufacturer=="toyota")

mean(manu_audi$cty)
mean(manu_toyota$cty)

#3
manu_che <- mpg %>% filter(manufacturer=="chevrolet")
manu_ford <- mpg %>% filter(manufacturer=="ford")
manu_honda <- mpg %>% filter(manufacturer=="honda")

manu_che
manu_ford
manu_honda

exam %>% filter(class %in% c(1,3,5))

manu_triple <- mpg %>% filter(manufacturer %in% c("chevrolet","ford","honda"))
mean(manu_triple$hwy)
