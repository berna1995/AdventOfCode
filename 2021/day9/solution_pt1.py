height_map = []


def adjiacents(x, y, w, h):
    adj = []
    if x - 1 >= 0:
        adj.append((x-1, y))
    if x + 1 < w:
        adj.append((x+1, y))
    if y - 1 >= 0:
        adj.append((x, y-1))
    if y + 1 < h:
        adj.append((x, y+1))
    return adj


with open("input", "r") as file:
    while(True):
        line = file.readline().rstrip()
        if not line:
            break
        height_map.append([int(character) for character in line])

map_w = len(height_map)
map_h = len(height_map[0])
min_spots_sum = 0

for x in range(0, map_w):
    for y in range(0, map_h):
        adj_coords = adjiacents(x, y, map_w, map_h)
        neighbours = [height_map[x0][y0] for x0, y0 in adj_coords]
        if height_map[x][y] < min(neighbours):
            min_spots_sum += 1 + height_map[x][y]

print(min_spots_sum)
