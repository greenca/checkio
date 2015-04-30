# You are given a matrix of NxN (4≤N≤10). You should check if there is a
# sequence of 4 or more matching digits. The sequence may be positioned
# horizontally, vertically or diagonally (NW-SE or NE-SW diagonals).
# Input: A matrix as a list of lists with integers.
# Output: Whether or not a sequence exists as a boolean.
# Precondition:
# 0 ≤ len(matrix) ≤ 10
# all(all(0 < x < 10 for x in row) for row in matrix)

def checkio(matrix):
    
    N = len(matrix)

    # Check horizontal
    for row in matrix:
        for n in range(N-3):
            if max(row[n:n+4]) == min(row[n:n+4]):
                return True

    # Check vertical
    for n in range(N-3):
        for j in range(N):
            col = [matrix[i][j] for i in range(n,n+4)]
            if max(col) == min(col):
                return True

    # Check diagonals
    for n in range(N-3):
        for m in range(N-3):
            diag1 = [matrix[i][j] for i, j in zip(range(n,n+4), range(m,m+4))]
            diag2 = [matrix[i][j] for i, j  in zip(range(n,n+4), range(m+3,m-1,-1))]
            if max(diag1) == min(diag1) or max(diag2) == min(diag2):
                return True

    return False


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True, "Vertical"
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False, "Nothing here"
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True, "Long Horizontal"
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"

