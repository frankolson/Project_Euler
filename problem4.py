### Project Euler Problem 4
### Will Olson
### 28 Jan 2013
### Python 2.7.5

def make_high_number( n ):
    """ makes the largest number with n digits """
    count = 0
    num = ""
    while count < n:
        num += '9'
        count += 1
    return int(num)

def make_low_number( n ):
    """ makes the smallest number with n digits """
    count = 1
    num = "1"
    while count < n:
        num += '0'
        count += 1
    return int(num)


def is_highest_palindrome( n ):
    """ looks for largest palindrome made by multiplying together
        two number of length n """
    result = 0
    for x in range(make_high_number(n),make_low_number(n),-1):
        for i in range(make_high_number(n),make_low_number(n),-1):
            num = x * i
            string = str(num)
            if string == string[::-1]:
                if num > result:
                    result = num
    return result
            


print is_highest_palindrome(3)
print ''


