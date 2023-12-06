import sys
import math

# Solution based on disequation x * (t - x) > d
# where: x is the time to 'charge'
#        t is the input record time
#        d is the input record distance

with open(sys.argv[1], 'r') as file:
    t = int(''.join(file.readline()[7:].strip().split(' ')))
    d = int(''.join(file.readline()[9:].strip().split(' ')))

l = 0.5 * (t - math.sqrt(math.pow(t, 2) - (4 * d)))
r = 0.5 * (t + math.sqrt(math.pow(t, 2) - (4 * d)))
print(math.trunc(r) - math.trunc(l))
