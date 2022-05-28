from collections import defaultdict

graph = defaultdict(lambda: [])


def dfs(node: str, end: str, ban_list: list, path: list):

    path.append(node)

    if node.islower():
        ban_list.append(node)

    if node == end:
        return [path]

    visitable = [x for x in graph[node] if x not in ban_list]

    valid_paths = []

    for other_node in visitable:
        res = dfs(other_node, end, ban_list.copy(), path.copy())
        for res_path in res:
            if res_path[-1] == end:
                valid_paths.append(res_path)

    if valid_paths == []:
        return [path]

    return valid_paths


with open("input", "r") as file:
    while True:
        line = file.readline().rstrip()
        if not line:
            break

        tokens = line.split("-")
        graph[tokens[0]].append(tokens[1])
        graph[tokens[1]].append(tokens[0])

result = dfs("start", "end", [], [])

print(len(result))
