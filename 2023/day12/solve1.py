import sys
import itertools


def validate_sequence(sequence: str, rule: list[int]) -> bool:
    i = 0

    for r in rule:
        i = sequence.find("#" * r, i)
        if i == -1:
            return False
        if i + r < len(sequence) and sequence[i + r] == "#":
            return False
        i += r + 1

    return True


with open(sys.argv[1], "r") as file:
    counter = 0

    for line in file:
        conf, rule = line.strip().split(" ")
        parsed_rule = list(map(int, rule.split(",")))
        unknown_count = conf.count("?")

        for unknown_seq in itertools.product(".#", repeat=unknown_count):
            line_char_list = list(conf)
            j = 0
            for i in range(len(line_char_list)):
                if line_char_list[i] == "?":
                    line_char_list[i] = unknown_seq[j]
                    j += 1
            if line_char_list.count("#") == sum(parsed_rule) and validate_sequence(
                "".join(line_char_list), parsed_rule
            ):
                counter += 1

    print(counter)
