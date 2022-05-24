energy_map = []


def neighbours(x, y, w, h):
    neigh = []
    leftOkay = x - 1 >= 0
    rightOkay = x + 1 < w
    bottomOkay = y + 1 < h
    topOkay = y - 1 >= 0
    if leftOkay:
        neigh.append((x - 1, y))
        if bottomOkay:
            neigh.append((x - 1, y + 1))
        if topOkay:
            neigh.append((x - 1, y - 1))
    if rightOkay:
        neigh.append((x + 1, y))
        if bottomOkay:
            neigh.append((x + 1, y + 1))
        if topOkay:
            neigh.append((x + 1, y - 1))
    if bottomOkay:
        neigh.append((x, y + 1))
    if topOkay:
        neigh.append((x, y - 1))
    return neigh


with open("input", "r") as file:
    for line in file.readlines():
        energy_map.append([int(char) for char in line.rstrip()])

steps = 100
map_h = len(energy_map)
map_w = len(energy_map[0])
steps = 0

while True:
    already_flashed_list = set()
    for x in range(map_w):
        for y in range(map_h):
            expand_energy = [(x, y)]
            while len(expand_energy) > 0:
                x0, y0 = expand_energy.pop()
                if (x0, y0) in already_flashed_list:
                    continue
                energy_map[y0][x0] += 1
                if energy_map[y0][x0] > 9:
                    already_flashed_list.add((x0, y0))
                    expand_energy.extend(neighbours(x0, y0, map_w, map_h))

    steps += 1
    flashed = 0

    for x in range(map_w):
        for y in range(map_h):
            if energy_map[y][x] > 9:
                flashed += 1
                energy_map[y][x] = 0

    if flashed == map_w * map_h:
        break

print(steps)
