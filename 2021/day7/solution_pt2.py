from collections import defaultdict

with open("input", "r") as file:
    posx = list(map(int, file.readline().split(",")))

frequencies = defaultdict(lambda: 0)
fuels_computations = defaultdict(lambda: 0)

for pos in posx:
    frequencies[pos] += 1

min_pos = min(posx)
max_pos = max(posx)

for source in frequencies.keys():
    for destination in range(min_pos, max_pos + 1):
        if source != destination:
            distance = abs(destination - source)
            cost = frequencies[source] * (((distance + 1) * (distance)) // 2)
            fuels_computations[destination] += cost

lowest_consumption = min(fuels_computations, key=fuels_computations.get)
print(fuels_computations[lowest_consumption])
