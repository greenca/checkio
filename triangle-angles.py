# Input: The lengths of the sides of a triangle as integers.
# Output: Angles of a triangle in degrees as sorted list of integers.
# Precondition: 
# 0 < a,b,c ≤ 1000

import math

def checkio(a, b, c):
    # Check triangle validity
    if (max(a,b,c) >= sum([a,b,c]) - max(a,b,c)) or min(a,b,c) <= 0:
        return [0, 0, 0]

    # Law of Cosines
    alpha = math.acos(float(b**2 + c**2 - a**2)/(2*b*c))
    beta = math.acos(float(a**2 + c**2 - b**2)/(2*a*c))
    gamma = math.acos(float(a**2 + b**2 - c**2)/(2*a*b))
    
    # Sort, convert and round
    angles = [alpha, beta, gamma]
    angles = map(math.degrees, angles)
    angles.sort()
    angles = map(round, angles)
    angles = map(int, angles)

    return angles


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"
