import sys
import string

digits_sum = 0

with open(sys.argv[1], "r") as input:
    while True:
        line = input.readline()
        if not line:
            break

        digits_list = list(filter(lambda x: x in string.digits, line))
        digits_sum += int(digits_list[0] + digits_list[-1])

print(digits_sum)
