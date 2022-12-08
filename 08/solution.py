input = open("input.txt").read().splitlines()

trees = [[int(t) for t in list(l)] for l in input]
w, h = len(trees[0]), len(trees)


def tree_info(trees, current):
    # Return a tuple (viewing distance, visible from edge)
    for i, t in enumerate(trees):
        if t >= current:
            return (i + 1, False)
    return (len(trees), True)


visible = 2 * w + 2 * (h - 2)
highest_score = 0
for x in range(1, w - 1):
    for y in range(1, h - 1):
        current = trees[y][x]

        left, vis_left = tree_info(trees[y][:x][::-1], current)
        right, vis_right = tree_info(trees[y][x + 1 :], current)
        top, vis_top = tree_info([t[x] for t in trees[:y][::-1]], current)
        bottom, vis_bot = tree_info([t[x] for t in trees[y + 1 :]], current)

        highest_score = max(left * right * top * bottom, highest_score)
        if vis_left or vis_right or vis_top or vis_bot:
            visible += 1

solution_1 = visible
solution_2 = highest_score

print(solution_1)
print(solution_2)
