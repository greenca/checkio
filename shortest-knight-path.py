# You are given the start and end squares as chess coordinates separated
# by a hyphen. You should find the length of the shortest path for the
# knight from one point to another on the chessboard.

def checkio(cells):
    cell_str = cells.split('-')
    start = (ord(cell_str[0][0])-ord('a'), ord(cell_str[0][1])-ord('1'))
    end = (ord(cell_str[1][0])-ord('a'), ord(cell_str[1][1])-ord('1'))

    shortest_path = 1000

    steps = [(start, 0)]
    visited = {start}

    while steps and shortest_path > 1:
        step = steps.pop(0)
        visited.add(step[0])
        if step[0] == end:
            if step[1] < shortest_path:
                shortest_path = step[1]
        elif step[1] < shortest_path - 1:
            row, col = step[0]
            [(i, 2*j) for i in [1,-1] for j in [1,-1]]
            [(2*i, 2*j) for i in [1,-1] for j in [1,-1]]
            for i in [1,-1]:
                for j in [1, -1]:
                    next1 = (row + i, col + 2*j)
                    next2 = (row + 2*i, col + j)
                    if max(next1) < 8 and min(next1) >= 0 and next1 not in visited:
                        steps.append((next1, step[1] + 1))
                    if max(next2) < 8 and min(next2) >= 0 and next2 not in visited:
                        steps.append((next2, step[1] + 1))

    return shortest_path

if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(u"b1-d5") == 2, "1st example"
    assert checkio(u"a6-b8") == 1, "2nd example"
    assert checkio(u"h1-g2") == 4, "3rd example"
    assert checkio(u"h8-d7") == 3, "4th example"
    assert checkio(u"a1-h8") == 6, "5th example"
