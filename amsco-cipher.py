# Let's look at the AMSCO cipher. This is a positional cipher with
# exchanges. You can easily encode or decode a message with a pen and
# paper, that is of course, if you know the key.
# The key is represented as a number that consist of unique digits from
# 1 to N. N is a length of the key. To encode message we should write a
# message in a matrix with N columns. The matrix is written row by
# row. In this process, one or two characters are alternately recorded
# in a field. One or two characters alternate in rows and in columns too
# (like a chessboard). The first element is single letter field (this is
# the arrangement for this mission). The last field can have single
# characters if there are not enough. Columns are then numbered with
# digits from the key in order. For example: using the key 312, the
# first column will be 3, the second is 1 and the third is 2. Lastly,
# you will write all characters in the columns as they were numbered in
# the most recent step. All white spaces and punctuation symbols are
# excluded while letters are in lowercase.
# Let's look at this with an example. The message "Lorem ipsum dolor sit
# amet". And the key is 4123. The cut message is
# "loremipsumdolorsitamet". In matrix form it will be:
#    4   1   2   3
#    l  or   e  mi
#   ps   u  md   o
#    l  or   s  it
#   am   e   t
# Now write the columns as they are numbered in the ascending order -
# "oruore", "emdst", "mioit", "lpslam". The encoded message is
# "oruoreemdstmioitlpslam".
# You are given an encoded message and the key. Your mission is to
# decode the message. Of course in the cut version.
# Input: Two arguments. A message as a string (unicode) and a key as an
# integer.
# Output: The decoded message as a string.
# Precondition: 4 <= len(str(key))
# int(len(str(key)) * 1.5) <= len(message)
# re.match("\w+$", message)

import math

def decode_amsco(message, key):
    cols = [int(i) for i in str(key)]
    N = len(cols)
    num_rows = int(math.ceil(len(message)/(1.5*N)))
    chars = []
    char_sum = 0
    for i in range(num_rows):
        chars_row = []
        for j in range(N):
            if char_sum < len(message):
                num = min((i + j) % 2 + 1, len(message)-char_sum)
                chars_row.append(num)
                char_sum += num
            else:
                chars_row.append(0)
        chars.append(chars_row)
    for col in range(1,N+1):
        j = cols.index(col)
        for i in range(num_rows):
            num_chars = chars[i][j]
            chars[i][j] = message[:num_chars]
            message = message[num_chars:]
    decoded_rows = [''.join(row) for row in chars]
    decoded = ''.join(decoded_rows)
    return decoded

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert decode_amsco(u"oruoreemdstmioitlpslam", 4123) == "loremipsumdolorsitamet", "Lorem Ipsum"
    assert decode_amsco(u'kicheco', 23415) == "checkio", "Checkio"
    assert decode_amsco(u'hrewhoorrowyilmmmoaouletow', 123) == "howareyouwillhometommorrow", "How are you"
