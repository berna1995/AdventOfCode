import sys

digit_map = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
}

digits_sum = 0

with open(sys.argv[1], "r") as input:
    while True:
        line = input.readline()
        if not line:
            break
        first_digit = min(
            filter(
                lambda tup: tup[1] != -1,
                map(lambda x: (digit_map[x], line.find(x)), digit_map.keys()),
            ),
            key=lambda tup: tup[1],
        )[0]

        last_digit = max(
            filter(
                lambda tup: tup[1] != -1,
                map(lambda x: (digit_map[x], line.rfind(x)), digit_map.keys()),
            ),
            key=lambda tup: tup[1],
        )[0]

        digits_sum += 10 * first_digit + last_digit

print(digits_sum)
