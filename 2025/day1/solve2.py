with open("input.txt", "r") as f:
    lines = f.readlines()

location = 50
zeroes = 0

for line in lines:
    dir = line[0]
    mov = int(line[1:])

    # very stupid simulation, still using the mod trick,
    # can probably be made in a simpler and quicker way
    while mov != 0:
        location += -1 if dir == "L" else 1
        mov -= 1
        if location % 100 == 0:
            zeroes += 1

print(zeroes)
