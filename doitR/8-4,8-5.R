#8-4
ggplot(data=economics, aes(x=date, y=unemploy))+ geom_line()

#혼자서 해보기
ggplot(data=economics, aes(x=date, y= psavert))+ geom_line()

#8-5
ggplot(data=mpg, aes(x=drv, y=hwy))+ geom_boxplot()

#혼자서 해보기
class_mpg <- mpg %>% filter(class%in% c("compact","subcompact","suv")) 

ggplot(data=class_mpg, aes(x=class, y=cty))+ geom_boxplot()
