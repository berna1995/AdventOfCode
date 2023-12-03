import sys
import string
from typing import Tuple
from collections import defaultdict


def get_gears_positions_around(
    matrix: list[str], i: int, j: int
) -> list[Tuple[int, int]]:
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
            if char == "*":
                neighbours.append((x, y))
        except IndexError:
            continue
    return neighbours


num_sum = 0

with open(sys.argv[1], "r") as file:
    matrix = list(map(lambda x: x.strip(), file.readlines()))

# map of (gearx, geary) -> [num0, num1, ..., numn]
gear_neighbours_map = defaultdict(lambda: [])

for i in range(0, len(matrix)):
    current_num_chars: str = ""
    tmp_gears_found_loc = set()
    for j in range(0, len(matrix[i])):
        current_char = matrix[i][j]
        if current_char in string.digits:
            current_num_chars = current_num_chars + current_char
            tmp_gears_found_loc.update(get_gears_positions_around(matrix, i, j))
            if j == len(matrix[i]) - 1:
                for gear_pos in tmp_gears_found_loc:
                    gear_neighbours_map[gear_pos].append(int(current_num_chars))
        elif len(current_num_chars):
            for gear_pos in tmp_gears_found_loc:
                gear_neighbours_map[gear_pos].append(int(current_num_chars))
            current_num_chars = ""
            tmp_gears_found_loc.clear()

gear_ratios_sum = 0

for gear_pos in gear_neighbours_map.keys():
    if len(gear_neighbours_map[gear_pos]) == 2:
        gear1, gear2 = gear_neighbours_map[gear_pos]
        gear_ratios_sum += gear1 * gear2

print(gear_ratios_sum)
