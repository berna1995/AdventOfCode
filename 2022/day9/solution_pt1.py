with open('input', 'r') as file:
    instructions = list(map(lambda x: x.strip(), file.readlines()))

origin = (0, 0)
head_location = origin
tail_location = origin
tail_visited_locations = set()
tail_visited_locations.add(origin)

for instruction in instructions:
    inst_list = instruction.split(' ')
    dir = inst_list[0]
    steps = int(inst_list[1])

    x_offset = steps if dir == "R" else -steps if dir == "L" else 0
    y_offset = steps if dir == "D" else -steps if dir == "U" else 0
    x_step = 1 if x_offset > 0 else -1 if x_offset < 0 else 0
    y_step = 1 if y_offset > 0 else -1 if y_offset < 0 else 0

    head_destination = (head_location[0] +
                        x_offset, head_location[1] + y_offset)

    while head_location != head_destination:
        head_x, head_y = head_location
        tail_x, tail_y = tail_location

        if x_step:
            head_x += x_step
        elif y_step:
            head_y += y_step

        diff_x = abs(head_x - tail_x)
        diff_y = abs(head_y - tail_y)

        if max(diff_x, diff_y) > 1:
            if x_step:
                tail_x += x_step
                if diff_y:
                    tail_y = head_y
            elif y_step:
                tail_y += y_step
                if diff_x:
                    tail_x = head_x

            tail_location = (tail_x, tail_y)
            tail_visited_locations.add(tail_location)

        head_location = (head_x, head_y)

print(len(tail_visited_locations))
