from collections import defaultdict

graph = defaultdict(lambda: [])


def dfs(node: str, end: str, ban_list: list, path: list, revisitable: str):
    path.append(node)

    if node.islower():
        if node == revisitable:
            revisitable = None
        else:
            ban_list.append(node)

    if node == end:
        return [path]

    visitable = [x for x in graph[node] if x not in ban_list]

    valid_paths = []

    for other_node in visitable:
        res = dfs(other_node, end, ban_list.copy(), path.copy(), revisitable)
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

small_caves = [x for x in graph.keys() if x != "start" and x !=
               "end" and x.islower()]
result = set()

for small_cave in small_caves:
    for path in dfs("start", "end", [], [], small_cave):
        path_string = ",".join(path)
        result.add(path_string)

print(len(result))
