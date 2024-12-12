def check_valid(matrix, start_i, start_j, i_delta, j_delta) -> bool:
    if matrix[start_i][start_j] != "X":
        return False
    string_to_find = "MAS"
    for i, c in enumerate(string_to_find):
        i_to_look = start_i + (i_delta * (i + 1))
        j_to_look = start_j + (j_delta * (i + 1))
        if i_to_look < 0 or i_to_look >= len(matrix):
            return False
        if j_to_look < 0 or j_to_look >= len(matrix[0]):
            return False
        if matrix[i_to_look][j_to_look] != c:
            return False
    return True


with open("input", "r") as file:
    matrix = file.readlines()

directions = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
words_found = 0

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        for x, y in directions:
            if check_valid(matrix, i, j, x, y):
                words_found += 1

print(words_found)