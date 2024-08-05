# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 17:03:13 2024

@author: soyoung
"""

#1
result=0
for i in range(1000):
    if i%3==0:
        result+=i
    elif i%5==0:
        result+=i
        
print(result)

#2
a=[]
a.append(1)
a.append(2)

for i in range(100):
    a.append(a[i]+a[i+1])
    if a[i]>4000000:
        break

result=0
list=[]
for i in range(len(a)):
    if a[i]%2==0:
        print(result)
        result+=a[i]
        list.append(result)
    else: pass

print(result)
print(list[10])

#5
import math
math.lcm(1,2,3,4,5,6,7,8,9,10)
math.lcm(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)

#6
result1=0
result2=0
for i in range(1,101):
    result1+=i**2
print("제곱의 합",result1)

for i in range(1,101):
    result2+=i
result2=result2**2
print("합의 제곱",result2)

totresult=result2-result1
print("합의 제곱 - 제곱의 합",totresult)

#7
a=[1,]                                      #속도 느림
for i in range(2,99999):
    if sum(i%j==0 for j in range(2,i))==0:
        a.append(i)
print(a)
print(a[10001])

#에라토스테네스의 체 알고리즘
def sieve_of_eratosthenes(limit):
    primes = []                             #소수를 저장할 리스트
    is_prime = [True] * (limit + 1)         #각 숫자가 소수인지 여부 저장 리스트
    is_prime[0] = is_prime[1] = False       #0,1 은소수 아니므로 false

    for number in range(2, int(limit**0.5) + 1):
        if is_prime[number]:
            primes.append(number)           #현재 숫자 소수이면 primes리스트에 추가
            for multiple in range(number * number, limit + 1, number):
                is_prime[multiple] = False
                                            #현재 숫자의 배수들은 false로 소수아님 표시

    for number in range(int(limit**0.5) + 1, limit + 1):
        if is_prime[number]:
            primes.append(number) 
                                            #남은 숫자들중 소수를 primes리스트에 추가
    return primes                           #찾아낸 소수 리스트 반환
primes = sieve_of_eratosthenes(120000)
print(primes[10000])                        #10001번째 소수 출력

#8
data="""7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450 """
datalist=[int (digit) for digit in data if digit.isdigit()]


maximum=0
for i in range(len(datalist)-12):
    maxi=datalist[i]*datalist[i+1]*datalist[i+2]*datalist[i+3]*datalist[i+4]*datalist[i+5]*datalist[i+6]*datalist[i+7]*datalist[i+8]*datalist[i+9]*datalist[i+10]*datalist[i+11]*datalist[i+12]
    maximum=max(maximum,maxi)
print(maximum)

#9
for i in range(1000):
    for j in range(i+1,1000):
        for k in range(j+1,1000):
            if i+j+k==1000:
                if i**2+j**2==k**2:
                    print(i,j,k)
                    print(i*j*k)

#10
def sieve_of_eratosthenes(limit):
    primes = []                             #소수를 저장할 리스트
    is_prime = [True] * (limit + 1)         #각 숫자가 소수인지 여부 저장 리스트
    is_prime[0] = is_prime[1] = False       #0,1 은소수 아니므로 false

    for number in range(2, int(limit**0.5) + 1):
        if is_prime[number]:
            primes.append(number)           #현재 숫자 소수이면 primes리스트에 추가
            for multiple in range(number * number, limit + 1, number):
                is_prime[multiple] = False
                                            #현재 숫자의 배수들은 false로 소수아님 표시

    for number in range(int(limit**0.5) + 1, limit + 1):
        if is_prime[number]:
            primes.append(number) 
                                            #남은 숫자들중 소수를 primes리스트에 추가
    return primes                           #찾아낸 소수 리스트 반환

primes = sieve_of_eratosthenes(2000000)
sum=0
for i in range(len(primes)):
    if primes[i]<=2000000:
        sum+=primes[i]

print(sum)

#11
data="""08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"""
data=data.split("\n")
print(data)                         #20개씩 20개의 인덱스로 줄마다 나눔

numbers=[]
for i in data:
    numbers.append(i.split(" "))
print(numbers)                      #2차원 배열로 만듬 ex) numbers[0][0] =8

maximum1=0                          #가로곱 최대값
for i in range(20):
    for j in range(16):
        a=int(numbers[i][j])*int(numbers[i][j+1])*int(numbers[i][j+2])*int(numbers[i][j+3])
        maximum1=max(maximum1,a)
        
maximum2=0                          #세로곱 최대값
for i in range(16):
    for j in range(20):
        b=int(numbers[i][j])*int(numbers[i+1][j])*int(numbers[i+2][j])*int(numbers[i+3][j])
        maximum2=max(maximum2,b)

maximum3=0                          #오른쪽대각선 곱 최대값
for i in range(16):
    for j in range(16):
        c=int(numbers[i][j])*int(numbers[i+1][j+1])*int(numbers[i+2][j+2])*int(numbers[i+3][j+3])
        maximum3=max(maximum3,c)
        
maximum4=0                          #왼쪽 대각선 곱 최대값
for i in range(16):
    for j in range(3,20):
        d=int(numbers[i][j])*int(numbers[i+1][j-1])*int(numbers[i+2][j-2])*int(numbers[i+3][j-3])
        maximum4=max(maximum4,d)
        
result=max(maximum1,maximum2,maximum3,maximum4)     #maximum4가 가장큼
print(result)

#12
def count_divisors(num):
    # 소인수 분해
    divisors_count = 1
    i = 2
    while i * i <= num:
        count = 0
        while num % i == 0:
            count += 1
            num //= i
        divisors_count *= (count + 1)
        i += 1

    if num > 1:
        divisors_count *= 2

    return divisors_count

def find_triangle_number_with_divisors(divisor_count_limit):
    n = 1
    triangle_number = 1
    while count_divisors(triangle_number) <= divisor_count_limit:
        n += 1
        triangle_number += n

    return triangle_number

# 500개 이상의 약수를 갖는 가장 작은 삼각수 구하기
result = find_triangle_number_with_divisors(500)
print(result)

    
#13
data="""37107287533902102798797998220837590246510135740250
46376937677490009712648124896970078050417018260538
74324986199524741059474233309513058123726617309629
91942213363574161572522430563301811072406154908250
23067588207539346171171980310421047513778063246676
89261670696623633820136378418383684178734361726757
28112879812849979408065481931592621691275889832738
44274228917432520321923589422876796487670272189318
47451445736001306439091167216856844588711603153276
70386486105843025439939619828917593665686757934951
62176457141856560629502157223196586755079324193331
64906352462741904929101432445813822663347944758178
92575867718337217661963751590579239728245598838407
58203565325359399008402633568948830189458628227828
80181199384826282014278194139940567587151170094390
35398664372827112653829987240784473053190104293586
86515506006295864861532075273371959191420517255829
71693888707715466499115593487603532921714970056938
54370070576826684624621495650076471787294438377604
53282654108756828443191190634694037855217779295145
36123272525000296071075082563815656710885258350721
45876576172410976447339110607218265236877223636045
17423706905851860660448207621209813287860733969412
81142660418086830619328460811191061556940512689692
51934325451728388641918047049293215058642563049483
62467221648435076201727918039944693004732956340691
15732444386908125794514089057706229429197107928209
55037687525678773091862540744969844508330393682126
18336384825330154686196124348767681297534375946515
80386287592878490201521685554828717201219257766954
78182833757993103614740356856449095527097864797581
16726320100436897842553539920931837441497806860984
48403098129077791799088218795327364475675590848030
87086987551392711854517078544161852424320693150332
59959406895756536782107074926966537676326235447210
69793950679652694742597709739166693763042633987085
41052684708299085211399427365734116182760315001271
65378607361501080857009149939512557028198746004375
35829035317434717326932123578154982629742552737307
94953759765105305946966067683156574377167401875275
88902802571733229619176668713819931811048770190271
25267680276078003013678680992525463401061632866526
36270218540497705585629946580636237993140746255962
24074486908231174977792365466257246923322810917141
91430288197103288597806669760892938638285025333403
34413065578016127815921815005561868836468420090470
23053081172816430487623791969842487255036638784583
11487696932154902810424020138335124462181441773470
63783299490636259666498587618221225225512486764533
67720186971698544312419572409913959008952310058822
95548255300263520781532296796249481641953868218774
76085327132285723110424803456124867697064507995236
37774242535411291684276865538926205024910326572967
23701913275725675285653248258265463092207058596522
29798860272258331913126375147341994889534765745501
18495701454879288984856827726077713721403798879715
38298203783031473527721580348144513491373226651381
34829543829199918180278916522431027392251122869539
40957953066405232632538044100059654939159879593635
29746152185502371307642255121183693803580388584903
41698116222072977186158236678424689157993532961922
62467957194401269043877107275048102390895523597457
23189706772547915061505504953922979530901129967519
86188088225875314529584099251203829009407770775672
11306739708304724483816533873502340845647058077308
82959174767140363198008187129011875491310547126581
97623331044818386269515456334926366572897563400500
42846280183517070527831839425882145521227251250327
55121603546981200581762165212827652751691296897789
32238195734329339946437501907836945765883352399886
75506164965184775180738168837861091527357929701337
62177842752192623401942399639168044983993173312731
32924185707147349566916674687634660915035914677504
99518671430235219628894890102423325116913619626622
73267460800591547471830798392868535206946944540724
76841822524674417161514036427982273348055556214818
97142617910342598647204516893989422179826088076852
87783646182799346313767754307809363333018982642090
10848802521674670883215120185883543223812876952786
71329612474782464538636993009049310363619763878039
62184073572399794223406235393808339651327408011116
66627891981488087797941876876144230030984490851411
60661826293682836764744779239180335110989069790714
85786944089552990653640447425576083659976645795096
66024396409905389607120198219976047599490197230297
64913982680032973156037120041377903785566085089252
16730939319872750275468906903707539413042652315011
94809377245048795150954100921645863754710598436791
78639167021187492431995700641917969777599028300699
15368713711936614952811305876380278410754449733078
40789923115535562561142322423255033685442488917353
44889911501440648020369068063960672322193204149535
41503128880339536053299340368006977710650566631954
81234880673210146739058568557934581403627822703280
82616570773948327592232845941706525094512325230608
22918802058777319719839450180888072429661980811197
77158542502016545090413245809786882778948721859617
72107838435069186155435662884062257473692284509516
20849603980134001723930671666823555245252804609722
53503534226472524250874054075591789781264330331690"""
data=data.split("\n")

for i in range(100):
    data[i]=int(data[i])

sum=0
for i in range(100):
    sum+=data[i]

sum_str=str(sum)
print(sum_str[:10])


#14

totalcount = 0
count = [0] * 1000000

for i in range(2, 1000000):
    current_count = 0
    temp_i = i
    
    while temp_i != 1:
        if temp_i % 2 == 0:
            temp_i = temp_i // 2
        elif temp_i % 2 == 1 and temp_i != 1:
            temp_i = 3 * temp_i + 1
        current_count += 1

    count[i] = current_count
    totalcount = max(totalcount, current_count)
    if totalcount==524:
        print(i)
        break

print(i)
print(totalcount)


#16
def pow1(num):
    result=0
    result+=2**num
    return result

data1=(pow1(1000))
data1_str=str(data1)
sum=0

for i in data1_str:
    sum+=int(i)
    
    
#20
result=1
for i in range(1,101):
    result*=i
print(result)

result_str=str(result)
sum=0
for i in result_str:
    sum+=int(i)
    
print(sum)

#24
import itertools
count=1
permutation=list(itertools.permutations(['0','1','2','3','4','5','6','7','8','9'],10))
count_permu=len(permutation)
result=''.join(permutation[999999])


#25
a=[1,1]
for i in range(1000000):
    a.append(a[i]+a[i+1])
    if len(str(a[i+1])) >=1000:
        break
    
print(i+2)                    #i는 0일때 i+2의 값이 생성되므로 


a = [1, 1]
i = 2

while True:
    current_term = a[i - 1] + a[i - 2]
    a.append(current_term)
    i += 1
    if len(str(current_term)) >= 1000:
        break
    
    


#26

def find_recurring_cycle_length(d):
    # remainders 리스트는 현재까지 계산한 나머지를 저장
    remainders = []
    remainder = 1 % d

    # 나머지가 이전에 나온 적이 없을 때까지 반복
    while remainder not in remainders:
        remainders.append(remainder)
        remainder = (remainder * 10) % d

    # 순환마디 길이는 remainders 리스트의 길이에서 첫 번째로 등장한 나머지의 인덱스를 뺀 값
    return len(remainders) - remainders.index(remainder)


def find_longest_recurring_cycle(limit):
    max_length = 0
    result = 0

    # 2부터 limit까지의 분모에 대해 반복
    for d in range(2, limit + 1):
        # 현재 분모에 대한 순환마디의 길이를 계산
        cycle_length = find_recurring_cycle_length(d)

        # 최대 길이와 해당 분모를 업데이트
        if cycle_length > max_length:
            max_length = cycle_length
            result = d
    # 가장 긴 순환마디를 갖는 분모를 반환
    return result


# 분모가 1000 이하인 경우를 대상으로 함수를 호출하고 결과를 출력합니다.
limit = 1000
answer = find_longest_recurring_cycle(limit)
print("가장 긴 순환마디를 갖는 분모:", answer)




#28
result=1
data=1

for i in range(1,501):
    for j in range(1,5):
        data+=2*i
        print(2*i+1,"*",j,"=",i*j)
        print("Data",data)
        result+=data
        print("result",result)
        
print(result)
       

#29
a=[]
alldata=[]
for i in range(2,101):
    for j in range(2,101):
        current_value=i**j
        alldata.append(i**j)
        if current_value not in a:
            a.append(current_value)
print(len(a))          


#30
data=[]
for i in range(1000,10000000):
    a=i//10000000
    b=i//1000000-a*10
    c=i//100000-a*100-b*10
    d=i//10000-a*1000-b*100-c*10
    e=i//1000-a*10000-b*1000-c*100-d*10
    f=i//100-a*100000-b*10000-c*1000-d*100-e*10
    g=i//10-a*1000000-b*100000-c*10000-d*1000-e*100-f*10
    h=i-a*10000000-b*1000000-c*100000-d*10000-e*1000-f*100-g*10
    if i==a**5+b**5+c**5+d**5+e**5+f**5+g**5+h**5:
        data.append(i)

print(sum(data))        
    

data=[]
for i in range(1000,10000):
    a=i//1000
    b=i//100-a*10
    c=i//10-a*100-b*10
    d=i-a*1000-b*100-c*10
    if i==a**4+b**4+c**4+d**4:
        data.append(i)
print(sum(data))        


#31
# 아래코드: 로딩 시간이 오래걸린다.
count=0

for a in range(2):
    for b in range(3):
        for c in range(5):
            for d in range(11):
                for e in range(51):
                    for f in range(21):
                        for g in range(101):
                            for h in range(201):
                                total=a*200+b*100+c*50+d*20+e*10+f*5+g*2+h
                                if total==200:
                                    count+=1
    
                
print(count)


def count_coin_combinations(target_amount, coin_values):
    # dp[i]는 금액 i를 만들기 위한 동전의 조합 수를 나타냅니다.
    dp = [0] * (target_amount + 1)
    dp[0] = 1  # 금액 0을 만드는 방법은 1가지 (아무 동전도 사용하지 않는 경우)

    for coin in coin_values:
        for amount in range(coin, target_amount + 1):
            dp[amount] += dp[amount - coin]

    return dp[target_amount]

# 동전의 종류와 목표 금액을 설정합니다.
coin_values = [1, 2, 5, 10, 20, 50, 100, 200]
target_amount = 200

# 함수를 호출하여 서로 다른 방법으로 2파운드를 만드는 경우의 수를 구합니다.
result = count_coin_combinations(target_amount, coin_values)

print("2파운드를 만드는 서로 다른 방법의 수:", result)



#34

import math
def calculate_factorial(n):
    return sum([math.factorial(int(digit))for digit in str(n)])


total_sum=0
for i in range(3,1000000):
    if calculate_factorial(i)==i:
        total_sum+=i
print(total_sum)       
        
        
#35
#에라토스테네스의 체 알고리즘
def sieve_of_eratosthenes(limit):
    primes = []                             #소수를 저장할 리스트
    is_prime = [True] * (limit + 1)         #각 숫자가 소수인지 여부 저장 리스트
    is_prime[0] = is_prime[1] = False       #0,1 은소수 아니므로 false

    for number in range(2, int(limit**0.5) + 1):
        if is_prime[number]:
            primes.append(number)           #현재 숫자 소수이면 primes리스트에 추가
            for multiple in range(number * number, limit + 1, number):
                is_prime[multiple] = False
                                            #현재 숫자의 배수들은 false로 소수아님 표시

    for number in range(int(limit**0.5) + 1, limit + 1):
        if is_prime[number]:
            primes.append(number) 
                                            #남은 숫자들중 소수를 primes리스트에 추가
    return primes                           #찾아낸 소수 리스트 반환
primes = sieve_of_eratosthenes(1000000)
print(primes[10000])                        #10001번째 소수 출력





def is_prime(num):
    # 주어진 수가 소수인지 확인하는 함수
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def circular_prime_count(limit):
    # 원형 소수 개수를 찾는 함수
    circular_primes = []

    for i in range(2, limit):
        if is_prime(i):
            str_i = str(i)
            # 현재 소수를 순환시켜서 모두 소수인지 확인
            is_circular_prime = all(is_prime(int(str_i[j:] + str_i[:j])) for j in range(len(str_i)))
            
            if is_circular_prime:
                circular_primes.append(i)

    return len(circular_primes)

# 주어진 범위 내에서 원형 소수 개수를 계산
limit = 1000000
result = circular_prime_count(limit)

print(f"{limit} 미만의 원형 소수 개수:", result)