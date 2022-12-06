input = open("input.txt", "r").read()


def find_marker(input, n):
    for i in range(n, len(input)):
        if len(set(input[i - n : i])) == n:
            return i


solution_1 = find_marker(input, n=4)
solution_2 = find_marker(input, n=14)

print(solution_1)
print(solution_2)
