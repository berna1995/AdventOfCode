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
            return (dst_pos[0], 1 + dst_pos[1]) if delta_y != 0 else (dst_pos[0] + 1, dst_pos[1])
        case "7":
            return (dst_pos[0], dst_pos[1] -1) if delta_y != 0 else (dst_pos[0] + 1, dst_pos[1])
        case "J":
            return (dst_pos[0], dst_pos[1] -1) if delta_y != 0 else (dst_pos[0] -1, dst_pos[1])
        case "L":
            return (dst_pos[0], dst_pos[1]+1) if delta_y != 0 else (dst_pos[0] -1, dst_pos[1])
        case _:
            return None


with open(sys.argv[1], "r") as file:
    matrix = list(map(lambda line: list(line.strip()), file.readlines()))
    rows = len(matrix)
    cols = len(matrix[0])
    src_row, src_col = find_source(matrix)

    print(f"source is at {src_row}:{src_col}")

    matrix[src_row][src_col] = infer_source_type(matrix, (src_row, src_col))

    print(f"source should be {matrix[src_row][src_col]}")

    dst_pos = (-1, -1)

    match matrix[src_row][src_col]:
        case "-" | "F":
            dst_pos = (src_row, src_col + 1)
        case "|" | "J" | "L":
            dst_pos = (src_row - 1, src_col)
        case "7":
            dst_pos = (src_row, src_col - 1)

    print(f"destination is {dst_pos}")

    current_pos = (src_row, src_col)
    loop_size = 0

    while loop_size == 0 or current_pos != (src_row, src_col):
        next_pos = loop_nav(matrix, current_pos, dst_pos)
        current_pos = dst_pos
        print(f"exploring {current_pos}: {matrix[current_pos[0]][current_pos[1]]}")
        dst_pos = next_pos
        loop_size += 1

    print(loop_size // 2)
