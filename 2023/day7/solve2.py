import sys
from collections import defaultdict

def hand_to_nums(hand: str) -> list[int]:
    card_to_num_dict = {
        'A': 14,
        'K': 13,
        'Q': 12,
        'J': 1,
        'T': 10
    }
    return [int(card) if card.isdigit() else card_to_num_dict[card] for card in hand]

def get_hand_type_val(hand_vals: list[int]) -> int:
    occ_counter_map = defaultdict(lambda: 0)
    for val in hand_vals:
        occ_counter_map[val] = occ_counter_map[val] + 1
    if 1 in occ_counter_map.keys():
        jokers = occ_counter_map[1]
        del occ_counter_map[1]
        if jokers == len(hand_vals):
            return 6
        higher_occ_card = max(occ_counter_map, key=lambda k: occ_counter_map[k])
        occ_counter_map[higher_occ_card] += jokers

    counters = occ_counter_map.values()
    n_eq = len(counters)

    if n_eq == 1:
        return 6
    elif n_eq == 2 and 4 in counters:
        return 5
    elif n_eq == 2 and 3 in counters:
        return 4
    elif n_eq == 3 and 3 in counters:
        return 3
    elif n_eq == 3 and 2 in counters:
        return 2
    elif n_eq == 4:
        return 1
    else:
        return 0


with open(sys.argv[1], 'r') as file:
    parsed_input = [(hand_to_nums(hand),int(score)) for hand,score in map(lambda x: x.strip().split(' '), file.readlines())]

    type_hand_bet = []
    for card_list, bet in parsed_input:
        type_hand_bet.append((get_hand_type_val(card_list), card_list, bet))
    type_hand_bet.sort()

    score = 0
    for i in range(len(type_hand_bet)):
        _,_,bet = type_hand_bet[i]
        score += (i + 1) * bet

    print(score)