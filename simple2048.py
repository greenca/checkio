# 2048 is played on a simple 4×4 grid with tiles. Player can move tiles
# left, right, up, and down. If two tiles of the same number collide
# while moving, they will merge into a tile with the sum value of the
# two tiles. The resulting tile cannot merge with another tile again in
# the same move. If we have three tiles of the same number, then first
# collide tiles which closer to edge in the moving direction (right move
# - closer to the right edge). Every turn, a new tile will appear in the
# last empty spot (value 0) on the board with a value of 2. The last
# empty slot is determined by indexes that are defined in the following
# order:
# [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
# At the beginning, there's already two numbers on the board.

# You are given a game state represented as a 4x4 matrix with numbers
# that are powers of 2. Players move in a direction (up, down, left,
# right). You should return the game state after this move.
# If the game is won, i.e. 2048 appears on the board, then return the
# winning matrix:
# [['U','W','I','N'], ['U','W','I','N'], ['U','W','I','N'], ['U','W','I','N']]
# If the game is lose, i.e. nothing change after the player move and
# there is not a empty spot, then return the losing matrix:
# [['G','A','M','E'], ['O','V','E','R'], ['G','A','M','E'], ['O','V','E','R']]

# Input: A game state as a list of lists with integers and player's move
# as a string ('up', 'down', 'left' or 'right').
# Output: The game state after player's move as a list of lists with
# integers or letters.
# Preconditions: len(state) == 4
# all(len(row) == 4 for row in state)
# all(all(x in (0, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024) for x in row) for row in state)

WIN = [['U','W','I','N'], ['U','W','I','N'], ['U','W','I','N'], ['U','W','I','N']]
LOSE = [['G','A','M','E'], ['O','V','E','R'], ['G','A','M','E'], ['O','V','E','R']]

def move2048(state, move):
    if move == 'up':
        newstate = moveUp(state)
    elif move == 'right':
        newstate = moveRight(state)
    elif move == 'down':
        newstate = moveDown(state)
    elif move == 'left':
        newstate = moveLeft(state)
    else:
        raise ValueError('Invalid move')
    if max(max(newstate,key=max)) == 2048:
        return WIN
    if newstate == state and min(min(newstate,key=min)) > 0:
        return LOSE
    return newstate

def moveUp(state):
    N = len(state)
    for j in range(N):
        tiles = [state[i][j] for i in range(N) if state[i][j] != 0]
        for i in range(N):
            state[i][j] = 0
        i = 0
        while tiles:
            tile = tiles.pop(0)
            if tiles and tiles[0] == tile:
                tile *= 2
                tiles.pop(0)
            state[i][j] = tile
            i += 1
    newtile = False
    for i in range(N-1,-1,-1):
        for j in range(N-1,-1,-1):
            if state[i][j] == 0 and not newtile:
                state[i][j] = 2
                newtile = True
    return state

def moveRight(state):
    N = len(state)
    for i in range(N):
        tiles = [state[i][j] for j in range(N-1,-1,-1) if state[i][j] != 0]
        for j in range(N):
            state[i][j] = 0
        j = N-1
        while tiles:
            tile = tiles.pop(0)
            if tiles and tiles[0] == tile:
                tile *= 2
                tiles.pop(0)
            state[i][j] = tile
            j -= 1
    newtile = False
    for i in range(N-1,-1,-1):
        for j in range(N-1,-1,-1):
            if state[i][j] == 0 and not newtile:
                state[i][j] = 2
                newtile = True
    return state
            
def moveDown(state):
    N = len(state)
    for j in range(N):
        tiles = [state[i][j] for i in range(N-1,-1,-1) if state[i][j] != 0]
        for i in range(N):
            state[i][j] = 0
        i = N-1
        while tiles:
            tile = tiles.pop(0)
            if tiles and tiles[0] == tile:
                tile *= 2
                tiles.pop(0)
            state[i][j] = tile
            i -= 1
    newtile = False
    for i in range(N-1,-1,-1):
        for j in range(N-1,-1,-1):
            if state[i][j] == 0 and not newtile:
                state[i][j] = 2
                newtile = True
    return state

def moveLeft(state):
    N = len(state)
    for i in range(N):
        tiles = [state[i][j] for j in range(N) if state[i][j] != 0]
        for j in range(N):
            state[i][j] = 0
        j = 0
        while tiles:
            tile = tiles.pop(0)
            if tiles and tiles[0] == tile:
                tile *= 2
                tiles.pop(0)
            state[i][j] = tile
            j += 1
    newtile = False
    for i in range(N-1,-1,-1):
        for j in range(N-1,-1,-1):
            if state[i][j] == 0 and not newtile:
                state[i][j] = 2
                newtile = True
    return state


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert move2048([[0, 2, 0, 0],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0],
                     [0, 2, 0, 0]], 'up') == [[0, 4, 0, 0],
                                              [0, 0, 0, 0],
                                              [0, 0, 0, 0],
                                              [0, 0, 0, 2]], "Start. Move Up!"
    assert move2048([[4, 0, 0, 0],
                     [0, 4, 0, 0],
                     [0, 0, 0, 0],
                     [0, 0, 8, 8]], 'right') == [[0, 0, 0, 4],
                                                 [0, 0, 0, 4],
                                                 [0, 0, 0, 0],
                                                 [0, 0, 2, 16]], "Simple right"
    assert move2048([[2, 0, 2, 2],
                     [0, 4, 4, 4],
                     [8, 8, 8, 16],
                     [0, 0, 0, 0]], 'right') == [[0, 0, 2, 4],
                                                 [0, 0, 4, 8],
                                                 [0, 8, 16, 16],
                                                 [0, 0, 0, 2]], "Three merging"
    assert move2048([[256, 0, 256, 4],
                     [16, 8, 8, 0],
                     [32, 32, 32, 32],
                     [4, 4, 2, 2]], 'right') == [[0, 0, 512, 4],
                                                 [0, 0, 16, 16],
                                                 [0, 0, 64, 64],
                                                 [0, 2, 8, 4]], "All right"
    assert move2048([[4, 4, 0, 0],
                     [0, 4, 1024, 0],
                     [0, 256, 0, 256],
                     [0, 1024, 1024, 8]], 'down') == [['U', 'W', 'I', 'N'],
                                                      ['U', 'W', 'I', 'N'],
                                                      ['U', 'W', 'I', 'N'],
                                                      ['U', 'W', 'I', 'N']], "We are the champions!"
    assert move2048([[2, 4, 8, 16],
                     [32, 64, 128, 256],
                     [512, 1024, 2, 4],
                     [8, 16, 32, 64]], 'left') == [['G', 'A', 'M', 'E'],
                                                   ['O', 'V', 'E', 'R'],
                                                   ['G', 'A', 'M', 'E'],
                                                   ['O', 'V', 'E', 'R']], "Nobody moves!"
