def find_non_repeated(line: str, consecutive_chars: int):
    for i in range(0, len(line) - consecutive_chars):
        s = set(line[i : i + consecutive_chars])
        if len(s) == consecutive_chars:
            return i + consecutive_chars
    return None

with open('input', 'r') as file:
    l = file.readline()

print(find_non_repeated(l, 4))