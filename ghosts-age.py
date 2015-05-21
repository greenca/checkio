# Nicola takes a moment to study the ghosts. He is trying to think up a
# new method to determine just how old these ghosts are. He knows that
# their age is somehow related to their opacity. To measure their
# opacity Nikola uses a scale of 10000 units to 0 units, where 10000 is
# a completely opaque newborn ghost (0 years old) and 0 is completely
# transparent ghost (of an unknown age).
# After some experimenting, Nikola thinks he has discovered the law of
# ghostly opacity. On every birthday, a ghost's opacity is reduced by a
# number of units equal to its age when its age is a Fibonacci number
# (Read about this here) or increased by 1 if it is not.
# Help Nicola write a function which will determine the age of a ghost
# based on its opacity. You are given opacity measurements as a number
# ranging from 0 to 10000 inclusively. The ghosts cannot be older than
# 5000 years as they simply disappear after such a long time (really!).
# This is a Halloween task so you should try and write a "magic" or
# "scary" solution. Please, do not write "regular" solution.
# Input: An opacity measurement as an integer.
# Output: The age of the ghost as an integer.

def checkio(opacity):
    g = Ghost(opacity)
    return g + 0


class Ghost:
    def __init__(self, opacity):
        self.opacity = opacity

    def __add__(self, other):
        curr_opacity = 10000
        for year in range(5000):
            if self.is_fibonacci(year):
                curr_opacity -= year
            else:
                curr_opacity += 1
            if curr_opacity == self.opacity:
                return year + other
        return None

    @staticmethod
    def is_fibonacci(num):
        if num == 0 or num == 1:
            return True
        curr_fib = 1
        last_fib = 1
        while curr_fib < num:
            curr_fib += last_fib
            last_fib = curr_fib - last_fib
        if curr_fib == num:
            return True
        else:
            return False      


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(10000) == 0, "Newborn"
    assert checkio(9999) == 1, "1 year"
    assert checkio(9997) == 2, "2 years"
    assert checkio(9994) == 3, "3 years"
    assert checkio(9995) == 4, "4 years"
    assert checkio(9990) == 5, "5 years"
