#2-1
install.packages("multilinguer")
library(multilinguer)
install_jdk()

install.packages("remomtes")
remotes::install_github("haven-jeon/KoNLP",
                        upgrade="never",
                        INSTALL_opts= c("--no-multiarch"))
library(KoNLP)
useNIADic()

library(KoNLP)
library(dplyr)
text <- tibble(value= 
                 c("대한민국은 민주공화국이다.",
               "대한민국의 주권은 국민에게 있고, 모든 권력은 국민으로부터 나온다."))
text

extractNoun(text$value)

library(tidytext)
text %>% unnest_tokens(input=value,
                       output=word,
                       token=extractNoun)
raw_moon <- readLines("speech_moon.txt",encoding="UTF-8")

library(stringr)

moon <- raw_moon %>% 
  str_replace_all("[^가-힣]"," ") %>% 
  str_squish() %>% 
  as_tibble()

word_noun <- moon %>% 
  unnest_tokens(input=value,
                output=word,
                token=extractNoun)
word_noun

# 2-2
word_noun <- word_noun %>% 
  count(word,sort=T) %>% 
  filter(str_count(word)>1)
word_noun

top20 <- word_noun %>%  head(20)
top20

library(ggplot2)
ggplot(top20, aes(x=reorder(word,n), y=n))+
  geom_col()+
  coord_flip()+
  geom_text(aes(label=n), hjust=-0.3)+
  labs(x=NULL)+theme(text=element_text(family="nanumgothic"))

# par(family="serif")
library(showtext)
font_add_google(name="Black Han Sans", family="blackhansans")

library(ggwordcloud)
ggplot(word_noun, aes(label=word,size=n,col=n))+
  geom_text_wordcloud(seed=1234,family="blackhansans")+
  scale_radius(limits=c(3,NA),
               range=c(3,15))+
  scale_color_gradient(low="#66aaf2", high="#004EA1")+
  theme_minimal()

# 2-3
sentences_moon <- raw_moon %>% 
  str_squish() %>% 
  as_tibble() %>% 
  unnest_tokens(input=value,
                output=sentence,
                token="sentences")
sentences_moon

str_detect("치킨은 맛있다","치킨")
str_detect("치킨은 맛있다","피자")

sentences_moon %>% filter(str_detect(sentence,"국민"))
sentences_moon %>% filter(str_detect(sentence,"일자리"))

#분석도전
raw_park <- readLines("speech_park.txt",encoding="UTF-8")

park <- raw_park %>%
  str_replace_all("[^가-힣]", " ") %>%  
  str_squish() %>%                     
  as_tibble()    

noun_park <- park %>% 
  unnest_tokens(input=value,
                output=word,
                token=extractNoun)

park20 <- noun_park %>% 
  count(word,sort=T) %>% 
  filter(str_count(word)>1) %>% 
  head(20)
park20

library(ggplot2)
ggplot(park20, aes(x=reorder(word,n), y=n))+
  geom_col()+
  coord_flip()+
  geom_text(aes(label=n), hjust=-0.3)

sentences_park <- raw_park %>% 
  str_squish() %>% 
  as_tibble() %>% 
  unnest_tokens(input=value,
                output=sentence,
                token="sentences")
sentences_park

sentences_park %>% filter(str_detect(sentence,"경제"))
