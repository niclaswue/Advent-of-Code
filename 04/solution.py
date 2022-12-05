input = open("input.txt", "r").read().splitlines()


def get_ranges(line):
    first, second = (r.strip().split("-") for r in line.split(","))
    return *[int(x) for x in first], *[int(x) for x in second]


def contained(s1, e1, s2, e2):
    return s1 <= s2 and e1 >= e2 or s2 <= s1 and e2 >= e1


def overlap(s1, e1, s2, e2):
    return e1 >= s2 and s1 <= e2


solution_1 = sum(contained(*get_ranges(line)) for line in input)
solution_2 = sum(overlap(*get_ranges(line)) for line in input)

print(solution_1)
print(solution_2)
