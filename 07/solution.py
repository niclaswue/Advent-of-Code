from __future__ import annotations

from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class Directory:
    name: str
    parent: Directory
    files: List[Tuple[int, str]]
    children: List[Directory]

    def get_size(self):
        return sum(f[0] for f in self.files) + sum(d.get_size() for d in self.children)


input = open("input.txt", "r").read().split("$")[2:]
root = Directory("/", None, [], [])

cwd = root
for line in input:
    cmd, *out = line.strip().splitlines()
    if cmd.startswith("ls"):
        for info, name in [o.split(" ") for o in out]:
            if info == "dir":
                cwd.children.append(Directory(name, cwd, [], []))
            else:
                cwd.files.append((int(info), name))
    elif cmd.startswith("cd"):
        dir = cmd.split(" ")[-1].strip()
        if dir == "..":
            cwd = cwd.parent
        else:
            cwd = [c for c in cwd.children if c.name == dir].pop()

queue = [root]
sum_of_dirs = 0
smallest_deletable_dir_size = root.get_size()
while len(queue) > 0:
    d = queue.pop()
    size = d.get_size()
    if size <= 100000:
        sum_of_dirs += d.get_size()
    if size >= 8381165:
        smallest_deletable_dir_size = min(smallest_deletable_dir_size, size)
    queue += d.children

solution_1 = sum_of_dirs
solution_2 = smallest_deletable_dir_size

print(solution_1)
print(solution_2)
