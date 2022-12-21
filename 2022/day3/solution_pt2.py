def common(s: list):
    bp1 = set(s[0].rstrip())
    bp2 = set(s[1].rstrip())
    bp3 = set(s[2].rstrip())
    return list(bp1 & bp2 & bp3)[0]


with open("input", "r") as f:
    lines = f.readlines()
    common_items = map(common, zip(*(iter(lines),) * 3))

    print(sum(map(lambda x: ord(
        x) - ord('a') + 1 if x.islower() else ord(x) - ord('A') + 27, common_items)))
