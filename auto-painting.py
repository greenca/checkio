# Nicola has built a semi-automatized painting system, but this system
# can paint only one side of an item. After that, an operator must
# reload the machine and paint the other side (the system detects
# painted sides automatically). The painting process always takes the
# same amount of time. The camera can paint K surfaces at a time. Nicola
# wants Stephan to operate the painting machine and he needs to develop
# an algorithm for Stephan which will allow him to paint N (0 < N <= 10)
# surfaces in the shortest possible timeframe. Be careful that you don't
# paint the item more than two times.
# The items are numbered from 0 to 9. You are given the paint holding
# capacity of the machine (K) and the quantity of items (N). You should
# return the sequence Stephen must paint as a string, where each action
# is the numbers of painted items. Actions separated by comma (",").
# Input: Capacity of the painting system and quantity of items as
# integers.
# Output: The sequence of actions as a string.
# Precondition:
# 0 < capacity <= 10
# 0 < number <= 10

def checkio(capacity, number):
    unpainted = range(number)
    halfpainted = []
    painted = []
    action_seq = ""
    if capacity >= number:
        action_seq += ''.join([str(d) for d in range(number)])
        action_seq += ','
        action_seq += ''.join([str(d) for d in range(number)])
        painted = range(number)
    while len(painted) < number:
        if action_seq:
            action_seq += ","
        for k in range(capacity):
            target = ""
            if unpainted:
                target = unpainted.pop(0)
                halfpainted.append(target)
            elif halfpainted:
                target = halfpainted.pop(0)
                painted.append(target)
            action_seq += str(target)
    return action_seq


if __name__ == '__main__':
    #This part is using only for self-checking and not necessary for auto-testing
    def check_solution(func, k, n, max_steps):
        result = func(k, n)
        actions = result.split(",")
        if len(actions) > max_steps:
            print("It can be shorter.")
            return False
        details = [0] * n
        for act in actions:
            if len(act) > k:
                print("The system can contain {0} detail(s).".format(k))
                return False
            if len(set(act)) < len(act):
                print("You can not place one detail twice in one load")
                return False
            for ch in act:
                details[int(ch)] += 1
        if any(d < 2 for d in details):
            print("I see no painted details.")
            return False
        if any(d > 2 for d in details):
            print("I see over painted details.")
            return False
        return True

    assert check_solution(checkio, 2, 3, 3), "1st Example"
    assert check_solution(checkio, 6, 3, 2), "2nd Example"
    assert check_solution(checkio, 3, 6, 4), "3rd Example"
    assert check_solution(checkio, 1, 4, 8), "4th Example"
    assert check_solution(checkio, 2, 5, 5), "5th Example"
