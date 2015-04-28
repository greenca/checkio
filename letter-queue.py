# You are given a sequence of commands:
# - "PUSH X" -- enqueue X, where X is a letter in uppercase.
# - "POP" -- dequeue the front position. if the queue is empty, then do
#   nothing.
# The queue can only contain letters.
# You should process all commands and assemble letters which remain in
# the queue in one word from the front to the rear of the queue.
# Input: A sequence of commands as a list of strings.
# Output: The queue remaining as a string.
# Precondition:
# 0 ≤ len(commands) ≤ 30;
# all(re.match("\APUSH [A-Z]\Z", c) or re.match("\APOP\Z", c) for c in commands)

def letter_queue(commands):
    queue = []
    for command in commands:
        command_vec = command.split()
        if command_vec[0] == 'PUSH':
            queue.append(command_vec[1])
        elif command_vec[0] == 'POP':
            if queue:
                queue.pop(0)
    return "".join(queue)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert letter_queue(["PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T"]) == "DOT", "dot example"
    assert letter_queue(["POP", "POP"]) == "", "Pop, Pop, empty"
    assert letter_queue(["PUSH H", "PUSH I"]) == "HI", "Hi!"
    assert letter_queue([]) == "", "Nothing"
