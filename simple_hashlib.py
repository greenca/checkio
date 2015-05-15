# Input: Two arguments. A string to be hashed and a hash algorithm as a
# string (unicode utf8).
# Output: Hexadecimal hash for for input string using given algorithm as
# a string.
# Precondition:
# algorithm in ("md5", "sha224", "sha256", "sha384", "sha512", "sha1")

import hashlib

def checkio(hashed_string, algorithm):
    return getattr(hashlib, algorithm)(hashed_string.encode('utf-8')).hexdigest()

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(u'welcome', 'md5') == '40be4e59b9a2a2b5dffb918c0e86b3d7'
    assert checkio(u'happy spam', 'sha224') == '6e9dc3e01d57f1598c2b40ce59fc3527e698c77b15d0840ae96a8b5e'
