with open("input", "r") as file:
    lines = file.readlines()

valid_reports = 0

for line in lines:
    values = list(map(int, line.split(" ")))
    diffs = [b - a for a, b in zip(values[:-1], values[1:])]
    if all(map(lambda x: abs(x) >= 1 and abs(x) <= 3, diffs)) and (
        all(map(lambda x: x > 0, diffs)) or all(map(lambda x: x < 0, diffs))
    ):
        valid_reports += 1

print(valid_reports)
