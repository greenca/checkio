# You are given a rhyme (a multiline string), in which lines 
# are separated by "newline" (\n). Casing does not matter 
# for your search, but whitespaces should be removed before 
# your search. You should find the word inside the rhyme in 
# the horizontal (from left to right) or vertical (from up 
# to down) lines. For this you need envision the rhyme as a 
# matrix (2D array). Find the coordinates of the word in the 
# cut rhyme (without whitespaces).
# The result must be represented as a list -- 
# [row_start,column_start,row_end,column_end], where
# row_start is the line number for the first letter of the word.
# column_start is the column number for the first letter of the word.
# row_end is the line number for the last letter of the word.
# column_end is the line number for the last letter of the word.
# Counting of the rows and columns start from 1.
# Input: Two arguments. A rhyme as a string and a word as a string (lowercase).
# Output: The coordinates of the word.
# Precondition: The word is given in lowercase
# 0 < |word| < 10
# 0 < |rhyme| < 300

def checkio(text, word):
    matrix_text = text.replace(' ', '').lower().split('\n')
    word_len = len(word)
    num_rows = len(matrix_text)

    # Check horizontal
    for row_num, text_line in enumerate(matrix_text):
        for col_num in range(len(text_line)-word_len):
            if text_line[col_num:col_num+word_len] == word:
                return [row_num+1, col_num+1, row_num+1, col_num+word_len]

    # Check vertical
    for row_num in range(num_rows - word_len + 1):
        min_len = min([len(matrix_text[i]) for i in range(row_num, row_num+word_len)])
        for col_num in range(min_len):
            vertical = ''.join([matrix_text[i][col_num] for i in range(row_num, row_num+word_len)])
            if vertical == word:
                return [row_num+1, col_num+1, row_num+word_len, col_num+1]
    return []

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"""DREAMING of apples on a wall,
And dreaming often, dear,
I dreamed that, if I counted all,
-How many would appear?""", u"ten") == [2, 14, 2, 16]
    assert checkio(u"""He took his vorpal sword in hand:
Long time the manxome foe he sought--
So rested he by the Tumtum tree,
And stood awhile in thought.
And as in uffish thought he stood,
The Jabberwock, with eyes of flame,
Came whiffling through the tulgey wood,
And burbled as it came!""", u"noir") == [4, 16, 7, 16]
