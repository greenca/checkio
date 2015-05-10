# There is a list which contains integers or other nested lists which
# may contain yet more lists and integers which then… you get the
# idea. You should put all of the integer values into one flat list. The
# order should be as it was in the original list with string
# representation from left to right.
# Your code should be shorter than 140 characters (with whitespaces).
# Input data: A nested list with integers.
# Output data: The one-dimensional list with integers.

def flat_list(a):
    b = []
    for x in a:
        if type(x) is list: b.extend(flat_list(x))
        else: b.append(x)
    return b
