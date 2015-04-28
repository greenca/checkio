# You are given a text, which contains different english letters and
# punctuation symbols. You should find the most frequent letter in the
# text. The letter returned must be in lower case.
# While checking for the most wanted letter, casing does not matter, so
# for the purpose of your search, "A" == "a". Make sure you do not count
# punctuation symbols, digits and whitespaces, only letters.
# If you have two or more letters with the same frequency, then return
# the letter which comes first in the latin alphabet. For example --
# "one" contains "o", "n", "e" only once for each, thus we choose "e".
# Input: A text for analysis as a string (unicode for py2.7).
# Output: The most frequent letter in lower case as a string.
# Precondition:
# A text contains only ASCII symbols.
# 0 < len(text) ≤ 105

def checkio(text):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    letter_counts = []
    for letter in letters:
        letter_counts.append(text.lower().count(letter))
    max_count = max(letter_counts)
    return letters[letter_counts.index(max_count)]


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(u"Hello World!") == "l", "Hello test"
    assert checkio(u"How do you do?") == "o", "O is most wanted"
    assert checkio(u"One") == "e", "All letter only once."
    assert checkio(u"Oops!") == "o", "Don't forget about lower case."
    assert checkio(u"AAaooo!!!!") == "a", "Only letters."
    assert checkio(u"abe") == "a", "The First."
    print("Start the long test")
    assert checkio(u"a" * 9000 + u"b" * 1000) == "a", "Long."
    print("The local tests are done.")
