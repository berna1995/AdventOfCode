import sys

# Assumption: numbers are unique
def main() -> None: 
    file = sys.argv[1]
    print(f"Loading file {file}...")

    with open(file, 'r') as f:
        number_set = set([int(l.strip()) for l in f.readlines()])
        number_list = list(number_set)

    for i in range(len(number_list)):
        for j in range(1, len(number_list)):
            part_sum = number_list[i] + number_list[j]
            if part_sum >= 2020:
                continue
            to_find = 2020 - part_sum
            if to_find in number_set:
                print(number_list[i] * number_list[j] * to_find)
                sys.exit(0)


if __name__ == "__main__":
    main()