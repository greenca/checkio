# You have been given a matrix as a 2D list with integers. Your task is
# to return a transposed matrix based on input.
# Input: A matrix as a list of lists with integers.
# Output: The transposed matrix as a list/tuple of lists/tuples with
# integers.
# Precondition:
# 0 < len(matrix) < 10
# all(0 < len(row) < 10 for row in matrix)

def checkio(data):
    transposed = []
    for row in data:
        for index, item in enumerate(row):
            if len(transposed) <= index:
                transposed.append([item])
            else:
                transposed[index].append(item)
    return transposed

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert isinstance(checkio([[0]]).pop(), list) is True, "Match types"
    assert checkio([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]]) == [[1, 4, 7],
                                    [2, 5, 8],
                                    [3, 6, 9]], "Square matrix"
    assert checkio([[1, 4, 3],
                    [8, 2, 6],
                    [7, 8, 3],
                    [4, 9, 6],
                    [7, 8, 1]]) == [[1, 8, 7, 4, 7],
                                    [4, 2, 8, 9, 8],
                                    [3, 6, 3, 6, 1]], "Rectangle matrix"
