import sys

with open(sys.argv[1], 'r') as file:
    seeds = set(map(int, file.readline().strip()[7:].split(' ')))
    seeds_new = set()

    while True:
        line = file.readline()
        if not line:
            seeds = seeds | seeds_new
            break
        if line == '\n':
            continue
        if 'map' in line:
            seeds = seeds | seeds_new
            seeds_new.clear()
            continue
        dst_start, src_start, size = list(map(int, line.strip().split(' ')))
        for seed in seeds.copy():
            if seed >= src_start and seed < src_start + size:
                seeds_new.add(dst_start - src_start + seed)
                seeds.remove(seed)

print(min(seeds))