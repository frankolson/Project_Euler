### Project Euler Problem 10
### Will Olson
### 01 July 2013
### Python 2.7.5

from math import sqrt

def is_prime( n ):
    if n == 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    for x in range(3, int((sqrt(n)))+1, 2):
        if n % x == 0:
            return False
    return True

def find_prime_sum( number ):
    count = 1
    prime_sum = 0
    while count < number:
        if is_prime(count):
            prime_sum += count
        count += 1
    return prime_sum

user_input = int(raw_input("Enter max number: "))
print find_prime_sum(user_input)
print ''
print raw_input("Any key to continue...")
