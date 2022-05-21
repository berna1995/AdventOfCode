x = 0
depth = 0
aim = 0

with open("input", "r") as file:
    while True:
        line = file.readline()
        if not line:
            break

        command = line.split(" ")
        cmd_type = command[0]
        cmd_value = int(command[1])

        if cmd_type == "forward":
            x += cmd_value
            depth += aim * cmd_value
        elif cmd_type == "down":
            aim += cmd_value
        else:
            aim -= cmd_value


print(x * depth)
