#날짜형

now <- "24/02/19"

dt <- as.Date(now,'%y/%m/%d')
dt

mode(dt)  #numeric
class(dt) #date

today <- "2024-03-01"
t1 <- as.Date(today,"%Y-%m-%d")   # %Y :년도 4자리 (대문자입력해야됨)
t1

class(t1)   #date

#시스템 날짜
syst <- Sys.time()    #sys안됨 Sys 으로 대소문자 구별하기
syst          # "2024-02-19 17:14:19 KST"

mode(syst)    # numeric
class(syst)   # "POSIXct" "POSIXt" 

# systm <-  as.POSIXlt(syst,format="%Y/%m/%d %H:%M:%S")
systm <-  as.POSIXlt(syst,format="%Y/%m/%d %H:%M:%S")
systm         # "2024-02-19 17:14:19 KST"

help(strptime)
example("as.POSIXct")

txm <- as.Date(syst,"%Y-%m-%d")
txm


strptime(syst,"%Y-%m-%d %H:%M:%S")
#시스템 날짜
format(Sys.time(), "%Y-%m-%d %H:%M:%S")   #"2024-02-19 17:38:15"

#로케일 확인
Sys.getlocale()
