# -10부터 10까지 1씩 증가하는 연속적인 숫자가 있다.
# 양의 3배의 배수를 구하라.
cnt <- -10
max <- 10
tot <- 0

while(FALSE) { # 조건이 거짓(FALSE)이면 루프에 진입하지 못함
  cnt <- cnt + 1
  cat('cnt=', cnt, '\n')
  
  if(cnt > 10) {
    break # 반복문을 탈출(종료)
  }
  
  if(cnt > 0 & (cnt %% 3 == 0)) { # 양수이면서 3의 배수
    tot <- tot + cnt
    cat('[3의 배수] cnt=', cnt, ', tot=', tot, '\n', sep='')
  }
} # while(end)

cat("1부터 10까지의 3의 배수의 합?", tot, '\n') # 18