import bisect

with open('input') as file:
    lines = list(map(lambda line: line.strip(), file.readlines()))

cycle_counter = 1
register = 1
cycle_reg_list = [(cycle_counter, register)]

for line in lines:
    if line == 'noop':
        cycle_counter += 1
    else:
        op, val = line.split(' ')
        if op == 'addx':
            cycle_counter += 2
            register += int(val)
            cycle_reg_list.append((cycle_counter, register))
        else:
            print(f'Unrecognized operation: {op}')
            exit(-1)

interest_cycles = list(range(20, 240, 40))
signal_strength = 0

for cc in interest_cycles:
    cycles, reg_val = zip(*cycle_reg_list)
    idx = bisect.bisect(cycles, cc)
    if cycles[idx] > cc:
        idx -= 1

    signal_strength += reg_val[idx] * cc

print(signal_strength)
