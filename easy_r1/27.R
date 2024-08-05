# while 문 : 반복문
# next : 다음 명령을 실행하지 않고 다시 조건문으로 돌아감
# break: 반복문을 탈출

# -10부터 10까지 1씩 증가하는 연속적인 숫자가 있다.
# 양의 3배의 배수를 구하라.
cnt <- -10
max <- 10
tot <- 0

while(TRUE) { # 무한루프: 반복문이 끝없이 계속 수행
  cnt <- cnt + 1
  #cat('cnt=', cnt, '\n')
  
  if(cnt > 10) {
    break # 반복문을 탈출(종료)
  }
  
  if(cnt <= 0) { # 음수인 경우 아래 명령문을 처리하지 않음
    next # 다시 반복문의 시작점으로 이동
  }
  
  if(cnt %% 3 == 0) { # 3의 배수
    tot <- tot + cnt
    cat('[3의 배수] cnt=', cnt, ', tot=', tot, '\n', sep='')
  }
} # while(end)

cat("1부터 10까지의 3의 배수의 합?", tot, '\n') # 18

# -10부터 10까지 1씩 증가하는 연속적인 숫자가 있다.
# 양의 3배의 배수를 구하라.
cnt <- -10
max <- 10
tot <- 0

while(TRUE) { # 무한루프: 반복문이 끝없이 계속 수행
  cnt <- cnt + 1
  #cat('cnt=', cnt, '\n')
  
  if(cnt > 10) {
    break # 반복문을 탈출(종료)
  }
  
  if(cnt > 0) { # 양수만 처리
    if(cnt %% 3 == 0) { # 3의 배수
      tot <- tot + cnt
      cat('[3의 배수] cnt=', cnt, ', tot=', tot, '\n', sep='')
    }
  }
} # while(end)

cat("1부터 10까지의 3의 배수의 합?", tot, '\n') # 18

# -10부터 10까지 1씩 증가하는 연속적인 숫자가 있다.
# 양의 3배의 배수를 구하라.
cnt <- -10
max <- 10
tot <- 0

while(TRUE) { # 무한루프: 반복문이 끝없이 계속 수행
  cnt <- cnt + 1
  #cat('cnt=', cnt, '\n')
  
  if(cnt > 10) {
    break # 반복문을 탈출(종료)
  }
  
  if(cnt > 0 & (cnt %% 3 == 0)) { # 양수이면서 3의 배수
    tot <- tot + cnt
    cat('[3의 배수] cnt=', cnt, ', tot=', tot, '\n', sep='')
  }
} # while(end)

cat("1부터 10까지의 3의 배수의 합?", tot, '\n') # 18