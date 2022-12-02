with open("./input.txt", "r") as file:
    data = file.read()

total = 0

winning = [["A", "Y"], ["B", "Z"], ["C", "X"]]
losing = [["A", "Z"], ["B", "X"], ["C", "Y"]]
draw = [["A", "X"], ["B", "Y"], ["C", "Z"]]

values = [v.split(" ") for v in data.splitlines()]

for v in values:
    if v in winning:
        total += 6
    if v in draw:
        total += 3
    if v[1] == "X":
        total += 1
    if v[1] == "Y":
        total += 2
    if v[1] == "Z":
        total += 3

print(total)

total = 0


def add_for_showing(v):
    if v == "A" or v == "X":
        return 1
    if v == "B" or v == "Y":
        return 2
    else:
        return 3


for v in values:
    if v[1] == "X":
        for l in losing:
            if l[0] == v[0]:
                total += add_for_showing(l[1])
                break
    if v[1] == "Y":
        total += 3
        total += add_for_showing(v[0])
    if v[1] == "Z":
        total += 6
        for w in winning:
            if w[0] == v[0]:
                total += add_for_showing(w[1])
                break


print(total)
