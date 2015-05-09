# You are given a pattern as a positive integer and a command as a
# word. For the comparison, the drone should convert the integer pattern
# into binary form, append zeros to left for the command length and
# compare this combination with the command.
# 1 is a letter. 0 is a digit.
# If the pattern and the command are coincided, then return True, else
# -- False. If pattern is longer than a command, then they are not
# coincided (For example - 8 = 1000 and "a").
# Input: Two arguments. A pattern as a positive integer and a command as
# a string.
# Output: Is the pattern coincide with the command or not as a boolean.
# Precondition: 0 ≤ pattern < 231
# 0 < len(command) < 32
# "command" contains only ASCII letters or digits.

def check_command(pattern, command):
    bin_pattern = '{:b}'.format(pattern).zfill(len(command))
    bin_command = ''.join([str(int(c.isalpha())) for c in command])
    return bin_command == bin_pattern

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_command(42, u"12a0b3e4") == True, "42 is the answer"
    assert check_command(101, u"ab23b4zz") == False, "one hundred plus one"
    assert check_command(0, u"478103487120470129") == True, "Any number"
    assert check_command(127, u"Checkio") == True, "Uppercase"
    assert check_command(7, u"Hello") == False, "Only full match"
    assert check_command(8, u"a") == False, "Too short command"
    assert check_command(5, u"H2O") == True, "Water"
    assert check_command(42, u"C2H5OH") == False, "Yep, this is not the Answer"
