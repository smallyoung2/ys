library(readr)
library(dplyr)
library(stringr)
library(textclean)
library(tidytext)
library(KoNLP)
library(tidyr)

raw_news_comment <- read_csv("news_comment_BTS.csv")
glimpse(raw_news_comment)

news_comment <- raw_news_comment %>% 
  select(reply) %>% 
  mutate(id=row_number(),
         reply=str_replace_all(reply,"[^가-힣]"," "),
         reply=str_squish(reply))
news_comment %>% select(id,reply)

comment_pos <- news_comment %>% 
  unnest_tokens(input=reply,
                output=word,
                token=SimplePos22,
                drop=F)
comment_pos <- comment_pos %>% 
  separate_rows(word,sep="[+]")
comment_pos %>% 
  select(word,reply)

comment <- comment_pos %>% 
  separate_rows(word,sep="[+]") %>% 
  filter(str_detect(word,"/n|/pv|/pa")) %>% 
  mutate(word=ifelse(str_detect(word,"/pv|/pa"),
                     str_replace(word,"/.*$","다"),
                     str_remove(word,"/.*$"))) %>% 
  filter(str_count(word)>=2) %>% 
  arrange(id)

comment %>% select(word,reply)

#3번할차례