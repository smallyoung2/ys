# repeat 문 : 무한 반복문

# -10부터 10까지 1씩 증가하는 연속적인 숫자가 있다.
# 양의 3배의 배수를 구하라.
cnt <- -10
max <- 10
tot <- 0

repeat { # 무한반복  
  cnt <- cnt + 1
  # cat('cnt=', cnt, '\n')
  
  # if(cnt > 10) {
  #   break # 반복문을 탈출(종료)
  # }
  
  if(cnt <= 0) {
    next
  }
  
  if(cnt %% 3 == 0) { # 양수이면서 3의 배수
    tot <- tot + cnt
    cat('[3의 배수] cnt=', cnt, ', tot=', tot, '\n', sep='')
  }
} # repeat

cat("1부터 10까지의 3의 배수의 합?", tot, '\n') # 18