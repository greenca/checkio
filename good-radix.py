# You are given some number n written as a string with the radix equal
# to k (1 < k < 37). We know that our number is divisible by (k - 1)
# without a remainder. You should find the minimal possible k, if it
# exists, or return 0.
# Input: A number as a string.
# Output: The radix k as an integer.
# Precondition: A number conforms regexp "[A-Z0-9]{1, 10}".
# 0 < number

def checkio(number):
    char_list = list(number)
    num_list = []
    for char in char_list:
        if char.isdigit():
            num_list.append(int(char))
        else:
            num_list.append(ord(char) - 55)
    for k in range(max(num_list) + 1, 37):
        if convertNum(num_list, k) % (k - 1) == 0:
            return k
    return 0

def convertNum(num_list, k):
    num = 0
    N = len(num_list) - 1
    for index, digit in enumerate(num_list):
        num += digit * k**(N - index)
    return num

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(u"18") == 10, "Simple decimal"
    assert checkio(u"1010101011") == 2, "Any number is divisible by 1"
    assert checkio(u"222") == 3, "3rd test"
    assert checkio(u"A23B") == 14, "It's not a hex"
    assert checkio(u"IDDQD") == 0, "k is not exist"
    print('Local tests done')
