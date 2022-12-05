state_input, cmd_input = open("input.txt", "r").read().split("\n\n")


def execute_cmd(state, amount, origin, dest, crate_mover_9001=False):
    if crate_mover_9001:
        state[dest - 1] += state[origin - 1][-amount:]
        del state[origin - 1][-amount:]
    else:
        for _ in range(amount):
            state[dest - 1].append(state[origin - 1].pop())
    return state


state = [line[1::4] for line in state_input.splitlines()[:-1]]
state = ["".join(col).replace(" ", "") for col in zip(*state)]
state = [list(x)[::-1] for x in state]

s1, s2 = [s.copy() for s in state], [s.copy() for s in state]

for cmd in [c.split(" ") for c in cmd_input.splitlines()]:
    s1 = execute_cmd(s1, *[int(c) for c in cmd[1::2]])
    s2 = execute_cmd(s2, *[int(c) for c in cmd[1::2]], crate_mover_9001=True)

solution_1 = "".join([s[-1] for s in s1])
solution_2 = "".join([s[-1] for s in s2])

print(solution_1)
print(solution_2)
