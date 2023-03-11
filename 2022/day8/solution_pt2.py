def scenic_score(map, map_width, map_height, row, column):
    tree_len = map[row][column]

    # Left score
    left_score = column
    for col in range(column - 1, -1, -1):
        if map[row][col] >= tree_len:
            left_score = column - col
            break

    # Right score
    right_score = map_width - column - 1
    for col in range(column + 1, map_width):
        if map[row][col] >= tree_len:
            right_score = col - column
            break

    # Top score
    top_score = row
    for r in range(row - 1, -1, -1):
        if map[r][column] >= tree_len:
            top_score = row - r
            break

    # Bottom score
    bottom_score = map_height - row - 1
    for r in range(row + 1, map_height):
        if map[r][column] >= tree_len:
            bottom_score = r - row
            break

    return left_score * top_score * right_score * bottom_score


with open('input', 'r') as file:
    map = list()
    for line in file.readlines():
        parsed_row = list()
        for cell in line.strip():
            parsed_row.append(int(cell))
        map.append(parsed_row)

width = len(map[0])
height = len(map)

top_scenic_score = 0

for i in range(1, width - 1):
    for j in range(1, height - 1):
        top_scenic_score = max(
            top_scenic_score, scenic_score(map, width, height, i, j))

print(top_scenic_score)
