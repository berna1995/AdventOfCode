from collections import defaultdict

with open("input", "r") as file:
    posx = list(map(int, file.readline().split(",")))

frequencies = defaultdict(lambda: 0)
fuels_computations = defaultdict(lambda: 0)

for pos in posx:
    frequencies[pos] += 1

for destination in frequencies.keys():
    for source in frequencies.keys():
        if source != destination:
            fuels_computations[destination] += frequencies[source] * \
                abs(destination - source)

lowest_consumption = min(fuels_computations, key=fuels_computations.get)
print(fuels_computations[lowest_consumption])
