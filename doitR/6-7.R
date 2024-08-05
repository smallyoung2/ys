test1 <- data.frame(id=c(1,2,3,4,5),
                    midterm=c(60,80,70,90,85))
test2 <- data.frame(id=c(1,2,3,4,5),
                    final=c(70,83,65,95,80))
test1
test2

total <- left_join(test1,test2,by="id")
total

name <- data.frame(class=c(1,2,3,4,5),
                   teacher=c("kim","lee","park","choi","jung"))
name

exam_new <- left_join(exam,name,by="class")
exam_new

group_a <- data.frame(id=c(1,2,3,4,5),
                      test=c(60,80,70,90,85))
group_b <- data.frame(id=c(6,7,8,9,10),
                      test=c(70,83,65,95,80))
group_a
group_b

group_all <- bind_rows(group_a,group_b)
group_all

# 혼자서해보기
fuel <- data.frame(fl=c("c","d","e","p","r"),
                   price_fl=c(2.45,2.38,2.11,2.76,2.22))
fuel

mpg <- as.data.frame(ggplot2::mpg)
#1
mpg <- left_join(mpg, fuel, by= "fl")
mpg

#2
mpg %>% select(model,fl,price_fl) %>% 
  head(5)

# 분석도전
#1
midwest <- as.data.frame(ggplot2::midwest)

midwest <- midwest %>% 
  mutate(percent=(poptotal-popadults)/poptotal*100)

midwest
#2
 midwest %>% 
  arrange(desc(percent)) %>% 
  select(county,percent) %>% 
  head(5)
midwest
#3
midwest <- midwest %>% 
  mutate(test= ifelse (percent>=40,"large",ifelse (percent>=30,"middle","small")))
midwest
table(midwest$test)

#4
midwest %>% 
  mutate(ratio_asian=popasian/poptotal*100) %>% 
  arrange(ratio_asian) %>% 
  select(state,county,ratio_asian) %>% 
  head(10)

