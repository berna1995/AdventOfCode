with open("input", "r") as f:
    current = 0
    max = 0
    while True:
        line = f.readline()
        if not line:
            break

        line = line.rstrip()
        if line == "":
            if current > max:
                max = current
            current = 0

        else:
            current += int(line)

print(max)
