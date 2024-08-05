df <- data.frame(var1=c(4,3,8),
                 var2=c(2,6,1))
df

df$var_sum <- df$var1+df$var2
df
df$var_mean <- df$var_sum/2
df

mpg <- as.data.frame(ggplot2::mpg)

mpg$total <- (mpg$cty+mpg$hwy)/2
head(mpg)

mean(mpg$total)
summary(mpg$total)
hist(mpg$total)

mpg$test <- ifelse(mpg$total>=20,"pass","fail")
head(mpg,20)

table(mpg$test)   #fail 106 pass  128 

library(ggplot2)

qplot(mpg$test)

#total을 기준으로 A,B,C 등급 부여
mpg$grade <- ifelse(mpg$total>=30,"A",ifelse(mpg$total>=20,"B","C"))
head(mpg,20)

table(mpg$grade)    # A  10   B 118   C 106 

qplot(mpg$grade)

# A,B,C,D 등급 부여
mpg$grade2 <- ifelse(mpg$total>=30,"A",
                     ifelse(mpg$total>=25,"B",
                            ifelse(mpg$total>=20,"C","D")))
table(mpg$grade2)
qplot(mpg$grade2)

## 분석도전
#1
midwest <- as.data.frame(ggplot2::midwest)
library(dplyr)
library(ggplot2)

head(midwest)
tail(midwest)
View(midwest)
dim(midwest)  # 437행 28열
str(midwest)
summary(midwest)

#2
midwest <- rename(midwest, total=poptotal)
midwest <- rename(midwest, asian=popasian)
head(midwest,3)

#3
midwest$perasian <- (midwest$asian /midwest$total)*100
head(midwest,2)

hist(midwest$perasian)

#4
midwest$mean_perasian <- mean(midwest$perasian)
summary(midwest$perasian)
mean(midwest$perasian)

midwest$test <- ifelse(midwest$perasian>0.4872462,"Large","small")

#5
table(midwest$test)
qplot(midwest$test)
