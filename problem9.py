### Project Euler Problem 9
### Will Olson
### 01 July 2013
### Python 2.7.5

from math import sqrt

def find_pythag( number ):
    for a in range(1, number):
        for b in range(1, number):
            c = sqrt((a**2)+(b**2))
            if a + b + c == 1000:
                print a
                print b
                print c
                return a*b*c

user_input = int(raw_input("enter a limit: "))
print find_pythag(user_input)
print ''
print raw_input("Any key to continue...")
