# The robots want to saw the stick in several pieces. 
# The length of the stick is N inches. 
# All of the parts should have integer lengths. 
# You should saw the stick so that the lengths form the 
# consecutive fragment of the Triangular numbers series 
# with the maximum quantity (fragment's length). 
# The parts should have different lengths (no repeating). 
# You are given a length of the stick (N). You should 
# return the list of lengths (integers) for the parts in 
# ascending order. If it's not possible and the problem 
# does not have a solution, then you should return an empty list.
# Input: A length of the stick as an integer.
# Output: A fragment of the Triangular numbers as a list of integers 
# (sorted in ascending order) or an empty list.
# Precondition: 0 < length < 1000

def checkio(number):
    triangular_series = []
    for n in range(1, number):
        triangular_series.append(n*(n+1)/2)
    solution_series = []
    for i, num in enumerate(triangular_series):
        curr_sum = num
        j = i+1
        while curr_sum < number:
            curr_sum += triangular_series[j]
            j += 1
        if curr_sum == number:
            solution_series.append(triangular_series[i:j])
    best_fragment = []
    for fragment in solution_series:
        if len(fragment) > len(best_fragment):
            best_fragment = fragment
    return best_fragment

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(64) == [15, 21, 28], "1st example"
    assert checkio(371) == [36, 45, 55, 66, 78, 91], "1st example"
    assert checkio(225) == [105, 120], "1st example"
    assert checkio(882) == [], "1st example"
