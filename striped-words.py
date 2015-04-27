# You are given a block of text with different words. These words are
# separated by white-spaces and punctuation marks. Numbers are not
# considered words in this mission (a mix of letters and digits is not a
# word either). You should count the number of words (striped words)
# where the vowels with consonants are alternating, that is; words that
# you count cannot have two consecutive vowels or consonants. The words
# consisting of a single letter are not striped -- do not count
# those. Casing is not significant for this mission.
# Input: A text as a string (unicode)
# Output: A quantity of striped words as an integer.
# Precondition:The text contains only ASCII symbols.
# 0 < len(text) < 105

import re

VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"

def checkio(text):
    words = re.split('\W+', text)
    striped_words = 0
    for word in words:
        striped_words += isStriped(word.upper())
    return striped_words

def isStriped(word):
    # Exclude words without at least one vowel and one consonant
    if len([c for c in word if c in VOWELS]) + len([c for c in word if c in CONSONANTS]) < 2:
        return False

    # Exclude words containing numbers
    if len([c for c in word if c.isdigit()]) > 0:
        return False

    # Compare each letter to the previous
    prev_char = ''
    for c in word:
        if prev_char:
            if (prev_char in VOWELS and c in VOWELS) or (prev_char in CONSONANTS and c in CONSONANTS):
                return False
        if c in VOWELS or c in CONSONANTS:
            prev_char = c

    return True

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"My name is ...") == 3, "All words are striped"
    assert checkio(u"Hello world") == 0, "No one"
    assert checkio(u"A quantity of striped words.") == 1, "Only of"
    assert checkio(u"Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
