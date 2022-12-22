import re
from collections import defaultdict

with open('input', 'r') as f:

    instructions = False
    stacks = defaultdict(lambda: [])

    while True:
        line = f.readline().strip('\n')
        if instructions and not line:
            break

        if not instructions:
            if '[' in line:
                # crates status
                for i in range(1, len(line), 4):
                    if line[i] != ' ':
                        stacks[(i//4)].append(line[i])
            elif line == '':
                # after this start instructions
                instructions = True
                for s in stacks.values():
                    s.reverse()
            else:
                # stacks ids, ignore
                continue
        else:
            matches = re.match(r'move (\d+) from (\d+) to (\d+)', line)
            how_many = int(matches.group(1))
            src = int(matches.group(2)) - 1
            dst = int(matches.group(3)) - 1
            crates_to_move = stacks[src][-how_many:]
            stacks[src] = stacks[src][:-how_many]
            stacks[dst].extend(crates_to_move)
   
    for k in sorted(stacks.keys()):
        print(stacks[k][-1])
