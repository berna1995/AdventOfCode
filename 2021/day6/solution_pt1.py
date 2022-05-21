import sys

with open("input", "r") as file:
    timers = list(map(int, file.readline().rstrip().split(",")))

days = int(sys.argv[1])

for _ in range(0, days):
    for i in range(0, len(timers)):
        timers[i] -= 1
        if timers[i] < 0:
            timers[i] = 6
            timers.append(8)

print(len(timers))
