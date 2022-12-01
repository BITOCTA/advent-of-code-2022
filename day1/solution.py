with open("./input.txt") as f:
    data = f.read()

elves_carrying = data.split("\n\n")

for i, elf in enumerate(elves_carrying):
    elf_carrying = elf.split("\n")
    elf_carrying = [int(x) for x in elf_carrying]
    elves_carrying[i] = sum(elf_carrying)

index_of_max_elves_carrying = elves_carrying.index(max(elves_carrying))

top_3_elves_carrying = sorted(elves_carrying, reverse=True)[:3]
total_weight = sum(top_3_elves_carrying)

print(index_of_max_elves_carrying + 1)
print(max(elves_carrying))
print(top_3_elves_carrying)
print(total_weight)
