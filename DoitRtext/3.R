# 3-1
library(dplyr)
raw_moon <- readLines("speech_moon.txt", encoding="UTF-8")
moon <- raw_moon %>% 
  as_tibble() %>% 
  mutate(president="moon")
raw_park <- readLines("speech_park.txt", encoding="UTF-8")
park <- raw_park %>% 
  as_tibble() %>% 
  mutate(president="park")

bind_speeches <- bind_rows(moon, park) %>% 
  select(president, value)
head(bind_speeches)
tail(bind_speeches)

library(stringr)
speeches <- bind_speeches %>% 
  mutate(value=str_replace_all(value,"[^가-힣]"," "),
         value=str_squish(value))
speeches

library(tidytext)
library(KoNLP)
speeches <- speeches %>% 
  unnest_tokens(input=value,
                output=word,
                token=extractNoun)
speeches

# df <- tibble(class=c("a","a","a","b","b","b"),
#              sex=c("female","male","female","male","male","female"))
# df
# df %>% count(class,sex)

frequency <- speeches %>% 
  count(president,word) %>% 
  filter(str_count(word)>1)
head(frequency)

# df <- tibble(x=c(1:100))
# df
# df %>% slice_max(x,n=3)

top10 <- frequency %>% 
  group_by(president) %>% 
  slice_max(n,n=10)
top10

top10 %>% filter(president=="park")

# df <- tibble(x=c("A","B","C","D"),y=c(4,3,2,2))
# df %>% slice_max(y,n=3)
# df %>% slice_max(y,n=3,with_ties=F)

top10 <- frequency %>% 
  group_by(president) %>% 
  slice_max(n,n=10,with_ties=F)
top10

library(ggplot2)
ggplot(top10,aes(x=reorder(word,n),y=n,fill=president))+
  geom_col()+
  coord_flip()+
  facet_wrap(~ president,
             scales="free_y")

top10 <- frequency %>% 
  filter(word!="국민") %>% 
  group_by(president) %>% 
  slice_max(n,n=10,with_ties=F)
top10

ggplot(top10, aes(x=reorder(word,n),y=n,fill=president))+
  geom_col()+
  coord_flip()+
  facet_wrap(~ president, scales= "free_y")
ggplot(top10,aes(x=reorder_within(word,n,president),
                 y=n,fill=president))+
  geom_col()+
  coord_flip()+
  facet_wrap(~ president, scales="free_y")+
  scale_x_reordered()+
  labs(x=NULL)



# 3-2
df_long <- frequency %>% 
  group_by(president) %>% 
  slice_max(n,n=10) %>% 
  filter(word %in% c("국민","우리","정치","행복"))
df_long

install.packages("tidyr")
library(tidyr)

df_wide <- df_long %>% 
  pivot_wider(names_from=president,
              values_from=n,
              values_fill=list(n=0))
df_wide

frequency_wide <- frequency %>% 
  pivot_wider(names_from=president,
              values_from=n,
              values_fill=list(n=0))
frequency_wide

frequency_wide <- frequency_wide %>% 
  mutate(ratio_moon=((moon+1)/(sum(moon+1))),
         ratio_park=((park+1)/(sum(park+1))),
         odds_ratio=ratio_moon/ratio_park)
frequency_wide %>% arrange(-odds_ratio)
frequency_wide %>% arrange(odds_ratio)

top10 <- frequency_wide %>% 
  filter(rank(odds_ratio)<=10 |rank(-odds_ratio)<=10)
top10 %>% arrange(-odds_ratio)

# df <- tibble(x=c(2,5,10))
# df %>% mutate(y=rank(x))
# df %>% mutate(y=rank(-x))

top10 <- top10 %>% 
  mutate(president=ifelse(odds_ratio>1, "moon","park"),
         n=ifelse(odds_ratio>1,moon,park))
top10

ggplot(top10,aes(x=reorder_within(word,n,president),
                 y=n,fill=president))+
  geom_col()+
  coord_flip()+
  facet_wrap(~ president, scales="free_y")+
  scale_x_reordered()

ggplot(top10,aes(x=reorder_within(word,n,president),
                 y=n,fill=president))+
  geom_col()+
  coord_flip()+
  facet_wrap(~ president, scales="free")+
  scale_x_reordered()+
  labs(x=NULL)

speeches_sentence <- bind_speeches %>% 
  as_tibble() %>% 
  unnest_tokens(input=value,
                output=sentence,
                token="sentences")
head(speeches_sentence)
tail(speeches_sentence)

speeches_sentence %>% 
  filter(president=="moon"&str_detect(sentence,"복지국가"))

speeches_sentence %>% 
  filter(president=="park"&str_detect(sentence,"행복"))

frequency_wide %>% 
  arrange(abs(1-odds_ratio)) %>% 
  head(10)

frequency_wide %>% 
  filter(moon>=5 &park>=5) %>% 
  arrange(abs(1-odds_ratio)) %>% 
  head(10)



# 3-3
frequency_wide <- frequency_wide %>% 
  mutate(log_odds_ratio=log(odds_ratio))

frequency_wide %>% 
  arrange(-log_odds_ratio)

frequency_wide %>% 
  arrange(log_odds_ratio)

frequency_wide %>% 
  arrange(abs(log_odds_ratio))

frequency_wide <- frequency_wide %>% 
  mutate(log_odds_ratio=log(((moon+1)/(sum(moon+1)))/
                              ((park+1)/(sum(park+1)))))

top10 <- frequency_wide %>% 
  group_by(president=ifelse(log_odds_ratio>0,"moon","park")) %>% 
  slice_max(abs(log_odds_ratio), n=10,with_ties=F)

top10 %>% 
  arrange(-log_odds_ratio) %>%
  select(word,log_odds_ratio,president)

ggplot(top10,aes(x=reorder(word,log_odds_ratio),
                 y=log_odds_ratio,
                 fill=president))+
  geom_col()+
  coord_flip()+
  labs(x=NULL)


# 3-4
install.packages("readr")
library(readr)

raw_speeches <- read_csv("speeches_presidents.csv")
raw_speeches

speeches <- raw_speeches %>% 
  mutate(value=str_replace_all(value,"[^가-힣]"," "),
         value=str_squish(value))
speeches <- speeches %>% 
  unnest_tokens(input=value,
                output=word,
                token=extractNoun)
frequency <- speeches %>% 
  count(president,word) %>% 
  filter(str_count(word)>1)
frequency

frequency <- frequency %>% 
  bind_tf_idf(term=word,
              document=president,
              n=n) %>% 
  arrange(-tf_idf)
frequency

frequency %>% filter(president=="문재인")

frequency %>% filter(president=="문재인") %>% 
  arrange(tf_idf)

top10 <- frequency %>% 
  group_by(president) %>% 
  slice_max(tf_idf,n=10,with_ties=F)

top10$president <- factor(top10$president,
                          levels=c("문재인","박근혜","이명박","노무현"))


ggplot(top10,aes(x=reorder_within(word,tf_idf,president),
                 y=tf_idf,
                 fill=president))+
  geom_col()+
  coord_flip()+
  facet_wrap(~ president,scales="free",ncol=2)+
  scale_x_reordered()+
  labs(x=NULL)


# 분석도전
library(dplyr)
library(stringr)
library(tidytext)
library(KoNLP)
library(tidyr)
library(ggplot2)
# 1
q1_speeches <- read_csv("speeches_presidents.csv")
q1_speeches

q1 <- q1_speeches %>% filter(president==c("이명박","노무현"))%>% 
      mutate(value=str_replace_all(value,"[^가-힣]"," "),
              value=str_squish(value))
q1 <- q1 %>% 
  unnest_tokens(input=value,
                output=word,
                token=extractNoun)
freq <- q1 %>% 
  count(president,word) %>% 
  filter(str_count(word)>1)

freq_wide <- freq %>% 
  pivot_wider(names_from=president,
              values_from=n,
              values_fill=list(n=0))
freq_wide <- freq_wide %>%
  mutate(log_odds_ratio=log(((이명박+1)/(sum(이명박+1)))/
                              ((노무현+1)/(sum(노무현+1)))))
freq_wide
top10 <- freq_wide %>% 
  group_by(president=ifelse(log_odds_ratio>0,"lee","roh")) %>% 
  slice_max(abs(log_odds_ratio),n=10,with_ties=F)
top10

ggplot(top10,aes(x=reorder(word,log_odds_ratio),
                 y=log_odds_ratio,
                 fill=president))+
  geom_col()+
  coord_flip()+
  labs(x=NULL)


# 2
raw_speeches <- read_csv("inaugural_address.csv")

speeches <- raw_speeches %>% 
  mutate(value=str_replace_all(value,"[^가-힣]"," "),
         value=str_squish(value))

speeches  <- speeches %>% 
  unnest_tokens(input=value,
                output=word,
                token=extractNoun)

frequency <- speeches %>% 
  count(president,word) %>% 
  filter(str_count(word)>1)

frequency <- frequency %>% 
  bind_tf_idf(term=word,
              document=president,
              n=n) %>% 
  arrange(-tf_idf)

top10 <- frequency %>% 
  group_by(president) %>% 
  slice_max(tf_idf,n=10,with_ties=F)

ggplot(top10,aes(x=reorder_within(word,tf_idf,president),
                 y=tf_idf,
                 fill=president))+
  geom_col(show.legend=F)+
  coord_flip()+
  facet_wrap(~ president, scales="free",ncol=2)+
  scale_x_reordered()+
  labs(x=NULL)
