with open("input", "r") as file:
    lines = file.readlines()

values = [int(x, 2) for x in lines]


def rating_function(valList, criteriaFunction):
    bits = len(lines[0]) - 1
    left = valList

    for bit in reversed(range(bits)):
        discriminant = criteriaFunction(bit, left)
        left = list(
            filter(lambda x: (((1 << bit) & x) >> bit) == discriminant, left))
        if(len(left) == 1):
            return left[0]


def most_common_bit(bitPosition: int, valList):
    mask = 1 << bitPosition
    masked_vals = [(x & mask) >> bitPosition for x in valList]
    ones = sum(masked_vals)
    return 1 if (ones >= len(valList) / 2) else 0


def least_common_bit(bitPosition: int, valList):
    return 0 if most_common_bit(bitPosition, valList) else 1


ogr = rating_function(values, most_common_bit)
co2 = rating_function(values, least_common_bit)
print(ogr * co2)
