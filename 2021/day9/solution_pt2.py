from collections import deque
from functools import total_ordering

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


def dfs_basin_size(x, y, w, h, visited):
    if (x, y) in visited:
        return 0

    visited.add((x, y))
    to_visit = [(x0, y0) for x0, y0 in adjiacents(
        x, y, w, h) if height_map[x0][y0] > height_map[x][y] and height_map[x0][y0] < 9]

    sum_to_visit = 0
    for x0, y0 in to_visit:
        sum_to_visit += dfs_basin_size(x0, y0, w, h, visited)

    return sum_to_visit + 1


with open("input", "r") as file:
    while(True):
        line = file.readline().rstrip()
        if not line:
            break
        height_map.append([int(character) for character in line])

map_w = len(height_map)
map_h = len(height_map[0])

basins_sizes = []

for x in range(0, map_w):
    for y in range(0, map_h):
        adj_coords = adjiacents(x, y, map_w, map_h)
        neighbours = [height_map[x0][y0] for x0, y0 in adj_coords]
        if height_map[x][y] < min(neighbours):
            basins_sizes.append(dfs_basin_size(x, y, map_w, map_h, set()))

basins_sizes.sort(reverse=True)
assert len(basins_sizes) >= 3

res = basins_sizes[0] * basins_sizes[1] * basins_sizes[2]
print(res)
