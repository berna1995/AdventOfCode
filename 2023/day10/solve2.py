import sys


def find_source(matrix) -> tuple[int, int] | None:
    for row, line in enumerate(matrix):
        try:
            source_pos = line.index("S")
            return (row, source_pos)
        except ValueError:
            continue
    return None


def infer_source_type(matrix, src_pos: tuple[int, int]) -> str:
    src_r, src_c = src_pos
    top_type = matrix[src_r - 1][src_c] if src_r != 0 else None
    bottom_type = matrix[src_r + 1][src_c] if src_r != len(matrix) - 1 else None
    left_type = matrix[src_r][src_c - 1] if src_c != 0 else None
    right_type = matrix[src_r][src_c + 1] if src_c != len(matrix[src_r]) - 1 else None

    match top_type:
        case "|" | "F" | "7":
            if left_type == "-" or left_type == "F" or left_type == "L":
                return "J"
            elif right_type == "-" or right_type == "J" or right_type == "7":
                return "L"
            elif bottom_type == "|" or bottom_type == "J" or bottom_type == "L":
                return "|"

    match bottom_type:
        case "|" | "J" | "L":
            if left_type == "-" or left_type == "F" or left_type == "L":
                return "7"
            elif right_type == "-" or right_type == "J" or right_type == "7":
                return "F"

    match left_type:
        case "-" | "F" | "L":
            if right_type == "-" or right_type == "J" or right_type == "7":
                return "-"

    return None


def loop_nav(
    matrix, src_pos: tuple[int, int], dst_pos: tuple[int, int]
) -> tuple[int, int]:
    delta_y, delta_x = dst_pos[0] - src_pos[0], dst_pos[1] - src_pos[1]
    match matrix[dst_pos[0]][dst_pos[1]]:
        case "|":
            return (dst_pos[0] + delta_y, dst_pos[1])
        case "-":
            return (dst_pos[0], delta_x + dst_pos[1])
        case "F":
            return (
                (dst_pos[0], 1 + dst_pos[1])
                if delta_y != 0
                else (dst_pos[0] + 1, dst_pos[1])
            )
        case "7":
            return (
                (dst_pos[0], dst_pos[1] - 1)
                if delta_y != 0
                else (dst_pos[0] + 1, dst_pos[1])
            )
        case "J":
            return (
                (dst_pos[0], dst_pos[1] - 1)
                if delta_y != 0
                else (dst_pos[0] - 1, dst_pos[1])
            )
        case "L":
            return (
                (dst_pos[0], dst_pos[1] + 1)
                if delta_y != 0
                else (dst_pos[0] - 1, dst_pos[1])
            )
        case _:
            return None


def intersection_points_r(matrix, source_pt, polygon_pts) -> int:
    src_row, src_col = source_pt
    matrix_cols = len(matrix[0])
    intersection_points = 0

    for col in range(src_col, matrix_cols):
        if (src_row, col) in polygon_pts:
            if matrix[src_row][col] in ['J', 'L', '|']:
                intersection_points += 1

    return intersection_points


with open(sys.argv[1], "r") as file:
    matrix = list(map(lambda line: list(line.strip()), file.readlines()))
    rows = len(matrix)
    cols = len(matrix[0])
    src_row, src_col = find_source(matrix)

    matrix[src_row][src_col] = infer_source_type(matrix, (src_row, src_col))

    dst_pos = (-1, -1)

    match matrix[src_row][src_col]:
        case "-" | "F":
            dst_pos = (src_row, src_col + 1)
        case "|" | "J" | "L":
            dst_pos = (src_row - 1, src_col)
        case "7":
            dst_pos = (src_row, src_col - 1)

    current_pos = (src_row, src_col)
    loop_nodes = set()

    min_row = src_row
    max_row = src_row
    min_col = src_col
    max_col = src_col

    while len(loop_nodes) == 0 or current_pos != (src_row, src_col):
        next_pos = loop_nav(matrix, current_pos, dst_pos)
        current_pos = dst_pos
        loop_nodes.add(dst_pos)
        min_row = min(min_row, dst_pos[0])
        max_row = max(max_row, dst_pos[0])
        min_col = min(min_col, dst_pos[1])
        max_col = max(max_col, dst_pos[1])
        dst_pos = next_pos

    dot_inside_loop = 0

    for i in range(min_row + 1, max_row):
        for j in range(min_col + 1, max_col):
            if (
                (i,j) not in loop_nodes and intersection_points_r(matrix, (i, j), loop_nodes) % 2 == 1
            ):
                dot_inside_loop += 1

    print(dot_inside_loop)
