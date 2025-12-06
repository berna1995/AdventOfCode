with open("input.txt", "r") as file:
    intervals = file.readline()

sum_wrong = 0

for interval in intervals.split(","):
    start_id, end_id = list(map(int, interval.split("-")))
    for x in range(start_id, end_id+1):
        # small optimization, can only happen if num length is even
        string_form = str(x)
        if len(string_form) % 2 == 0:
            if string_form[:len(string_form)//2] == string_form[len(string_form)//2:]:
                sum_wrong += x

print(sum_wrong)