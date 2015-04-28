# The Hamming distance between two binary integers is the number of bit
# positions that differs.
# You are given two positive numbers (N, M) in decimal form. You should
# calculate the Hamming distance between these two numbers in binary
# form.
# Input: Two arguments as integers.
# Output: The Hamming distance as an integer.
# Precondition:
# 0 < n < 106
# 0 < m < 106

def checkio(n, m):

    # Convert to binary, strip initial '0b' and reverse
    bin1 = bin(max(n,m))[:1:-1]
    bin2 = bin(min(n,m))[:1:-1]

    dist = 0

    # Compare pairs of bits
    for x,y in zip(bin1, bin2):
        if x != y:
            dist += 1

    # Count 1's in extra bits in larger number
    dist += bin1[len(bin2):].count('1')

    return dist


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(117, 17) == 3, "First example"
    assert checkio(1, 2) == 2, "Second example"
    assert checkio(16, 15) == 5, "Third example"
