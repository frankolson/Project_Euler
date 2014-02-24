### Project Euler Problem 6
### Will Olson
### 28 June 2013
### Python 2.7.5

def square_sum_diff( n ):
    if square_sum(n) > sum_square(n):
        return square_sum(n) - sum_square(n)
    return sum_square(n) - square_sum(n)

def square_sum( n ):
    k = 0
    for x in range(1, n+1):
        k += x
    return k**2

def sum_square( n ):
    k = 0
    for x in range(1, n+1):
        k += x**2
    return k

print square_sum_diff(100)
