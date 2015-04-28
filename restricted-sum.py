# Our new calculator is censored and as such it does not accept certain
# words. You should try to trick by writing a program to calculate the
# sum of numbers.
# Given a list of numbers, you should find the sum of these
# numbers. Your solution should not contain any of the banned words,
# even as a part of another word.
# The list of banned words are as follows:
# sum
# import
# for
# while
# reduce
# Input: A list of numbers.
# Output: The sum of numbers.
# Precondition: The small amount of data. 

def checkio(data):
    if data:
        return data[0] + checkio(data[1:])
    else:
        return 0
