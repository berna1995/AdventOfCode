packages = list()

with open("input", "r") as f:
    current = 0
    while True:
        line = f.readline()
        if not line:
            break

        line = line.rstrip()
        if line == "":
            packages.append(current)
            current = 0

        else:
            current += int(line)

print(sum(sorted(packages, reverse=True)[:3]))
