# How CheckSum Works:
# CheckSum reasoning will need map points. This is a definition lookup
# for how to process the input necessary to generate the final
# character, which will be enable us instantly verify that our input is
# correct. In other words, for each sequence character of the input, we
# are confident there can only be one possible input, all thanks to this
# final character.
# The steps you must take to obtain the final character are as follows:
# From the rightmost input, traverse from right to left, and apply 'map
# point character lookup' for even-indexed characters.
# Add map point results for even-indexed characters with the unchanged
# digits from the original number.
# Find the remainder of this sum with 10. For an example sum of 67, the
# remainder is 7. ( 67 modulo 10 = 7 )
# Your final character should be 0 if the sum is a multiple-of-10, but
# it should be 10 minus remainder if the sum is not a multiple-of-10.
# To generate the 'map point character lookup' table: 
# Double the value of a character.
# If the product of this doubling operation is greater than 9 (e.g: 7 *
# 2 = 14), reduce it by summing the digits of the product. (i.e., find
# its digital root. e.g., 10: 1 + 0 = 1, 14: 1 + 4 = 5) Only do this
# once. Even if the sum is greater than 9, leave it alone.
# To make this more interesting, we can use alphanumeric input, which is
# a possible combination of 10 digits and 26 capital letters. It means
# that we will have to upgrade our map point to support letters. How we
# achieve that? We use each character's ASCII value to help us determine
# the character sequence. For example: 'A' has an ASCII value 65. To
# determine its sequence in our map, we need to substract 48.
# Now it's time to test your CheckSum module!
# Input: Unsanitized numeric or alphanumeric due to formatting purpose
# Output: List of its final character and sum of digits

import string

def checkio(data):
    trans_map = dict((ord(char), None) for char in data if char not in string.digits + string.letters)
    input = data.translate(trans_map)
    char_sum = 0
    for i, char in enumerate(input[::-1]):
        if i % 2 == 0:
            char_sum += map_point(char)
        else:
            char_sum += ord(char) - 48
    if char_sum % 10 == 0:
        final_char = 0
    else:
        final_char = 10 - (char_sum % 10)
    return [str(final_char), char_sum]

def map_point(char):
    val = ord(char) - 48
    doubled = 2*val
    if doubled <= 9:
        reduced = doubled
    else:
        reduced = (doubled % 10) + ((doubled / 10) % 10) + (doubled / 100)
    return reduced

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert (checkio(u"799 273 9871") == ["3", 67]), "First Test"
    assert (checkio(u"139-MT") == ["8", 52]), "Second Test"
    assert (checkio(u"123") == ["0", 10]), "Test for zero"
    assert (checkio(u"999_999") == ["6", 54]), "Third Test"
    assert (checkio(u"+61 820 9231 55") == ["3", 37]), "Fourth Test"
    assert (checkio(u"VQ/WEWF/NY/8U") == ["9", 201]), "Fifth Test"

    print("OK, done!")
