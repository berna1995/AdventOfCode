from collections import defaultdict
import sys

days = int(sys.argv[1])

with open("input", "r") as file:
    timers = list(map(int, file.readline().rstrip().split(",")))

timers_freq = defaultdict(lambda: 0)
for timer in timers:
    timers_freq[timer] += 1

for _ in range(0, days):
    for num in range(0, 9):
        timers_freq[num-1] = timers_freq[num]
    timers_freq[8] = timers_freq[-1]
    timers_freq[6] = timers_freq[6] + timers_freq[-1]
    timers_freq[-1] = 0

res = sum(timers_freq.values())
print(res)
