# A cipher grille is a 4×4 square of paper with four windows cut
# out. Placing the grille on a paper sheet of the same size, the encoder
# writes down the first four symbols of his password inside the windows
# (see fig. below). After that, the encoder turns the grille 90 degrees
# clockwise. The symbols written earlier become hidden under the grille
# and clean paper appears inside the windows. The encoder then writes
# down the next four symbols of the password in the windows and turns
# the grille 90 degrees again. Then, they write down the following four
# symbols and turns the grille once more. Lastly, they write down the
# final four symbols of the password.
# The cipher grille and the ciphered password are represented as an
# array (tuple) of strings.
# Input: A cipher grille and a ciphered password as a tuples of strings.
# Output: The password as a string.

def recall_password(cipher_grille, ciphered_password):
    windows = []
    for i, row in enumerate(cipher_grille):
        for j, char in enumerate(row):
            if char=='X':
                windows.append((i, j))
    password = ""
    for n in range(4):
        for (i, j) in windows:
            password += ciphered_password[i][j]
        windows = rotate_windows(windows)
    return password

def rotate_windows(windows):
    rotated = []
    for (i, j) in windows:
        rotated.append((j, 3-i))
    rotated.sort()
    return rotated

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'
