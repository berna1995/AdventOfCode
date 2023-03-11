def is_visible(map, map_width, map_height, row, column):
    tree_len = map[row][column]

    # Check from left
    visible = True
    for col in range(0, column):
        if map[row][col] >= tree_len:
            visible = False
            break

    if visible:
        return True

    # Check from right
    visible = True
    for col in range(map_width - 1, column, -1):
        if map[row][col] >= tree_len:
            visible = False
            break

    if visible:
        return True

    # Check from top
    visible = True
    for r in range(0, row):
        if map[r][column] >= tree_len:
            visible = False
            break

    if visible:
        return True

    # Check from bottom
    visible = True
    for r in range(map_height - 1, row, -1):
        if map[r][column] >= tree_len:
            visible = False
            break

    return visible


with open('input', 'r') as file:
    map = list()
    for line in file.readlines():
        parsed_row = list()
        for cell in line.strip():
            parsed_row.append(int(cell))
        map.append(parsed_row)

width = len(map[0])
height = len(map)

visible_trees = ((width + height) * 2) - 4

for i in range(1, width - 1):
    for j in range(1, height - 1):
        if(is_visible(map, width, height, i, j)):
            visible_trees += 1

print(visible_trees)
