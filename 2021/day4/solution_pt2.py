from itertools import chain

boards = []

with open("input", "r") as file:
    extracted_numbers = list(map(int, file.readline().split(",")))

    while True:
        line = file.readline()

        if not line:
            break
        if line == "":
            continue

        board = []

        for i in range(5):
            row = [(cell, False)
                   for cell in map(int, filter(lambda x: x != "", file.readline().split(" ")))]
            board.append(row)

        boards.append(board)

wins = []

for number in extracted_numbers:
    for board in boards[:]:
        for row in board:
            try:
                i = row.index((number, False))
                row[i] = (row[i][0], True)
                row_win = all(map(lambda cell: cell[1] == True, row))
                if row_win:
                    res = sum(map(lambda c: c[0], filter(
                        lambda x: x[1] == False, chain(*boards[0])))) * number
                    boards.remove(board)
                    wins.append(res)

                else:
                    col = [board[x][i] for x in range(5)]
                    col_win = all(map(lambda cell: cell[1] == True, col))
                    if col_win:
                        res = sum(map(lambda c: c[0], filter(
                            lambda x: x[1] == False, chain(*boards[0])))) * number
                        boards.remove(board)
                        wins.append(res)
                break
            except ValueError:
                continue

print(wins.pop())
