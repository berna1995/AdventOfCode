with open('input', 'r') as file:
    lines = file.readlines()

left_list = []
right_list = []

for line in lines:
    left, right = line.split('   ')
    left_list.append(int(left))
    right_list.append(int(right))

left_list.sort()
right_list.sort()

result = sum([abs(a - b) for a, b in zip(left_list, right_list)])
print(result)
