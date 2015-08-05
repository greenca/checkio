# Input: Three arguments. The number of dice, the number of sides per
# die and the target number as integers.
# Output: The probability of getting exactly target number on a single
# roll of the given dice as a float.
# Preconditions:
# 1 <= dice_number <= 10
# 2 <= sides <= 20
# 0 <= target < 1000

def probability(dice_number, sides, target):
    combinations = {0:1}
    for n in range(dice_number):
        prev_comb = combinations
        combinations = {}
        for i in range(1,sides+1):
            for k,v in prev_comb.items():
                combinations[k+i] = combinations.get(k+i,0) + v
    return float(combinations.get(target,0))/(sides**dice_number)

if __name__ == '__main__':
    #These are only used for self-checking and are not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=4):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision
        
    assert(almost_equal(probability(2, 6, 3), 0.0556)), "Basic example"
    assert(almost_equal(probability(2, 6, 4), 0.0833)), "More points"
    assert(almost_equal(probability(2, 6, 7), 0.1667)), "Maximum for two 6-sided dice"
    assert(almost_equal(probability(2, 3, 5), 0.2222)), "Small dice"
    assert(almost_equal(probability(2, 3, 7), 0.0000)), "Never!"
    assert(almost_equal(probability(3, 6, 7), 0.0694)), "Three dice"
    assert(almost_equal(probability(10, 10, 50), 0.0375)), "Many dice, many sides"
