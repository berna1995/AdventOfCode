import sys

valid_game_ids_sum = 0
color_limit = {"red": 12, "green": 13, "blue": 14}

with open(sys.argv[1], "r") as file:
    while True:
        line = file.readline()
        if not line:
            break
        header, body = line.split(":")
        game_id = int(header.split(" ")[1])
        plays = body.strip().split(";")

        all_valid = True
        for play in plays:
            for num_color in play.split(","):
                num, color = num_color.strip().split(" ")
                num = int(num)
                if num > color_limit[color]:
                    all_valid = False
                    break
            if not all_valid:
                break

        if all_valid:
            valid_game_ids_sum += game_id

print(valid_game_ids_sum)
