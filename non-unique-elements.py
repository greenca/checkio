# You are given a non-empty list of integers (X). 
# For this task, you should return a list consisting of only 
# the non-unique elements in this list. To do so you will 
# need to remove all unique elements (elements which are 
# contained in a given list only once). When solving this task, 
# do not change the order of the list. 
# Input: A list of integers.
# Output: The list of integers.

def checkio(data):
    filtered_data = []
    for d in data:
        if data.count(d) > 1:
            filtered_data.append(d)
    return filtered_data


if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(checkio([1]), list), "The result must be a list"
    assert checkio([1, 2, 3, 1, 3]) == [1, 3, 1, 3], "1st example"
    assert checkio([1, 2, 3, 4, 5]) == [], "2nd example"
    assert checkio([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5], "3rd example"
    assert checkio([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9], "4th example"
