from queue import SimpleQueue

class Tree:
    def __init__(self, name, parent) -> None:
        self.name = name
        self.parent = parent
        self.size = 0
        self.childs = dict()

    def append_child(self, name):
        if name not in self.childs:
            new_dir = Tree(name, self)
            self.childs[name] = new_dir
            return new_dir
        return None

    def get_child(self, name):
        return self.childs[name]

    def get_childs(self):
        return self.childs.values()

    def add_file(self, size):
        current = self
        while current is not None:
            current.size += size
            current = current.parent
    
    def get_path(self):
        current = self
        ll = []
        while current is not None:
            ll.append(current.name)
            current = current.parent
        ll.reverse()
        return '/'.join(ll)

with open('input', 'r') as file:
    lines = map(lambda x : x.rstrip(), file.readlines())

tree_root = Tree('/', None)
cwd = None

for l in lines:
    if l[0] == '$':
        if l[2:4] == 'cd':
            path = l[5:len(l)]
            if path == '..':
                cwd = cwd.parent
            elif path == '/':
                cwd = tree_root
            else:
                cwd = cwd.get_child(path)
        elif l[2:4] == 'ls':
            continue
    else:
        if l[0:3] == 'dir':
            cwd.append_child(l[4:len(l)])
        else:
            cwd.add_file(int(l.split(' ')[0]))

matching_folders = []
q = SimpleQueue()
q.put(tree_root)

TOTAL_SPACE = 70000000
REQUIRED_FREE_SPACE = 30000000
used_space = tree_root.size
free_space = TOTAL_SPACE - used_space
missing_space = REQUIRED_FREE_SPACE - free_space

assert missing_space > 0

while q.qsize() > 0:
    to_explore = q.get()
    if to_explore.size >= missing_space:
        matching_folders.append(to_explore)
    for child in to_explore.get_childs():
        q.put(child)

print(sorted(map(lambda x : x.size, matching_folders))[0])