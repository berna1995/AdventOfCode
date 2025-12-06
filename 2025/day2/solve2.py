# this is indeed a bruteforce implementation but at least it prunes impossible repeating units
def has_repeating_unit(num: int) -> bool:
    s = str(num)

    for rep_size in range(1, (len(s)//2)+1):
        if len(s) % rep_size == 0: # must be a divisor
            if s[:rep_size] * (len(s) // rep_size) == s:
                return True

    return False


with open("input.txt", "r") as file:
    intervals = file.readline()

sum_wrong = 0

for interval in intervals.split(","):
    start_id, end_id = list(map(int, interval.split("-")))
    for x in range(start_id, end_id+1):
        if has_repeating_unit(x):
             sum_wrong += x

print(sum_wrong)