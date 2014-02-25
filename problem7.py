### Project Euler Problem 7
### Will Olson
### 01 July 2013
### Python 2.7.5

""" from problem3 import is_prime (optional)"""
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

def iterate_through_primes( n ):
    primes = 0
    number = 0
    while primes < n:
        number += 1
        if is_prime(number):
            primes += 1
    return number

print "This program calculates the nth prime number"
print ''
user_input = int(raw_input("enter number: "))
print iterate_through_primes(user_input)

