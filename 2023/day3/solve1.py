import sys
import string


def get_symbols_around(matrix: list[str], i: int, j: int) -> list[str]:
    neighbours = []
    indexes = [
        (i - 1, j - 1),
        (i - 1, j),
        (i - 1, j + 1),
        (i, j - 1),
        (i, j + 1),
        (i + 1, j - 1),
        (i + 1, j),
        (i + 1, j + 1),
    ]
    for x, y in indexes:
        try:
            char = matrix[x][y]
            if char != "." and char not in string.digits:
                neighbours.append(char)
        except IndexError:
            continue
    return neighbours


num_sum = 0

with open(sys.argv[1], "r") as file:
    matrix = list(map(lambda x: x.strip(), file.readlines()))

for i in range(0, len(matrix)):
    has_symbol_near = False
    current_num_chars: str = ""
    for j in range(0, len(matrix[i])):
        current_char = matrix[i][j]
        if current_char in string.digits:
            current_num_chars = current_num_chars + current_char
            if not has_symbol_near and len(get_symbols_around(matrix, i, j)) > 0:
                has_symbol_near = True
        elif len(current_num_chars):
            if has_symbol_near:
                num_sum += int(current_num_chars)
            has_symbol_near = False
            current_num_chars = ""
        if len(current_num_chars) and j == len(matrix[i]) - 1:
            if has_symbol_near:
                num_sum += int(current_num_chars)

print(num_sum)
