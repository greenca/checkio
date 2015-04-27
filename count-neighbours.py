# You are given a state for a rectangular board game grid with chips in
# a binary matrix, where 1 is a cell with a chip and 0 is an empty
# cell. You are also given the coordinates for a cell in the form of row
# and column numbers (starting from 0). You should determine how many
# chips are close to this cell. Every cell interacts with its eight
# neighbours; those cells that are horizontally, vertically, or
# diagonally adjacent.
# Input: Three arguments. A grid as a tuple of tuples with integers
# (1/0), a row number and column number for a cell as integers.
# Output: How many neighbouring cells have chips as an integer.
# Precondition:
# 3 ≤ len(grid) ≤ 10
# all(len(grid[0]) == len(row) for row in grid)

def count_neighbours(grid, row, col):
    num_rows = len(grid)
    num_cols = len(grid[0])
    neighbours = [grid[i][j] for i in range(max(0,row-1), min(num_rows,row+2)) for j in range(max(0,col-1), min(num_cols,col+2))]
    return sum(neighbours) - grid[row][col]


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_neighbours(
        ((1, 0, 0, 1, 0),
         (0, 1, 0, 0, 0),
         (0, 0, 1, 0, 1),
         (1, 0, 0, 0, 0),
         (0, 0, 1, 0, 0),), 1, 2) == 3, "1st example"
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 0, 0) == 1, "2nd example"
    assert count_neighbours(((1, 1, 1),
                             (1, 1, 1),
                             (1, 1, 1),), 0, 2) == 3, "Dense corner"
    assert count_neighbours(((0, 0, 0),
                             (0, 1, 0),
                             (0, 0, 0),), 1, 1) == 0, "Single"
