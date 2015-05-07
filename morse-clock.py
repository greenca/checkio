# Help Stephen to create a module for converting a normal time string to
# a morse time string. The first digit for the hours has a length of 2
# while the second digit for the hour has a length of 4. The first
# digits for the minutes and seconds have a length of 3 while the second
# digits for the minutes and seconds have a length of 4. Every digit in
# the time is converted to binary representation. You will convert every
# on (or 1) signal to dash ("-") and every off (or 0) signal to dot
# (".").
# The result will be a morse time string with specific format:
# "h h : m m : s s"
# where each digits represented as sequence of "." and "-"
# Input: A normal time string as a string (unicode).
# Output: The morse time string as a string.
# Precondition: 
# time_string contains correct time.

import string

def checkio(time_string):
    times = map(int, time_string.split(":"))
    trans = string.maketrans('10', '-.')
    outputs = []
    for time in times:
        position =  '{0:03b}'.format(time/10).translate(trans) + ' '
        position += '{0:04b}'.format(time%10).translate(trans)
        outputs.append(position)
    return " : ".join(outputs)[1:]

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(u"10:37:49") == ".- .... : .-- .--- : -.. -..-", "First Test"
    assert checkio(u"21:34:56") == "-. ...- : .-- .-.. : -.- .--.", "Second Test"
    assert checkio(u"00:1:02") == ".. .... : ... ...- : ... ..-.", "Third Test"
    assert checkio(u"23:59:59") == "-. ..-- : -.- -..- : -.- -..-", "Fourth Test"

