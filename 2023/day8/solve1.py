import sys
import itertools

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

    current_node = "AAA"
    end_node = "ZZZ"
    steps = 0

    while current_node != end_node:
        instruction = next(repeating_intructions)
        current_node = (
            route_options[current_node][0]
            if instruction == "L"
            else route_options[current_node][1]
        )
        steps += 1

    print(steps)
