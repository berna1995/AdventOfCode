def common(s: str):
    bp1, bp2 = set(), set()
    for e in range(0, len(s) // 2):
        bp1.add(s[e])
    for e in range(len(s) // 2, len(s)):
        bp2.add(s[e])
    return list(bp1 & bp2)


with open("input", "r") as f:
    common_items = list(map(lambda x: common(x.rstrip()), f.readlines()))

    for li in common_items:
        assert len(li) == 1

    print(sum(map(lambda x: ord(
        x[0]) - ord('a') + 1 if x[0].islower() else ord(x[0]) - ord('A') + 27, common_items)))
