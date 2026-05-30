import sys

# Assumption: numbers are unique
def main() -> None: 
    file = sys.argv[1]
    print(f"Loading file {file}...")

    with open(file, 'r') as f:
        number_set = set([int(l.strip()) for l in f.readlines()])

    for number in number_set:
        to_find = 2020 - number
        if to_find in number_set:
            print(to_find * number)
            sys.exit(0)


if __name__ == "__main__":
    main()