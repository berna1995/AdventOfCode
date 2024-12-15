with open("input", "r") as file:
    matrix = [s.strip() for s in file.readlines()]

words_found = 0

for i in range(1, len(matrix) - 1):
    for j in range(1, len(matrix[i]) - 1):
        if matrix[i][j] == "A":
            l_cross = matrix[i - 1][j - 1] + "A" + matrix[i + 1][j + 1]
            r_cross = matrix[i - 1][j + 1] + "A" + matrix[i + 1][j - 1]
            if (l_cross == "MAS" or l_cross == "SAM") and (
                r_cross == "MAS" or r_cross == "SAM"
            ):
                words_found += 1
print(words_found)
