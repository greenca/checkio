# In Stephan's version of multiplication, we convert numbers to binary
# representation without leading zeroes. Then the first number is
# written vertically (up to down) and the second horizontally (left to
# right). With that, we fill a table with various binary operations for
# each crossing -- AND, OR, XOR, so we end up with three tables. In each
# table we convert rows to decimal and summarize it, then summarize the
# results of three tables. Let's look at several examples.
# 4 x 6 =
# AND
# X	1	1	0	dec	sum
# 1	1	1	0	6	6
# 0	0	0	0	0
# 0	0	0	0	0
# OR
# X	1	1	0	dec	sum
# 1	1	1	1	7	19
# 0	1	1	0	6
# 0	1	1	0	6
# XOR
# X	1	1	0	sum
# 1	0	0	1	1	13
# 0	1	1	0	6
# 0	1	1	0	6
# 6 + 19 + 13 = 38
# 2 x 7 =
# AND
# X	1	1	1	dec	sum
# 1	1	1	1	7	7
# 0	0	0	0	0
# OR
# X	1	1	1	dec	sum
# 1	1	1	1	7	14
# 0	1	1	1	7
# XOR
# X	1	1	1	sum
# 1	0	0	0	0	7
# 0	1	1	1	7
# 7 + 14 + 7 = 28
# 7 x 2 =
# AND
# X	1	0	dec	sum
# 1	1	0	2	6
# 1	1	0	2
# 1	1	0	2
# OR
# X	1	0	dec	sum
# 1	1	1	3	9
# 1	1	1	3
# 1	1	1	3
# XOR
# X	1	0	sum
# 1	0	1	1	3
# 1	0	1	1
# 1	0	1	1
# 6 + 9 + 3 = 18
# You should help Stephan write a function to calculate this
# "multiplication". You are given two positive integers (n > 0), be careful with order of arguments.
# Input: Two arguments as integers.
# Output: The result of the Stephan's "multiplication", an integer.
# Precondition: 0 < x < 100
# 0 < y < 100

def checkio(first, second):
    bin1 = bin(first)[2:]
    bin2 = bin(second)[2:]
    and_sum = 0
    or_sum = 0
    xor_sum = 0
    for char1 in bin1:
        and_val = ''
        or_val = ''
        xor_val = ''
        i = int(char1)
        for char2 in bin2:
            j = int(char2)
            if i and j:
                and_val += '1'
            else:
                and_val += '0'
            if i or j:
                or_val += '1'
            else:
                or_val += '0'
            if (i or j) and not (i and j):
                xor_val += '1'
            else:
                xor_val += '0'
        and_sum += int(and_val, 2)
        or_sum += int(or_val, 2)
        xor_sum += int(xor_val, 2)
    return and_sum + or_sum + xor_sum

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 6) == 38
    assert checkio(2, 7) == 28
    assert checkio(7, 2) == 18
