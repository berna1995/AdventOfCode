import sys

def intersection(x, y):
    start_x, len_x = x
    start_y, len_y = y
    end_x = start_x + len_x - 1
    end_y = start_y + len_y - 1
    if (start_x >= start_y and start_x < end_y) or (end_x >= start_y and end_x < end_y):
        inter_start, inter_end = max(start_x, start_y), min(end_x, end_y)
        inter_size = inter_end - inter_start + 1
        inter_range = (inter_start, inter_size)
        if inter_size == len_x:
            return x,None
        leftover_size = len_x - inter_size
        if inter_start > start_x:
            return inter_range, (start_x, leftover_size)
        else:
            return inter_range, (end_y + 1, leftover_size)
    else:
        return None,x


with open(sys.argv[1], 'r') as file:
    seeds = list(map(int,file.readline().strip()[7:].split(' ')))
    seed_ranges = [(seeds[i],seeds[i+1]) for i in range(0, len(seeds), 2)]
    seed_ranges_new = []

    for line in file:
        if line == '\n':
            continue
        if 'map' in line:
            seed_ranges = seed_ranges + seed_ranges_new
            seed_ranges_new.clear()
            continue
        dst_start, src_start, size = list(map(int, line.strip().split(' ')))

        copies = []
        while len(seed_ranges) > 0:
            seed_start, seed_len = seed_ranges.pop(0)
            intersected, leftover = intersection((seed_start, seed_len), (src_start,size))
            if intersected:
                offset = dst_start - src_start
                inter_start, inter_size = intersected
                if not leftover:
                    seed_ranges_new.append((offset  + inter_start, inter_size))
                else:
                    leftover_start, leftover_size = leftover
                    seed_ranges_new.append((offset + inter_start, inter_size))
                    seed_ranges.append((leftover_start, leftover_size))
            else:
                copies.append((seed_start, seed_len))
        seed_ranges = copies
    
    seed_ranges = seed_ranges + seed_ranges_new
    seed_ranges_new.clear()

print(min([x[0] for x in seed_ranges]))