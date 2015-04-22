# After reading this fragment Nicola wants to build his own 
# "Humpty Dumpty". As a basis he chooses the spheroid (read 
# more about it on Wikipedia). We know the height and the 
# width (in inches) for this spheroid. For the job at hand, 
# Nikola needs to know how much material is required.
# You can help him and create a function to calculate the 
# volume (cubic inches) and the surface area (square inches).
# Input: Two arguments. A height and a width as integers.
# Output: The volume and the surface area as a list of floats. 
# The results should be accurate to two decimals.
# Precondition: 0 < width < 100
# 0 < height < 100

import math

def checkio(height, width):
    c = height/2.0
    a = width/2.0
    if c < a:
        # Oblate spheroid
        e = math.sqrt(1 - c**2/a**2)
        area = 2*math.pi*a**2*(1 + ((1 - e**2)/e)*math.atanh(e))
    elif c > a:
        # Prolate spheroid
        e = math.sqrt(1 - a**2/c**2)
        area = 2*math.pi*a**2*(1 + (c/(a*e))*math.asin(e))
    else:
        # Sphere
        area  = 4*math.pi*a**2
    volume = (4*math.pi*a**2*c)/3
    # Restrict to two decimal places
    area = round(area, 2)
    volume = round(volume, 2)
    return [volume, area]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 2) == [8.38, 21.48], "Prolate spheroid"
    assert checkio(2, 2) == [4.19, 12.57], "Sphere"
    assert checkio(2, 4) == [16.76, 34.69], "Oblate spheroid"
