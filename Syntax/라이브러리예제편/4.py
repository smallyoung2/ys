# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 17:08:26 2024

@author: soyoung
"""

#17 math.gcd
import math
math.gcd(60,100,80)

60/20,100/20,80/20

#18 math.lcm
import math
math.lcm(15,25)

#19 decimal.Decimal
0.1*3==0.3          
1.2-0.1==1.1
0.1*0.1==0.01           #3개 모두 오류, 미세한 오차때문에

math.isclose(0.1*3,0.3)
math.isclose(1.2-0.1,1.1)
math.isclose(0.1*0.1,0.01)

from decimal import Decimal
Decimal('0.1')*3
Decimal('1.2')-Decimal('0.1')
Decimal('0.1')*Decimal('0.1')

float(Decimal('1.2')-Decimal('0.1'))==1.1

#20 fractions
1/5+2/5

from fractions import Fraction
a=Fraction(1,5)
a
a=Fraction('1/5')
a

a.numerator
a.denominator

result=Fraction(1,5)+Fraction(2,5)
result
float(result)

#21 random
import random
result=[]
while len(result)<6:
    num=random.randint(1,45)
    if num not in result:
        result.append(num)
print(result)

a=[1,2,3,4,5]
random.shuffle(a)
a
random.choice(a)

#22 statistics

import statistics
marks=[78,93,99,95,51,71,52,43,81,78]
statistics.mean(marks)
statistics.median(marks)
