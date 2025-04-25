from collections import defaultdict

with open('input', 'r') as f:
    lines = f.readlines()

# key is before, values must be after
priority_dict = defaultdict(set)

middle_page_acc = 0

for line in lines:
    if '|' in line:
        left, right = line.strip().split('|')
        priority_dict[int(left)].add(int(right))
    elif line.strip() != '':
        value_list = list(map(int, line.strip().split(',')))
        valid = True
        for i in range(len(value_list) - 1, 1, -1):
            before_set = set(value_list[0:i-1])
            not_before = priority_dict[value_list[i]]
            if len(before_set.intersection(not_before)) > 0:
                valid = False
                break

        if not valid:
            continue

        middle_page_acc += value_list[len(value_list) // 2]

print(middle_page_acc)