import sys
from collections import defaultdict

extra_cards = defaultdict(lambda: 0)
og_cards_n = 0

with open(sys.argv[1], 'r') as file:
    while True:
        line = file.readline()
        if not line:
            break
        card_hdr, numbers = line.strip().split(':')
        winning_numbers_str, own_numbers_str = numbers.strip().split(' | ')

        card_id = int(card_hdr.split(' ')[-1])
        og_cards_n += 1
        winning_numbers = [int(x.strip()) for x in winning_numbers_str.split(' ') if x != '']
        own_numbers = [int(x.strip()) for x in own_numbers_str.split(' ') if x != '']
        
        matches = 0
        for num in winning_numbers:
            if num in own_numbers:
                matches += 1
                extra_cards[card_id + matches] = extra_cards[card_id + matches] + 1 + extra_cards[card_id]

print(sum(extra_cards.values()) + og_cards_n)