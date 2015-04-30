# The bird converts words by two rules:
# - after each consonant letter the bird appends a random vowel letter
#   (l ⇒ la or le);
# - after each vowel letter the bird appends two of the same letter (a ⇒
#   aaa);
# Vowels letters == "aeiouy".
# You are given an ornithological phrase as several words which are
# separated by white-spaces (each pair of words by one whitespace). The
# bird does not know how to punctuate its phrases and only speaks words
# as letters. All words are given in lowercase. You should translate
# this phrase from the bird language to something more understandable.
# Input: A bird phrase as a string.
# Output: The translation as a string.
# Precondition: re.match("\A([a-z]+\ ?)+(?<!\ )\Z", phrase)
# A phrase always has the translation.

VOWELS = "aeiouy"

def translate(phrase):
    words = phrase.split()
    translated_words = []
    for word in words:
        translated_words.append(translateWord(word))
    return ' '.join(translated_words)

def translateWord(word):
    char_list = list(word)
    translated_word = ''
    while char_list:
        curr_letter = char_list.pop(0)
        translated_word += curr_letter
        if curr_letter in VOWELS:
            char_list.pop(0)
            char_list.pop(0)
        else:
            char_list.pop(0)
    return translated_word

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate(u"hieeelalaooo") == "hello", "Hi!"
    assert translate(u"hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate(u"aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate(u"sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
