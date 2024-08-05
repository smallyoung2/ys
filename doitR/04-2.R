english <- c(90,80,60,70)
english

math <- c(50,60,100,20)
math

df_midterm <- data.frame(english,math)
df_midterm

class <- c(1,1,2,2)
class
df_midterm <- data.frame(english, math, class)
df_midterm

mean(df_midterm$english)
mean(df_midterm$math)

mean(math)

df_midterm <- data.frame(english=c(90,80,60,70),
                         math=c(50,60,100,20),
                         class=c(1,1,2,2))
df_midterm

#혼자서 해보기
data=c("사과","딸기","수박")
price=c(1800,1500,3000)
amount=c(24,38,13)

df <- data.frame(data,price,amount)
df

mean(df$price)
mean(df$amount)
