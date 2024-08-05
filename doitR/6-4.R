exam <- read_excel("excel_exam.xlsx")

exam %>% arrange(math)        #math 오름차순
exam %>% arrange(desc(math))  #math 내림차순

exam %>% arrange(class,math)

#혼자서 해보기
mpg <- as.data.frame(ggplot2::mpg)

audi <- mpg %>% filter(manufacturer=="audi")
audi %>% arrange(desc(hwy)) %>% 
  head(5)
