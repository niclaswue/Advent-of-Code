input = open("input.txt", "r").read().splitlines()


def preprocess(line):
    first, second = line.split(" ")
    return ord(first) - ord("A"), ord(second) - ord("X")


def choices(opponent, result):
    # if result == 0:  # loose
    #     return opponent, (opponent - 1) % 3
    # elif result == 1:  # draw
    #     return opponent, opponent
    # else:  # win
    #     return opponent, (opponent + 1) % 3
    return opponent, (opponent + result - 1) % 3


def score(opponent, choice):
    if opponent == choice:
        return 1 + choice + 3
    elif abs(opponent - choice) == 1:
        return 1 + choice + (0 if opponent > choice else 6)
    else:
        return 1 + choice + (0 if opponent < choice else 6)


clean_input = [preprocess(line) for line in input]
solution_1 = sum(score(*line) for line in clean_input)
solution_2 = sum(score(*choices(*line)) for line in clean_input)

print(solution_1)
print(solution_2)
