# ifelse(조건, 참, 거짓)

scores <- seq(50,100, 10)
scores # 50  60  70  80  90 100

exam <- ifelse(scores >= 80, '합격', '불합격')
exam #  "불합격" "불합격" "불합격" "합격"   "합격"   "합격" 

score <- scores[3]
score # 70

pass <- ifelse(score >= 70, '합격', '불합격')
pass # "합격"

fails <- ifelse(scores < 60, '불합격', '합격')
fails # "불합격" "합격"   "합격"   "합격"   "합격"   "합격"

# ifelse(조건, 참, 거짓)

scores <- c(NA, seq(50,100, 10), NA, 99, -10)
scores # NA  50  60  70  80  90 100  NA  99 -10

# 결측치 처리: NA -> 0 
# 이상치 처리: 음수 -> 0
scores <- ifelse(is.na(scores) | scores < 0, 0, scores)
scores

