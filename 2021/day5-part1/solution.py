import re
import itertools

segments = []
grid = [[0 for _ in range(1000)] for i in range(1000)]

with open("input", "r") as file:
    while(True):
        line = file.readline().rstrip()
        if not line:
            break
        segments.append(tuple(map(int, re.split(",| -> ", line))))

for x0, y0, x1, y1 in segments:
    if x0 == x1:
        for y in range(min(y0, y1), max(y0, y1) + 1):
            grid[x0][y] += 1
    if y0 == y1:
        for x in range(min(x0, x1), max(x0, x1) + 1):
            grid[x][y0] += 1

res = len(list(filter(lambda x: x >= 2, itertools.chain(*grid))))
print(res)
