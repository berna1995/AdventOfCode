import sys
import itertools
import math

# Things deducted from input and playing around:
# - Every node ending with A map to 1 and 1 only Z node in his loop
# - The distance between the Z node finding for each starting element is constant, there's some sort of loop, but not to the first element
# - Also, the input looks like is made so that the distance to reach the first element Z from any starting point A is the same to get to the next Z element

# Those things couldn't be deducted from the text and i guess the algorithm couldn't be applied to any input.

with open(sys.argv[1], "r") as file:
    instructions = file.readline().strip()
    repeating_intructions = itertools.cycle(instructions)
    file.readline()
    route_options = dict()
    for line in file:
        src, routes = line.strip().split(" = ")
        lroute, rroute = (
            routes.replace("(", "").replace(")", "").replace(",", "").split(" ")
        )
        route_options[src] = (lroute, rroute)

    current_nodes = [node for node in route_options.keys() if node[-1] == "A"]
    first_z_node = {i: 0 for i in range(len(current_nodes))}
    steps = 0

    while any(map(lambda val: val == 0, first_z_node.values())):
        instruction = next(repeating_intructions)
        for i, node in enumerate(current_nodes):
            current_nodes[i] = (
                route_options[node][0] if instruction == "L" else route_options[node][1]
            )
            if current_nodes[i][-1] == "Z" and first_z_node[i] == 0:
                first_z_node[i] = steps + 1
        steps += 1

    print(math.lcm(*first_z_node.values()))
