with open("input.txt", "r") as f:
    lines = f.readlines()

location = 50
zeroes = 0

for line in lines:
    dir = line[0]
    mov = int(line[1:])

    if dir == "L":
        mov = -mov

    location += mov

    # no need to calculate actual position and handle negatives.
    # if it stops on zero, location mod 100 is 0
    if location % 100 == 0:
        zeroes += 1

print(zeroes)
