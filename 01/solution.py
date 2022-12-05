input = open("input.txt", "r").read().split("\n\n")
inventory_per_elf = [sum(int(l) for l in elf.splitlines()) for elf in input]

solution_part_1 = max(inventory_per_elf)
solution_part_2 = sum(sorted(inventory_per_elf, reverse=True)[:3])

print(solution_part_1)
print(solution_part_2)
