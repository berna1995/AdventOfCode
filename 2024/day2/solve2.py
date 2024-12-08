from copy import deepcopy

def is_valid_solution(values):
    diffs = [b - a for a, b in zip(values[:-1], values[1:])]
    return all(map(lambda x: abs(x) >= 1 and abs(x) <= 3, diffs)) and (
        all(map(lambda x: x > 0, diffs)) or all(map(lambda x: x < 0, diffs))
    )


with open("input", "r") as file:
    lines = file.readlines()

valid_reports = 0

for line in lines:
    values = list(map(int, line.split(" ")))
    if is_valid_solution(values):
        valid_reports += 1
    else:
        diffs = [b - a for a, b in zip(values[:-1], values[1:])]
        increasing = len([d for d in diffs if d > 0]) > len(diffs) / 2
        invalid_indexes = [
                i
                for i, diff in enumerate(diffs)
                if abs(diff) < 1
                or abs(diff) > 3
                or (diff > 0 and not increasing)
                or (diff < 0 and increasing)
            ]
        if len(invalid_indexes) <= 2:
            for i in range(invalid_indexes[0]-1, invalid_indexes[0]+2):
                if i in range(0, len(values)):
                    values_copy = deepcopy(values)
                    values_copy.pop(i)
                    if is_valid_solution(values_copy):
                        valid_reports +=1
                        break


print(valid_reports)
