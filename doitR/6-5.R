exam <- read_excel("excel_exam.xlsx")

exam %>% mutate(total=math+english+science) %>% 
  head

exam %>% mutate(total=math+english+science,
                mean=(math+english+science)/3) %>% 
  head

exam %>% 
  mutate(test=ifelse(science>=60,"pass","fail")) %>% 
  head

exam %>% 
  mutate(total=math+english+science) %>% 
  arrange(total) %>% 
  head

#혼자서 해보기
#1
mpg <- as.data.frame(ggplot2::mpg)

mpg_new <- mpg %>% mutate(total=hwy+cty)
mpg_new

#2
mpg_new <- mpg_new %>% mutate(mean=total/2)

#3
mpg_new %>% arrange(desc(mean)) %>% head(3)

#4
mpg %>% mutate(total=hwy+cty,
               mean=(hwy+cty)/2) %>% 
  arrange(desc(mean)) %>% 
  head(3)
