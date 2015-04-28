# You are given a result of a game of Tic-Tac-Toe and you must
# determine if the game ends in a win or a draw as well as who will be
# the winner. Make sure to return "X" if the X-player wins and "O" if
# the O-player wins. If the game is a draw, return "D".
# A game's result is presented as a list of strings, where "X" and "O"
# are players' marks and "." is the empty cell.
# Input: A game result as a list of strings (unicode).
# Output: "X", "O" or "D" as a string.
# Precondition:
# There is either one winner or a draw.
# len(game_result) == 3
# all(len(row) == 3 for row in game_result)

def checkio(game_result):

    for row in game_result:
        if row == 'XXX':
            return 'X'
        if row == 'OOO':
            return 'O'
    
    for i in range(3):
        col = ''.join([game_result[j][i] for j in range(3)])
        if col == 'XXX':
            return 'X'
        if col == 'OOO':
            return 'O'
        
    diag1 = ''.join([game_result[i][i] for i in range(3)])
    if diag1 == 'XXX':
        return 'X'
    if diag1 == 'OOO':
        return 'O'
    
    diag2 = ''.join([game_result[2-i][i] for i in range(3)])
    if diag2 == 'XXX':
        return 'X'
    if diag2 == 'OOO':
        return 'O'

    return 'D'

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        u"X.O",
        u"XX.",
        u"XOO"]) == "X", "Xs wins"
    assert checkio([
        u"OO.",
        u"XOX",
        u"XOX"]) == "O", "Os wins"
    assert checkio([
        u"OOX",
        u"XXO",
        u"OXX"]) == "D", "Draw"
    assert checkio([
        u"O.X",
        u"XX.",
        u"XOO"]) == "X", "Xs wins again"

