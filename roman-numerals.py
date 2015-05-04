# For this task, you should return a roman numeral using the specified
# integer value ranging from 1 to 3999.
# Input: A number as an integer.
# Output: The Roman numeral as a string.
# Precondition: 0 < number < 4000

def checkio(data):
    roman = ''
    roman += convertDigit(data/1000, 'M', 'invalid', 'invalid')
    data %= 1000
    roman += convertDigit(data/100, 'C', 'D', 'M')
    data %= 100
    roman += convertDigit(data/10, 'X', 'L', 'C')
    data %= 10
    roman += convertDigit(data, 'I', 'V', 'X')
    return roman

def convertDigit(digit, ones_char, fives_char, tens_char):
    if digit <= 3:
        return digit*ones_char
    elif digit == 4:
        return ones_char + fives_char
    elif digit <= 8:
        return fives_char + (digit-5)*ones_char
    else:
        return (10-digit)*ones_char + tens_char
    

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
