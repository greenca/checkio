def checkio(opacity):
    return Ghost() + opacity


class Ghost:

    @staticmethod
    def __add__(other):
        curr_opacity = 10000
        for year in range(5000):
            if Ghost.is_fibonacci(year):
                curr_opacity -= year
            else:
                curr_opacity += 1
            if curr_opacity == other:
                return year
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