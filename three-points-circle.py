# You should find the circle for three given points, such that the
# circle lies through these point and return the result as a string with
# the equation of the circle. In a Cartesian coordinate system (with an
# X and Y axis), the circle with central coordinates of (x0,y0) and
# radius of r can be described with the following equation:
#     "(x-x0)^2+(y-y0)^2=r^2"
# where x0,y0,r are decimal numbers rounded to two decimal
# points. Remove extraneous zeros and all decimal points, they are not
# necessary. For rounding, use the standard mathematical rules.
# Input: Coordinates as a string..
# Output: The equation of the circle as a string.
# Precondition: All three given points do not lie on one line.
# 0 < xi, yi, r < 10

import math

def checkio(data):
    x1, y1, x2, y2, x3, y3 = map(float, data.replace('(','').replace(')','').split(','))
    if y1 == y3:
        x3, x2 = x2, x3
        y3, y2 = y2, y3
    c1 = (x1**2 - x3**2 + y1**2 - y3**2)/(2*(y1 - y3))
    c2 = (x3 - x1)/(y1 - y3)
    x0 = (y2**2 - y1**2 + x2**2 - x1**2 + 2*(y1 - y2)*c1)/(2*(x2 - x1) + 2*(y2 - y1)*c2)
    y0 = c1 + c2*x0
    r = math.sqrt((x1 - x0)**2 + (y1 - y0)**2)
    x0 = round(x0, 2)
    y0 = round(y0, 2)
    r = round(r, 2)
    return "(x-%g)^2+(y-%g)^2=%g^2" % (x0, y0, r)
    

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"(2,2),(6,2),(2,6)") == "(x-4)^2+(y-4)^2=2.83^2"
    assert checkio(u"(3,7),(6,9),(9,7)") == "(x-6)^2+(y-5.75)^2=3.25^2"
