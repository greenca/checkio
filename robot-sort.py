# You are given the sizes and initial order of the rods as an array of
# numbers. Indexes are position, values are sizes. You should order this
# array from the smallest to the largest in size.
# For each action Stephan can swap only two neighbouring elements. Each
# action should be represented as a string with two digits - indexes of
# the swapped elements (ex, "01" - swap 0th and 1st rods). The result
# should be represented as a string that contains the sequence of
# actions separated by commas. If the array does not require sorting,
# then return an empty string.
# And you can swap only N*(N-1)/2 times, where N - is a quantity of
# rods.
# Input: An array as a tuple of integers.
# Output: The sequence of actions as a string.

def swapsort(array):
    N = len(array)
    tosort = list(array)
    swaps = []
    isSorted = False
    while not isSorted:
        isSorted = True
        for i in range(N-1):
            if tosort[i] > tosort[i+1]:
                isSorted = False
                swaps.append('{:d}{:d}'.format(i, i+1))
                tosort[i], tosort[i+1] = tosort[i+1], tosort[i]
    return ','.join(swaps)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    def check_solution(f, indata):
        result = f(indata)
        array = list(indata[:])
        la = len(array)
        if not isinstance(result, str):
            print("The result should be a string")
            return False
        actions = result.split(",") if result else []
        for act in actions:
            if len(act) != 2 or not act.isdigit():
                print("The wrong action: {}".format(act))
                return False
            i, j = int(act[0]), int(act[1])
            if i >= la or j >= la:
                print("Index error: {}".format(act))
                return False
            if abs(i - j) != 1:
                print("The wrong action: {}".format(act))
                return False
            array[i], array[j] = array[j], array[i]
        if len(actions) > (la * (la - 1)) // 2:
            print("Too many actions. BOOM!")
            return False
        if array != sorted(indata):
            print("The array is not sorted. BOOM!")
            return False
        return True
    
    assert check_solution(swapsort, (6, 4, 2)), "Reverse simple"
    assert check_solution(swapsort, (1, 2, 3, 4, 5)), "All right!"
    assert check_solution(swapsort, (1, 2, 3, 5, 3)), "One move"
