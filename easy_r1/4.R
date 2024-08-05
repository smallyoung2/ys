#벡터
#합집합, 교집합, 차집합

#합집합 :union()
#양쪽의 모든 데이터가 선택, 중복데이터는 하나만 선택
n <- c(1,3,5,7)
m <- c(3,5,9)
nm <- union(n,m)
nm      # 1 3 5 7 9

#교집합 : intersect()
#양쪽에 동시에 존재하는 데이터만 선택
nxm <- intersect(n,m)
nxm     #  3 5
mxn <- intersect(m,n)
mxn     #  3 5

#차집합 :setdiff(n,m)
#n에는 있고 m 에는 없는 데이터
ndm <- setdiff(n,m)
ndm     #  1 7
mdn <- setdiff(m,n)
mdn     #  9

#n,m 에서 교집합(n,m)을 제외한 데이터
nmc <- c(n,m)     #단순결합(중복허용)
nmc         # 1 3 5 7 3 5 9
nmx <- setdiff(nmc,intersect(n,m))
nmx         # 1 7 9 

#결과 <-차집합(합집합, 교집합)
nm <- union(n,m)  #합집합
nm          # 1 3 5 7 9
nmu <- setdiff(nm,intersect(n,m))
nmu         # 1 7 9
