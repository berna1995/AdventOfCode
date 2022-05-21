with open("input", "r") as file:
    numbers = list(map(int, file.readlines()))

inc = 0

for i in range(3, len(numbers)):
    win_1 = numbers[i-1] + numbers[i-2] + numbers[i-3]
    win_2 = numbers[i] + numbers[i-1] + numbers[i-2]
    if win_2 > win_1:
        inc += 1

print(inc)
