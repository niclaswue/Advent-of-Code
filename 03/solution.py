input = open("input.txt", "r").read().splitlines()


def priority(char):
    return ord(char) - (38 if char.isupper() else 96)


def common(line):
    first, second = line[: len(line) // 2], line[len(line) // 2 :]
    return set(first).intersection(set(second)).pop()


def badge(group):
    return set.intersection(*[set(l) for l in group]).pop()


badges = [badge(input[i : i + 3]) for i in range(0, len(input), 3)]

solution_1 = sum(priority(c) for c in [common(i) for i in input])
solution_2 = sum(priority(b) for b in badges)

print(solution_1)
print(solution_2)
