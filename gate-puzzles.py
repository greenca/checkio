# You are given a message. You need to pick out all words (a consecutive
# sequence of letters or a single letter), calculate the "likeness"
# coefficients with other words, take an average of them and choose the
# greatest. Count "likeness" coefficient even for the same words (of
# course it's 100). If several words have the same resulting value, then
# choose the word closest to the end of the message. Words in the
# message can be separated by whitespaces and punctuation. There are no
# numbers.
# "Likeness" coefficient for two words is measured in percentages using
# the following rules:
# - Letter case does not matter ("A" == "a");
# - If the first letters of the words are equal, then add 10%;
# - If the last letters of the words are equal, then add 10%;
# - Add length comparison as 
# (length_of_word1 / length_of_word2) * 30%, if length_of_word1 ≤ length_of_word2;
# , else (length_of_word2 / length_of_word1) * 30%
# - Take all unique letters from the both words in one set and count how
#   many letters appear in the both words. Add to the coefficient
#   (common_letter_number / unique_letters_numbers) * 50;
# Input: A message as a string (unicode)
# Output: The keyword as a string.
# Precondition:
# 0 < len(message)
# all(x in (string.ascii_letters + string.punctuation + " ") for x in message)

import re

def find_word(message):
    words = re.split('\W+', message.lower())
    words.reverse()
    avg_like = []
    for word1 in words:
        likenesses = [likeness(word1, word2) for word2 in words]
        avg_like.append(sum(likenesses)/len(likenesses))
    return words[avg_like.index(max(avg_like))]

def likeness(word1, word2):
    if not word1 or not word2:
        return 0
    like = 0
    if word1[0] == word2[0]:
        like += 10
    if word1[-1] == word2[-1]:
        like += 10
    if len(word1) <= len(word2):
        like += 30.0*len(word1)/len(word2)
    else:
        like += 30.0*len(word2)/len(word1)
    unique_letters = len(set(word1).union(set(word2)))
    common_letters = len(set(word1).intersection(set(word2)))
    like += 50.0*common_letters/unique_letters
    return like

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_word(u"Speak friend and enter.") == "friend", "Friend"
    assert find_word(u"Beard and Bread") == "bread", "Bread is Beard"
    assert find_word(u"The Doors of Durin, Lord of Moria. Speak friend and enter. "
                     u"I Narvi made them. Celebrimbor of Hollin drew these signs") == "durin", "Durin"
    assert find_word(u"Aoccdrnig to a rscheearch at Cmabrigde Uinervtisy."
                     u" According to a researcher at Cambridge University.") == "according", "Research"
    assert find_word(u"One, two, two, three, three, three.") == "three", "Repeating"
