with open('input', 'r') as file:
    instructions = list(map(lambda x: x.strip(), file.readlines()))

origin = (0, 0)
rope_knots = list([origin] * 10)
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

    head_destination = (rope_knots[0][0] +
                        x_offset, rope_knots[0][1] + y_offset)

    while rope_knots[0] != head_destination:
        rope_knots_prev = rope_knots.copy()

        head_x, head_y = rope_knots[0]

        if x_step:
            head_x += x_step
        elif y_step:
            head_y += y_step

        rope_knots[0] = (head_x, head_y)

        for i in range(1, len(rope_knots)):
            knot_x, knot_y = rope_knots[i]
            following_x, following_y = rope_knots[i-1]
            diff_x = following_x - knot_x
            diff_y = following_y - knot_y

            if max(abs(diff_x), abs(diff_y)) > 1:
                if diff_x > 0:
                    knot_x += 1
                elif diff_x < 0:
                    knot_x -= 1
                if diff_y > 0:
                    knot_y += 1
                elif diff_y < 0:
                    knot_y -= 1

                rope_knots[i] = (knot_x, knot_y)

                if i == len(rope_knots) - 1:
                    tail_visited_locations.add(rope_knots[i])
            else:
                break

print(len(tail_visited_locations))
