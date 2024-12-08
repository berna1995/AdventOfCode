import re

with open('input', 'r') as file:
    lines = file.readlines()

aggregator = 0
instruction_enabled = True

for line in lines:
    for m in re.finditer(r"do\(\)|don't\(\)|mul\((\d{1,3}),(\d{1,3})\)", line):
        match m.group():
            case 'do()':
                instruction_enabled = True
            case 'don\'t()':
                instruction_enabled = False
            case _:
                if instruction_enabled:
                    x,y = map(int, m.groups())
                    aggregator += x * y
                    
print(aggregator)


