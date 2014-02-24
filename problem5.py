### Project Euler Problem 5
### Will Olson
### 28 June 2013
### Python 2.7.5

""" though this program works for the problem at hand, it does
    not work for all variations of the problem, I would like to
    eventually fix this """

def is_divisible_by():
    """ finds the smallest number divisble by 1 through 20 """
    val = 20
    found = False
    while not found:
        if val%20 == 0 and val%19 == 0 and val%18 == 0 and val%17 == 0 and\
        val%16 == 0 and val%15 == 0 and val%14 == 0 and val%13 == 0 and\
        val%12 == 0 and val%11 == 0:
            return val
        else:
            val += 20

print is_divisible_by()
