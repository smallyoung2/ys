class(welfare$religion)
table(welfare$religion)

welfare$religion <- ifelse(welfare$religion==1,"yes","no")
table(welfare$religion)
qplot(welfare$religion)

class(welfare$marriage)
table(welfare$marriage)

welfare$group_marriage <- ifelse(welfare$marriage==1,"marriage",
                             ifelse(welfare$marriage==3, "divorce",NA))
table(welfare$group_marriage)

table(is.na(welfare$group_marriage))
qplot(welfare$group_marriage)

religion_marriage <- welfare %>% 
  filter(!is.na(group_marriage)) %>% 
  group_by(religion,group_marriage) %>% 
  summarise(n=n()) %>% 
  mutate(tot_group=sum(n),
         pct=round(n/tot_group*100,1))
religion_marriage

religion_marriage <- welfare %>% 
  filter(!is.na(group_marriage)) %>% 
  count(religion,group_marriage) %>% 
  group_by(religion) %>% 
  mutate(pct=round(n/sum(n)*100,1))

divorce <- religion_marriage %>% 
  filter(group_marriage=="divorce") %>% 
  select(religion,pct)
divorce

ggplot(data=divorce,aes(x=religion,y=pct))+geom_col()

ageg_marriage <- welfare %>% 
  filter(!is.na(group_marriage)) %>% 
  group_by(ageg,group_marriage) %>% 
  summarise(n=n()) %>% 
  mutate(tot_group=sum(n),
         pct=round(n/tot_group*100,1))
ageg_marriage

ageg_divorce <- ageg_marriage %>% 
  filter(ageg !="young"&group_marriage=="divorce") %>% 
  select(ageg,pct)
ageg_divorce

ggplot(data=ageg_divorce,aes(x=ageg,y=pct))+geom_col()

ageg_religion_marriage <- welfare %>% 
  filter(!is.na(group_marriage)& ageg!="young") %>% 
  group_by(ageg,religion,group_marriage) %>% 
  summarise(n=n()) %>% 
  mutate(tot_group=sum(n),
         pct=round(n/tot_group*100,1))
ageg_religion_marriage

df_divorce <- ageg_religion_marriage %>% 
  filter(group_marriage=="divorce") %>% 
  select(ageg,religion,pct)
df_divorce

ggplot(data=df_divorce,aes(x=ageg,y=pct,fill=religion))+
  geom_col(position="dodge")
