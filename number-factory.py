# You are given a two or more digits number N. For this mission, you
# should find the smallest positive number of X, such that the product
# of its digits is equal to N. If X does not exist, then return 0.
# Let's examine the example. N = 20. We can factorize this number as
# 2*10, but 10 is not a digit. Also we can factorize it as 4*5 or
# 2*2*5. The smallest number for 2*2*5 is 225, for 4*5 -- 45. So we
# select 45.
# Input: A number N as an integer.
# Output: The number X as an integer.
# Precondition: 
# 9 < N < 10^5.

def checkio(number):
    factors = flatten(digit_factors(number,''))
    if factors:
        return min([int(n) for n in flatten(factors)])
    else:
        return 0

def digit_factors(number, prev_facs):
    if number == 1:
        return ''.join([str(n) for n in prev_facs])
    factors = []
    for n in range(2,10):
        if number % n == 0:
            factors.append(digit_factors(number/n, prev_facs + str(n)))
    return factors

def flatten(l):
    if any(type(x) is list for x in l):
        y = []
        for x in l:
            if type(x) is list:
                y += x
            else:
                y.append(x)
        return flatten(y)
    else:
        return l


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(20) == 45, "1st example"
    assert checkio(21) == 37, "2nd example"
    assert checkio(17) == 0, "3rd example"
    assert checkio(33) == 0, "4th example"
    assert checkio(3125) == 55555, "5th example"
    assert checkio(9973) == 0, "6th example"
