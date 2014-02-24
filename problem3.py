### Project Euler Problem 3
### Will Olson
### 27 June 2013
### Python 3.3.0
from math import sqrt

def is_prime( n ):
    if n == 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    for x in range(3, round(sqrt(n))+ 1, 2):
        if n % x == 0:
            return False
    return True

def high_prime_factor( n ):
    highest = 1
    for x in range(3,round(sqrt(n)), 2):
        if n % x == 0:
            if is_prime(x):
                if x > highest:
                    highest = x
    return highest

number = int(input("Enter a number: "))

print(high_prime_factor(number))
