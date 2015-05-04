# We have an array of straight connections between drones. Each
# connection is represented as a string with two names of friends
# separated by hyphen. For example: "dr101-mr99" means what the dr101
# and mr99 are friends. Your should write a function that allow
# determine more complex connection between drones. You are given two
# names also. Try to determine if they are related through common bonds
# by any depth. For example: if two drones have a common friends or
# friends who have common friends and so on.
# Input: Three arguments: Information about friends as a tuple of
# strings; first name as a string; second name as a string.
# Output: Are these drones related or not as a boolean.
# Precondition: len(network) ≤ 45
# if "name1-name2" in network, then "name2-name1" not in network
# 3 ≤ len(drone_name) ≤ 6
# first_name and second_name in network.

def check_connection(network, first, second):
    friends = {}
    for pair_str in network:
        pair = pair_str.split('-')
        friends[pair[0]] = friends.get(pair[0], []) + [pair[1]]
        friends[pair[1]] = friends.get(pair[1], []) + [pair[0]]
    friend_stack = friends[first]
    all_friends = set(friend_stack)
    while friend_stack:
        if second in all_friends:
            return True
        curr_friend = friend_stack.pop()
        for connection in friends[curr_friend]:
            if connection not in all_friends:
                friend_stack.append(connection)
                all_friends.add(connection)        
    return False


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") == True, "Scout Brotherhood"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2") == True, "Super Scout"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") == False, "I don't know any scouts."
