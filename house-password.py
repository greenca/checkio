# The password will be considered strong enough if its length is greater
# than or equal to 10 symbols, it has at least one digit, as well as
# containing one uppercase letter and one lowercase letter in it. The
# password contains only ASCII latin letters or digits.  Input: A
# password as a string (Unicode for python 2.7).
# Output: Is the password safe or not as a boolean or any data type that
# can be converted and processed as a boolean. In the results you will
# see the converted results.
# Precondition:
# re.match("[a-zA-Z0-9]+", password)
# 0 < len(password) ≤ 64

def checkio(data):

    if len(data) < 10:
        return False

    nums = [d for d in data if d.isdigit()]
    if not nums:
        return False

    letters = [l for l in data if l.isalpha()]
    if not any([l.islower() for l in letters]):
        return False
    if not any([l.isupper() for l in letters]):
        return False

    return True




if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(u'A1213pokl') == False, "1st example"
    assert checkio(u'bAse730onE4') == True, "2nd example"
    assert checkio(u'asasasasasasasaas') == False, "3rd example"
    assert checkio(u'QWERTYqwerty') == False, "4th example"
    assert checkio(u'123456123456') == False, "5th example"
    assert checkio(u'QwErTy911poqqqq') == True, "6th example"
