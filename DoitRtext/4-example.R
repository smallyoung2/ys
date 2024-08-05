# 3. 분석도전
library(readr)
library(dplyr)
library(stringr)
library(textclean)
library(tidytext)
library(KoNLP)
library(ggplot2)
library(tidyr)

raw_news_comment <- read_csv("news_comment_BTS.csv")
glimpse(raw_news_comment)

news_comment <- raw_news_comment %>% 
  mutate(id=row_number(),
         reply=str_squish(replace_html(reply)))
news_comment %>% select(id, reply)

word_comment <- news_comment %>% 
  unnest_tokens(input=reply,
                output=word,
                token="words",
                drop=F)
word_comment %>% select(word)

dic <- read_csv("knu_sentiment_lexicon.csv")

word_comment <- word_comment %>% 
  left_join(dic,by="word") %>% 
  mutate(polarity=ifelse(is.na(polarity),0,polarity))
word_comment %>% 
  select(word,polarity) %>% 
  arrange(-polarity)

score_comment <- word_comment %>% 
  group_by(id,reply) %>% 
  summarise(score=sum(polarity)) %>% 
  ungroup()

score_comment  %>% select(score,reply) %>% 
  arrange(-score)

score_comment <- score_comment %>% 
  mutate(sentiment=ifelse(score>=1,"pos",
                    ifelse(score<=-1,"neg","neu")))
score_comment %>% select(sentiment,reply)

frequency_score <- score_comment %>% 
  count(sentiment)
frequency_score

ggplot(frequency_score,aes(x=sentiment,y=n,fill=sentiment))+
  geom_col()+
  geom_text(aes(label=n),vjust=-0.3)

comment <- score_comment %>% 
  unnest_tokens(input=reply,
                output=word,
                token="words",
                drop=F)

frequency_word <- comment %>% 
  count(sentiment,word,sort=T)
frequency_word

comment_wide <- frequency_word %>% 
  filter(sentiment !="neu") %>% 
  pivot_wider(names_from=sentiment,
              values_from=n,
              values_fill=list(n=0))
comment_wide

comment_wide <- comment_wide %>% 
  mutate(log_odds_ratio=log(((pos+1)/(sum(pos+1)))/
                              ((neg+1)/(sum(neg+1)))))
comment_wide

top10 <- comment_wide %>% 
  group_by(sentiment=ifelse(log_odds_ratio>0,"pos","neg")) %>% 
  slice_max(abs(log_odds_ratio),n=10)
top10

ggplot(top10,aes(x=reorder(word,log_odds_ratio),
                 y=log_odds_ratio,
                 fill+sentiment))+
  geom_col()+
  coord_flip()+
  labs(x=NULL)

score_comment %>% filter(str_detect(reply,"자랑스럽다")) %>% 
  arrange(-score) %>% 
  select(reply)

score_comment %>% filter(str_detect(reply,"국내")) %>% 
  arrange(score) %>% 
  select(reply)
