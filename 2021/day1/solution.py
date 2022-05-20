i = 0
prev_num = -1
num = 0
up_count = 0

with open("input", "r") as file:
    while True:
        if i > 0:
            prev_num = num

        line = file.readline()
        if not line:
            break

        num = int(line)

        if i > 0:
            if num > prev_num:
                up_count += 1

        i += 1

print(up_count)
