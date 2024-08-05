# 1-1
raw_moon <- readLines("speech_moon.txt",encoding="UTF-8")
head(raw_moon)

txt <- "치킨은!! 맛있다. xyz 정말 맛있다!@#"
txt

install.packages("stringr")
library(stringr)
str_replace_all(string=txt, pattern="[^가-힣]", replacement=" ")

moon <- raw_moon %>% 
  str_replace_all("[^가-힣]"," ")
head(moon)

txt <- "치킨은  맛있다  정말 맛있다  "
txt
str_squish(txt)

moon <- moon %>% 
  str_squish()
moon
library(dplyr)
moon <- as_tibble(moon)
moon

moon <- raw_moon %>% str_replace_all("[^가-힣]"," ") %>% 
  str_squish() %>% 
  as_tibble()

# 1-2
text <- tibble(value="대한민국은 민주공화국이다. 대한민국의 주권은 국민에게 있고, 모든권력은 국민으로부터 나온다.")
text

install.packages("tidytext")
library(tidytext)

text %>% unnest_tokens(input=value,
                       output=word,
                       token="sentences")
text %>% unnest_tokens(input=value,
                       output=word,
                       token="words")
text %>% unnest_tokens(input=value,
                       output=word,
                       token="characters")
word_space <- moon %>% 
  unnest_tokens(input=value,
                output=word,
                token="words")
word_space

# 1-3
word_space <- word_space %>% 
  count(word,sort=T)
word_space

str_count("배")
str_count("사과")

word_space <- word_space %>% 
  filter(str_count(word)>1)
word_space

# word_space <- word_space %>% 
#   count(word,sort=T) %>% 
#   filter(str_count(word)>1)
# word_space
top20 <- word_space %>% head(20)
top20

install.packages("ggplot2")
library(ggplot2)

ggplot(top20, aes(x=reorder(word,n),y=n))+
  geom_col()+
  coord_flip()

theme_set(theme_gray(base_family="AppleGothic"))

ggplot(top20, aes(x=reorder(word,n),y=n))+
  geom_col()+
  coord_flip()+
  geom_text(aes(label=n), hjust=-0.3)+
  labs(tilte="문재인 대통령 출마 연설문 단어 빈도",
       x=NULL,y=NULL) +
  theme(title=element_text(size=12))

install.packages("ggwordcloud")
library(ggwordcloud)

ggplot(word_space, aes(label=word, size= n))+
  geom_text_wordcloud(seed=1234)+
  scale_radius(limits=c(3, NA),
               range=c(3,30))
ggplot(word_space, aes(label=word, size= n,col=n))+
  geom_text_wordcloud(seed=1234)+
  scale_radius(limits=c(3, NA),
               range=c(3,30))+
  scale_color_gradient(low="#66aaf2",
                       high="#004EA1")+
  theme_minimal()

install.packages("showtext")
library(showtext)

font_add_google(name="Nanum Gothic", family="nanumgothic")
showtext_auto()

ggplot(word_space, aes(label=word, size= n,col=n))+
  geom_text_wordcloud(seed=1234,
                      family="nanumgothic")+
  scale_radius(limits=c(3, NA),
               range=c(3,30))+
  scale_color_gradient(low="#66aaf2",
                       high="#004EA1")+
  theme_minimal()

ggplot(word_space, aes(label=word, size= n,col=n))+
  geom_text_wordcloud(seed=1234,
                      family="blackhansans")+
  scale_radius(limits=c(3, NA),
               range=c(3,30))+
  scale_color_gradient(low="#66aaf2",
                       high="#004EA1")+
  theme_minimal()

font_add_goole(name="Gamja Flower", family="gamjaflower")
showtext_auto()

ggplot(top20, aes(x=reorder(word,n),y=n))+
  geom_col()+
  coord_flip()+
  geom_text(aes(label=n), hjust=-0.3)+
  labs(tilte="문재인 대통령 출마 연설문 단어 빈도",
       x=NULL,y=NULL) +
  theme(title=element_text(size=12),
        text=element_text(family="gamjaflower"))

# theme_set(theme_gray(base_family="nanumgothic"))

# warnings()
# names(windowsFonts())
# 
# par(family="serif")
# par(family="sans")

#분석도전
raw_park <- readLines("speech_park.txt",encoding="UTF-8")

park <- raw_park %>% 
  str_replace_all("[^가-힣]"," ")
head(park)
park <- park %>% 
  str_squish()
park
park <- as_tibble(park)
moon

park <- park %>% 
  unnest_tokens(input=value,
                output=word,
                token="words")
park

park20 <- park %>% count(word,sort=T) %>% 
  filter(str_count(word)>1) %>% 
  head(20)
park20

library(showtext)
font_add_google(name="Nanum Gothic", family="nanumgothic")
showtext_auto()

library(ggplot2)
ggplot(park20, aes(x=reorder(word,n),y=n))+
  geom_col()+
  coord_flip()+
  geom_text(aes(label=n), hjust=-0.3)+
  labs(x=NULL)+
  theme(text=element_text(family="nanumgothic"))
