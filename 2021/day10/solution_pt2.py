opened = ['(', '[', '{', '<']
closed = [')', ']', '}', '>']

opened_to_closed = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

score_table = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
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

scores = []

for line in lines:
    res = validate_line(line)
    if type(res) == bool:
        continue
    if type(res) == tuple:
        continue
    else:
        score = 0
        while len(res) > 0:
            char = res.pop()
            score *= 5
            score += score_table[char]
        scores.append(score)

scores.sort()
mid_score = scores[len(scores)//2]
print(mid_score)
