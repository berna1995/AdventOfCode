class GameSign:
    ROCK_VAL = 1
    PAPER_VAL = 2
    SCISSORS_VAL = 3

    def __init__(self, s: str):
        if s == "X" or s == "A":
            self.sign = GameSign.ROCK_VAL
        elif s == "Y" or s == "B":
            self.sign = GameSign.PAPER_VAL
        elif s == "Z" or s == "C":
            self.sign = GameSign.SCISSORS_VAL
        else:
            self.sign = None

    def match_against(self, y) -> int:
        if self.sign == y.sign:
            return 0
        if y.sign == self.lose_against().sign:
            return -1
        else:
            return 1

    def value(self):
        return self.sign

    def lose_against(self):
        if self.sign == GameSign.ROCK_VAL:
            return GameSign("B")
        elif self.sign == GameSign.PAPER_VAL:
            return GameSign("C")
        elif self.sign == GameSign.SCISSORS_VAL:
            return GameSign("A")

    def win_against(self):
        return self.lose_against().lose_against()


def get_result(s: str) -> int:
    match = s.split(" ")
    s0 = GameSign(match[0])
    if match[1] == "Y":
        s1 = GameSign(match[0])
    elif match[1] == "X":
        s1 = s0.win_against()
    else:
        s1 = s0.lose_against()

    if s1.match_against(s0) == 0:
        return s1.value() + 3
    elif s1.match_against(s0) == 1:
        return s1.value() + 6
    else:
        return s1.value()


with open("input", "r") as f:
    total_score = sum(map(lambda x: get_result(x.rstrip()), f.readlines()))
    print(total_score)
