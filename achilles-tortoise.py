# You are given A1 and T2’s speed in m/s as well as the length of the
# advantage T2 has in seconds. Try to count the time when from when A1
# come abreast with T2 (count from T2 start). The result should be given
# in seconds.
# Input: Three arguments. Speeds of A1 and T2 and advantage as integers.
# Output: The time when A1 catch up T2 (count from T2 start) as an
# integer or float.
# Precondition:
# t2_speed < a1_speed < 343
# 0 < advantage <= 60

def chase(a1_speed, t2_speed, advantage):
    return float(advantage*a1_speed)/(a1_speed - t2_speed)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision
    
    assert almost_equal(chase(6, 3, 2), 4, 8), "example"
    assert almost_equal(chase(10, 1, 10), 11.111111111, 8), "long number"

