with open("input", "r") as file:
    inputs = [line.rstrip().split(" | ") for line in file.readlines()]

patterns = [input[0].split(" ") for input in inputs]
four_digit_output = [input[1].split(" ") for input in inputs]

count = 0

for output in four_digit_output:
    for word in output:
        word_len = len(word)
        if(word_len == 2 or word_len == 4 or word_len == 3 or word_len == 7):
            count += 1

print(count)
