#벡터
#문자벡터 : letters

#알파벳 소문자 벡터 :
# "a" "b" "c" "d" ---

ap <- letters
ap
ap[1]   #"a" "b" "c" "d" "e" "f" "g" "h" "i" "j" "k" "l" "m" "n" "o" "p" "q" "r" "s" "t" 
        # "u" "v" "w" "x" "y" "z"
ap[26]

ace <- ap[c(1,3,5)]
ace
ace[1]
ace[2]
ace[3]

#벡터에 원소를 추가
#빈공간은 NA로 채워진다
# 값 없는 인덱스에 값지정하면 추가, 값 있는 인덱스에 값지정하면 수정
ace[10] <- 'z'
ace       # "a" "c" "e" NA  NA  NA  NA  NA  NA  "z"

# NA로 채워진 빈공간을 삭제
ace <- ace[-c(4:9)]
ace       # "a" "c" "e" "z"

#요소를 수정
ace[1] <- 'A'
ace       # "A" "c" "e" "z"

