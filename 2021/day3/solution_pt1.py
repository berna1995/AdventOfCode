gamma_rate = 0
epsilon_rate = 0

with open("input", "r") as file:
    lines = file.readlines()

bits = len(lines[0]) - 1
values = [int(x, 2) for x in lines]

for bit in range(bits):
    mask = 1 << bit
    masked_vals = [(x & mask) >> bit for x in values]
    ones = sum(masked_vals)
    if(ones > len(values) / 2):
        gamma_rate |= mask
    else:
        epsilon_rate |= mask

print(gamma_rate * epsilon_rate)
