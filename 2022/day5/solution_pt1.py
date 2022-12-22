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
            for _ in range(0, how_many):
                crate = stacks[src].pop()
                stacks[dst].append(crate)
   
    for k in sorted(stacks.keys()):
        print(stacks[k][-1])
