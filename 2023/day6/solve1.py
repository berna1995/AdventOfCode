import sys

with open(sys.argv[1], 'r') as file:
    times = [int(x) for x in file.readline()[7:].strip().split(' ') if x != '']
    distances = [int(x) for x in file.readline()[9:].strip().split(' ') if x != '']


res = 1
for t,d in zip(times,distances):
    winning_ways = 0
    for ct in range(0, t):
        if ct * (t-ct) > d:
            winning_ways += 1
    print(winning_ways)
    res *= winning_ways

print(res)