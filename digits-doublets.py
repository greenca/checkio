# You are given the list of numbers with exactly the same length and you must find 
# the shortest chain of numbers to link the first number to the last, with each 
# pair of adjacent numbers differing by one digit.

# You should write a function that receives a list of numbers (positive integers) and 
# returns the shortest route as a list of numbers.

# Input: Numbers as a list of integers.
# Output: The shortest chain from the first to the last number as a list of integers.
# Precondition: Numbers have the same length
# ∀ x ∈ numbers : 100 ≤ x < 1000

def checkio(numbers):
    first = numbers[0]
    last = numbers[-1]

    # Check for only one element
    if first == last:
        return [first]

    # Check for first and last differing by only one digit
    if sum([i!=j for i,j in zip(str(first),str(last))]) == 1:
        return [first, last]
    
    # Find all list members one digit different from the first
    seconds = []
    for num in numbers:
        if sum([i!=j for i,j in zip(str(first),str(num))]) == 1:
            seconds.append(num)

    # Find chain from each second to last and choose the shortest
    best_solution = numbers
    for second in seconds:
        reduced_numbers = [second] + [num for num in numbers if num != first and num != second]
        curr_solution = checkio(reduced_numbers)
        if len(curr_solution) <= len(best_solution):
            best_solution = curr_solution

    return [first] + best_solution


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([123, 991, 323, 321, 329, 121, 921, 125, 999]) == [123, 121, 921, 991, 999], "First"
    assert checkio([111, 222, 333, 444, 555, 666, 121, 727, 127, 777]) == [111, 121, 127, 727, 777], "Second"
    assert checkio([456, 455, 454, 356, 656, 654]) == [456, 454, 654], "Third, [456, 656, 654] is correct too"

