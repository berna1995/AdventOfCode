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
    elif y0 == y1:
        for x in range(min(x0, x1), max(x0, x1) + 1):
            grid[x][y0] += 1
    else:
        l = max(abs(x0-x1), abs(y0-y1)) + 1
        for i in range(0, l):
            if x0 < x1 and y0 < y1:
                grid[x0+i][y0+i] += 1
            elif x0 > x1 and y0 > y1:
                grid[x0-i][y0-i] += 1
            elif x0 < x1 and y0 > y1:
                grid[x0+i][y0-i] += 1
            elif x0 > x1 and y0 < y1:
                grid[x0-i][y0+i] += 1


res = len(list(filter(lambda x: x >= 2, itertools.chain(*grid))))
print(res)
