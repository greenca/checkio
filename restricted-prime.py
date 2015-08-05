# The list of forbidden words and symbols:
# import
# div
# eval
# range
# len
# ⁄ % −
# digits (0-9)
# Given a number (0 < n < 10000), you should check if it is a prime or
# not. Your solution should not contain any of the forbidden words,
# symbols or digits (even as a part of another word).
# Input: A number as an integer.
# Output: Is it prime or not as a boolean.
# Precondition: 1 < number < 10000

def checkio(number):
    n = True
    all_nums = []
    while n < number:
        all_nums.append(n)
        n += True
    while all_nums:
        n = all_nums.pop(False)
        if n*n == number:
            return False
        for num in all_nums:
            if n*num == number:
                return False
    return True
