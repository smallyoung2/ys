df_raw <- data.frame(var1=c(1,2,1),
                     var2=c(2,3,2))

install.packages("dplyr")
library(dplyr)

df_new <- df_raw
df_raw

df_new <- rename(df_new,v2=var2)
df_new

df_raw

#혼자서 해보기
mpg <- as.data.frame(ggplot2::mpg)

mpg_new <- mpg
mpg_new <- rename(mpg_new,city=cty)
mpg_new
mpg_new <- rename(mpg_new,highway=hwy)
mpg_new

head(mpg_new)
