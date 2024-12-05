from collections import defaultdict

with open('input', 'r') as file:
    lines = file.readlines()

left_list = []
right_occurencies = defaultdict(lambda: 0)

for line in lines:
    left, right = line.split('   ')
    left_list.append(int(left))
    right_occurencies[int(right)] += 1

result = sum([val*right_occurencies[val] for val in left_list])
print(result)
