data = ['a','b','c']

# pick one and another in list, 
# the number of all cases consider the order

from itertools import permutations


result_1 = list(permutations(data,2))
print(result_1)

# [('a', 'b'), ('a', 'c'), ('b', 'a'), 
# ('b', 'c'), ('c', 'a'), ('c', 'b')]

###############################################

# pick one and another in list, 
# the number of all cases doesn't care the order

from itertools import combinations

result_2 = list(combinations(data, 2))
print(result_2)

# [('a', 'b'), ('a', 'c'), ('b', 'c')]

###############################################

# pick one and can pick the same thing in list
# the number of all cases consider the order

from itertools import product

result_3 = list(product(data, repeat=2))
print(result_3)

# ('a', 'a'), ('a', 'b'), ('a', 'c'), ('b', 'a'), 
# ('b', 'b'), ('b', 'c'), ('c', 'a'), ('c', 'b'), ('c', 'c')

###############################################

# pick one and can pick the same thing in list
# the number of all cases doesn't care the order

from itertools import combinations_with_replacement

result_4 = list(combinations_with_replacement(data, 2))
print(result_4)

# [('a', 'a'), ('a', 'b'), ('a', 'c'), 
# ('b', 'b'), ('b', 'c'), ('c', 'c')]



###############################################

# How many have same content in list

from collections import Counter

counter = Counter(['red', 'red', 'red', 'green', 'blue', 'blue'])
print(counter['blue']) # 2
print(counter['green']) # 1
print(dict(counter)) # {'red': 3, 'green': 1, 'blue': 2}
print(counter) # Counter({'red': 3, 'blue': 2, 'green': 1})


###############################################

# greatest common divisor 최대공약수
# lowest common denominator 최소 공약수

import math

def lcm(a, b):
    return a * b // math.gcd(a,b)
a = 21
b = 14
print(math.gcd(21,14)) # GCD
print(lcm(21, 14)) # LCM