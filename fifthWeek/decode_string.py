def decodeString(self, s: str) -> str:
    current_string = ''
    current_number = 0
    stack = []
    for c in s:
        if c.isdigit():
            current_number = current_numbet * 10 + int(c)
        elif c == '[':
            stack.append(current_string)
            stack.append(current_number)
            current_string = ''
            current_number = 0
        elif c == ']':
            repeat_number = stack.pop()
            previous_string = stack.pop()
            current_string = previous_string + previous_string * repeat_number
        else:
            current_string += c

    return current_string


