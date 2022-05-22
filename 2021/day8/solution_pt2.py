from collections import defaultdict

#  0:      1:      2:      3:      4:
#  aaaa    ....    aaaa    aaaa    ....
# b    c  .    c  .    c  .    c  b    c
# b    c  .    c  .    c  .    c  b    c
#  ....    ....    dddd    dddd    dddd
# e    f  .    f  e    .  .    f  .    f
# e    f  .    f  e    .  .    f  .    f
#  gggg    ....    gggg    gggg    ....

#   5:      6:      7:      8:      9:
#  aaaa    aaaa    aaaa    aaaa    aaaa
# b    .  b    .  .    c  b    c  b    c
# b    .  b    .  .    c  b    c  b    c
#  dddd    dddd    ....    dddd    dddd
# .    f  e    f  .    f  e    f  .    f
# .    f  e    f  .    f  e    f  .    f
#  gggg    gggg    ....    gggg    gggg

# segments are a,b,c,d,e,f,g in a 7-segment display

# 0,6,9 have 6 segments
# 1 has 2 segments
# 2,3,5 have 5 segments
# 4 has 4 segments
# 7 has 3 segments
# 8 has 7 segments

segments_configuration = {
    frozenset("abcefg"): 0,
    frozenset("cf"): 1,
    frozenset("acdeg"): 2,
    frozenset("acdfg"): 3,
    frozenset("bcdf"): 4,
    frozenset("abdfg"): 5,
    frozenset("abdfeg"): 6,
    frozenset("acf"): 7,
    frozenset("abcdefg"): 8,
    frozenset("abcdfg"): 9
}


def get_segments_mapping(patterns):
    # map to associate fake segment location to real ones
    segments_map = defaultdict()

    # forced numbers, by length
    one_set = set(next(x for x in patterns if len(x) == 2))
    four_set = set(next(x for x in patterns if len(x) == 4))
    seven_set = set(next(x for x in patterns if len(x) == 3))
    eight_set = set(next(x for x in patterns if len(x) == 7))
    # can deduce A segment mapping by difference between 7 and 1 letters set
    a_segment = next(iter(seven_set.difference(one_set)))
    segments_map[a_segment] = 'a'
    # can deduce C segment mapping by difference between 6 and 1,
    # 6 is not know but is the only one of length 6 that will produce a non-empty set
    c_segment = next(iter((next(one_set.difference(set(x)) for x in patterns if len(
        x) == 6 and len(one_set.difference(set(x))) == 1))))
    segments_map[c_segment] = 'c'
    # now the F segment is also known, cause 1 have only C and F...
    f_segment = next(iter(one_set.difference(set(c_segment))))
    segments_map[f_segment] = 'f'
    # i can now get mapping for segment B and D by subtracting from 4 segment set
    # the 1 segment set so that it leaves only B and D segments,
    # at this point if i subtract from the remaining B and D the segments of 0 (which contains B
    # but not D) i remain with the d mapping
    # even if zero is now know is the only one of size 6 that will give me a set of size 1 during this operation
    bd = four_set.difference(one_set)
    d_segment = next(iter(next(bd.difference(set(x)) for x in patterns if len(
        x) == 6 and len(bd.difference(set(x))) == 1)))
    b_segment = next(iter(bd.difference(set(d_segment))))
    segments_map[d_segment] = 'd'
    segments_map[b_segment] = 'b'
    # by removing segments A,C,D and F from 3 i will remain with G
    # this operation will give a set with 1 result only in the case of 3 (not 2, not 5)
    acdf = set([a_segment, c_segment, d_segment, f_segment])
    g_segment = next(iter(next(set(x).difference(acdf) for x in patterns if len(
        x) == 5 and len(set(x).difference(acdf)) == 1)))
    segments_map[g_segment] = 'g'
    # to obtain the remaining E segment mapping, ill just subtract all the others from the 8
    # set which has all of the segments
    e_segment = next(iter(eight_set.difference(set(segments_map.keys()))))
    segments_map[e_segment] = 'e'

    return segments_map


with open("input", "r") as file:
    inputs = [line.rstrip().split(" | ") for line in file.readlines()]

patterns = [input[0].split(" ") for input in inputs]
four_digit_output = [input[1].split(" ") for input in inputs]
sum = 0

for pattern, digits in tuple(zip(patterns, four_digit_output)):
    displayed_number = 0
    segments_map = get_segments_mapping(pattern)

    current_position = 3
    for digit in digits:
        letters_set = set()
        for letter in digit:
            letters_set.add(segments_map[letter])
        frozen_letters_set = frozenset(letters_set)
        num_digit = segments_configuration[frozen_letters_set]
        displayed_number += num_digit * pow(10, current_position)
        current_position -= 1

    sum += displayed_number

print(sum)
