opened = ['(', '[', '{', '<']
closed = [')', ']', '}', '>']

opened_to_closed = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

score_table = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}


def validate_line(line):
    stack = []
    for i in range(0, len(line)):
        char = line[i]
        if char in opened:
            stack.append(opened_to_closed[char])
        elif char in closed:
            if char == stack[-1]:
                stack.pop()
            else:
                return (i, stack[-1])
        else:
            raise Exception("invalid char")

    if len(stack) > 0:
        return stack

    return True


with open("input", "r") as file:
    lines = [line.rstrip() for line in file.readlines()]

score = 0

for line in lines:
    res = validate_line(line)
    if type(res) == bool:
        continue
    if type(res) == tuple:
        error_index, expected = res
        score += score_table[line[error_index]]
    else:
        continue

print(score)
