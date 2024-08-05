exam <- read_excel("excel_exam.xlsx")

exam %>% select(math)
exam %>% select(english)

exam %>% select(class,math,english)
exam %>% select(-math)
exam %>% select(-math,-english)

exam %>% filter(class==1) %>% select(english)
exam %>% 
  filter(class==1) %>% 
  select(english)

exam %>% 
  select(id,math) %>% 
  head

exam %>% 
  select(id,math) %>% 
  head(10)

# 혼자서 해보기
mpg <- as.data.frame(ggplot2::mpg)

#1
mpg_new <- mpg %>% select(class,cty)
mpg_new

#2
cty_suv <- mpg_new %>% filter(class=="suv")
cty_compact <- mpg_new %>% filter(class=="compact")
cty_suv
cty_compact

mean(cty_suv$cty)
mean(cty_compact$cty)
