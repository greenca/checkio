# All of the rings are numbered and you are told which of the rings are
# connected. This information is given as a sequence of sets. Each set
# describes the connected rings. For example: {1, 2} means that the 1st
# and 2nd rings are connected. You should count how many rings we need
# to break to get the maximum of separate rings. Each of the rings are
# numbered in a range from 1 to N, where N is total quantity of rings.
# Input: Information about the connected rings as a tuple of sets with
# integers.
# Output: The number of rings to break as an integer.
# Precondition: all(len(s) == 2 for s in rings)
# sorted(reduce(set.union, rings)) == list(range(1,
# max(reduce(set.union, rings)) + 1))

def break_rings(rings):
    minpath = len(reduce(set.union, rings))
    paths = [(0, rings)]
    while paths:
        curr_count, curr_rings = paths.pop()
        if curr_count < minpath:
            if not curr_rings:
                minpath = curr_count
            elif curr_count < minpath - 1:
                numlinks = {i: sum([i in pair for pair in curr_rings]) for i in reduce(set.union, curr_rings)}
                for ring in sorted(numlinks, key=numlinks.get):
                    if numlinks[ring] >= max(numlinks.values()) - 1:
                        remaining = [link for link in curr_rings if ring not in link]
                        paths.append((curr_count + 1, remaining))
    return minpath


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert break_rings(({1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {4, 6})) == 3, "example"
    assert break_rings(({1, 2}, {1, 3}, {1, 4}, {2, 3}, {2, 4}, {3, 4})) == 3, "All to all"
    assert break_rings(({5, 6}, {4, 5}, {3, 4}, {3, 2}, {2, 1}, {1, 6})) == 3, "Chain"
    assert break_rings(({8, 9}, {1, 9}, {1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {8, 7})) == 5, "Long chain"
