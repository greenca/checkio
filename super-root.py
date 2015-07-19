# The super root of a number N is the number x, such that x**x = N.
# The result should be accurate so that N - 0.001 < x**x < N + 0.001.
# Input: A number (N) as an integer.
# Output: The super root (x) as a float or an integer.
# Precondition:
# 1 <= number <= 10 ** 10

def super_root(number):
    threshold = 0.001
    upper = 10
    lower = 0
    mid = (upper + lower)/2.0
    while abs(mid**mid - number) > threshold:
        if mid**mid > number:
            upper = mid
        else:
            lower = mid
        mid = (upper + lower)/2.0
    return mid

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    def check_result(function, number):
        result = function(number)
        if not isinstance(result, (int, float)):
            print("The result should be a float or an integer.")
            return False
        p = result ** result
        if number - 0.001 < p < number + 0.001:
            return True
        return False
    assert check_result(super_root, 4), "Square"
    assert check_result(super_root, 9), "Cube"
    assert check_result(super_root, 81), "Eighty one"
