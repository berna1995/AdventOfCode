import re

with open('input', 'r') as file:
    lines = file.readlines()

aggregator = 0

for line in lines:
    matches = [x.groups() for x in re.finditer(r"mul\((\d{1,3}),(\d{1,3})\)", line)]
    for match in matches:
        x,y = int(match[0]), int(match[1])
        aggregator += x * y

print(aggregator)

