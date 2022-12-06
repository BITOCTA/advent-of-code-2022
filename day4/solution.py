with open("./input.txt", "r") as file:
    data = file.read()

rows = data.splitlines()


def range_contains_range(range1, range2):
    return (
        range1[0] <= range2[0]
        and range1[1] >= range2[1]
        or range1[0] >= range2[0]
        and range1[1] <= range2[1]
    )


def ranges_overlap(range1, range2):
    return (
        range1[0] <= range2[0] <= range1[1]
        or range1[0] <= range2[1] <= range1[1]
        or range2[0] <= range1[0] <= range2[1]
        or range2[0] <= range1[1] <= range2[1]
    )


total_pairs = 0
total_pairs_overlapping = 0

for row in rows:
    assignments = row.split(",")
    ranges = [assignment.split("-") for assignment in assignments]
    ranges = [[int(range[0]), int(range[1])] for range in ranges]
    if range_contains_range(ranges[0], ranges[1]):
        total_pairs += 1
    if ranges_overlap(ranges[0], ranges[1]):
        total_pairs_overlapping += 1

print(total_pairs)
print(total_pairs_overlapping)
