# If you rotate a lever, the other rotates in the same direction but
# with different speed.
# If you rotate the first, then the second is rotated f2 times faster,
# the third -- at the f3time faster.
# If you rotate the second, then the third is rotated s3 times faster,
# the first -- at the s1 time faster.
# If you rotate the third, then the first is rotated t1 times faster,
# the second -- at the t2 time faster.
# This correlation can be represented as a matrix 3x3 with 1 in the main
# diagonal.
# 1	f2	f3
# s1	1	s3
# t1	t2	1
# You can rotate the levers from -180 to +180 degrees only (but in
# interrelated mode it can be rotated more than 360 degrees). You can
# rotate each lever once in the following order: the first, the second,
# the third. After completing these rotations, the levers must be at 0,
# 225, 315.
# You are given a rotation matrix as a list of lists with positive
# integers and the unitary main diagonal. You should return a list of
# three integers -- the angles for each lever. The start position of the
# levers is [0, 0, 0].
# Input: A rotation matrix as a list of lists.
# Output: The angles as a list of integers.
# Precondition: |matrix| = 3x3

def checkio(matrix):
    f2 = matrix[0][1]
    f3 = matrix[0][2]
    s1 = matrix[1][0]
    s3 = matrix[1][2]
    t1 = matrix[2][0]
    t2 = matrix[2][1]
    for rot1 in range(-180, 181):
        for rot2 in range(-180, 181):
            for rot3 in range(-180, 181):
                if (rot1 + s1*rot2 + t1*rot3) % 360 == 0:
                    if (f2*rot1 + rot2 + t2*rot3) % 360 == 225:
                        if (f3*rot1 + s3*rot2 + rot3) % 360 == 315:
                            return [rot1, rot2, rot3]
    return None

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':

    def check_it(func, matrix):
        result = func(matrix)
        if not all(-180 <= el <= 180 for el in result):
            print("The angles must be in range from -180 to 180 inclusively.")
            return False
        f, s, t = result
        temp = [0, 0, 0]
        temp[0] += f
        temp[1] += matrix[0][1] * f
        temp[2] += matrix[0][2] * f

        temp[0] += matrix[1][0] * s
        temp[1] += s
        temp[2] += matrix[1][2] * s

        temp[0] += matrix[2][0] * t
        temp[1] += matrix[2][1] * t
        temp[2] += t
        temp = [n % 360 for n in temp]
        if temp == [0, 225, 315]:
            return True
        else:
            print("This is the wrong final position {0}.".format(temp))
            return False

    assert check_it(checkio,
                    [[1, 2, 3],
                     [3, 1, 2],
                     [2, 3, 1]]), "1st example"
    assert check_it(checkio,
                    [[1, 4, 2],
                     [2, 1, 2],
                     [2, 2, 1]]), "2nd example"
    assert check_it(checkio,
                    [[1, 2, 5],
                     [2, 1, 1],
                     [2, 5, 1]]), "3rd example"
