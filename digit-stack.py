# We will emulate the stack process with Python. 
# You are given a sequence of commands:
# - "PUSH X" -- add X in the stack, where X is a digit.
# - "POP" -- look and remove the top position. 
# If the stack is empty, then it returns 0 (zero) and does nothing.
# - "PEEK" -- look at the top position. 
# If the stack is empty, then it returns 0 (zero).
# The stack can only contain digits.
# You should process all commands and sum all digits which were 
# taken from the stack ("PEEK" or "POP"). Initial value of the 
# sum is 0 (zero).
# Input: A sequence of commands as a list of strings.
# Output: The sum of the taken digits as an integer.
# Precondition:
# 0 ≤ len(commands) ≤ 20;
# all(re.match("\APUSH \d\Z", c) or с == "POP" or c == "PEEK" for c in commands)

def digit_stack(commands):
    stack = []
    val = 0
    for command in commands:
        command_name = command.split()[0]
        if command_name == 'PUSH':
            stack.append(int(command.split()[1]))
        elif command_name == 'POP':
            if stack:
                val += stack.pop()
        elif command_name == 'PEEK':
            if stack:
                val += stack[-1]
        else:
            raise ValueError('Invalid command')
    return val

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert digit_stack(["PUSH 3", "POP", "POP", "PUSH 4", "PEEK",
                        "PUSH 9", "PUSH 0", "PEEK", "POP", "PUSH 1", "PEEK"]) == 8, "Example"
    assert digit_stack(["POP", "POP"]) == 0, "pop, pop, zero"
    assert digit_stack(["PUSH 9", "PUSH 9", "POP"]) == 9, "Push the button"
    assert digit_stack([]) == 0, "Nothing"
