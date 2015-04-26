# Find the greatest common divisor of positive integers

def greatest_common_divisor(*args):

    # Keep only unique and non-zero arguments
    relevant_args = list(set([x for x in args if x > 0]))

    if len(relevant_args) == 1:
        # If only one unique arg, that is the gcd
        return relevant_args[0]
    else:
        # Euclid's algorithm
        min_arg = min(relevant_args)
        return greatest_common_divisor(min_arg, *[arg % min_arg for arg in relevant_args])


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert greatest_common_divisor(6, 4) == 2, "Simple"
    assert greatest_common_divisor(2, 4, 8) == 2, "Three arguments"
    assert greatest_common_divisor(2, 3, 5, 7, 11) == 1, "Prime numbers"
    assert greatest_common_divisor(3, 9, 3, 9) == 3, "Repeating arguments"
