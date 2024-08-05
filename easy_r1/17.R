# 관계연산자
# 같다: ==
# 같지않다: !=
# 크다: >
# 크거나 같다: >=
# 작다: <
# 작거나 같다: <=
#
# 논리연산자
# 논리곱: &
# 논리합: |
# 논리부정: !

a <- 1
b <- 2
c <- 3

eq <- (a == b)
eq # FALSE

ne <- (a != b)
ne # TRUE

gt <- (a > b)
gt # FALSE

ge <- (a >= b)
ge # FALSE

lt <- (a < b)
lt # TRUE

le <- (a <= b)
le # TRUE

# 논리곱 (&) : A와 B가 참인 경우
ac <- (a != b) & (b != c)
ac # TRUE

# 논리합(|) :A와 B가 둘 중에 하나가 참인 경우
oc <- (a > b) | (b == c)
oc # FALSE

bc <- (a > b) | (b < c)
bc # TRUE

# 논리부정: TRUE <- !FALSE, FALSE <- !TRUE
nf <- !bc
nf # FALSE

nx <- !nf
nx # TRUE

ax <- !(a < b & a < c)
ax # FALSE

n0 <- !0
n0 # TRUE

n1 <- !1
n1 # FALSE

n1 <- !20
n1 # FALSE

az <- 10 < 5
az # FALSE

bz <- FALSE < 5
bz # TRUE