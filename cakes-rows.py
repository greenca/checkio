# Someone has decided to bake a load of cakes and place them on the
# floor. Our robots can't help but try to find a pattern behind the
# cakes' disposition. Some cakes form rows, we want to count these
# rows. A row is a sequence of three or more cakes if we can draw a
# straight line through its centers. The greater row takes up the
# smaller rows. So if we have a row with 4 cakes, then we have only one
# row (not 4 by 3).
# The cake locations are represented as a list of coordinates. A
# coordinate is a list of two integers. You should count the rows.
# example
# Input: Сoordinates as a list of lists with two integers.
# Output: The quantity of rows as an integer.
# Precondition: 0 < |coordinates| < 20
# ∀ x,y ∈ coordinates : 0 ≤ x,y ≤ 10

def checkio(cakes):
    curr_pt = cakes[0]
    remaining = cakes[1:]
    poss_lines = set()
    vert_lines = set()

    # Find possible lines based on all pairs of points
    while remaining:
        for pt in remaining:
            if pt != curr_pt:
                if pt[0] == curr_pt[0]:
                    vert_lines.add(pt[0])
                else:
                    m = float(pt[1]-curr_pt[1])/(pt[0]-curr_pt[0])
                    b = pt[1] - m*pt[0]
                    poss_lines.add((m, b))
        curr_pt = remaining[0]
        remaining = remaining[1:]
    num_lines = 0

    # Find possible lines containing at least three points
    for m, b in poss_lines:
        if len([pt for pt in cakes if pt[1] == m*pt[0] + b]) >= 3:
            num_lines += 1
    for c in vert_lines:
        if len([pt for pt in cakes if pt[0] == c]) >= 3:
            num_lines += 1

    return num_lines

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([[3, 3], [5, 5], [8, 8], [2, 8], [8, 2]]) == 2
    assert checkio(
        [[2, 2], [2, 5], [2, 8], [5, 2], [7, 2], [8, 2],
         [9, 2], [4, 5], [4, 8], [7, 5], [5, 8], [9, 8]]) == 6
