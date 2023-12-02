import sys

power_sum = 0

with open(sys.argv[1], "r") as file:
    while True:
        line = file.readline()
        if not line:
            break
        header, body = line.split(":")
        game_id = int(header.split(" ")[1])
        plays = body.strip().split(";")

        min_color = {"red": 0, "green": 0, "blue": 0}

        for play in plays:
            for num_color in play.split(","):
                num, color = num_color.strip().split(" ")
                num = int(num)
                min_color[color] = max(min_color[color], num)

        power_sum += min_color["red"] * min_color["blue"] * min_color["green"]


print(power_sum)
