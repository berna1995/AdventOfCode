import sys
import itertools

galaxy_offsets = 1 if int(sys.argv[1]) == 1 else 999999

with open(sys.argv[2], "r") as file:
    galaxies = []

    matrix = list(map(lambda x: x.strip(), file.readlines()))

    empty_rows = [True for _ in range(len(matrix))]
    empty_cols = [True for _ in range(len(matrix[0]))]

    for i, line in enumerate(matrix):
        for j, symbol in enumerate(line):
            if symbol == "#":
                empty_rows[i] = False
                empty_cols[j] = False
                galaxies.append((i, j))

    offset_rows, offset_cols = [], []
    empty_rows_cnt = 0
    empty_cols_cnt = 0

    for i, empty_row in enumerate(empty_rows):
        offset_rows.append(empty_rows_cnt)
        if empty_row:
            empty_rows_cnt += galaxy_offsets

    for i, empty_col in enumerate(empty_cols):
        offset_cols.append(empty_cols_cnt)
        if empty_col:
            empty_cols_cnt += galaxy_offsets

    galaxies = [(r + offset_rows[r], c + offset_cols[c]) for r, c in galaxies]

    distances_sum = sum(
        map(
            lambda pair: abs(pair[0][0] - pair[1][0]) + abs(pair[0][1] - pair[1][1]),
            itertools.combinations(galaxies, 2),
        )
    )
    
    print(distances_sum)
