import sys

score = 0

with open(sys.argv[1], 'r') as file:
    while True:
        line = file.readline()
        if not line:
            break
        _, numbers = line.strip().split(':')
        winning_numbers_str, own_numbers_str = numbers.strip().split(' | ')
        winning_numbers = [int(x.strip()) for x in winning_numbers_str.split(' ') if x != '']
        own_numbers = [int(x.strip()) for x in own_numbers_str.split(' ') if x != '']
        matches = 0
        for num in winning_numbers:
            if num in own_numbers:
                matches += 1
        if matches > 0:
            score += pow(2, matches - 1)

print(score)