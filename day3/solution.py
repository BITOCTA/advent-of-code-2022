with open("./input.txt", "r") as file:
    data = file.read()

rows = data.splitlines()


def get_index_of_letter(letter: str):
    if letter.isupper():
        return ord(letter) - 38
    else:
        return ord(letter) - 96


total = 0


def find_common_letter(row1, row2):
    for letter in row1:
        if letter in row2:
            return letter


for row in rows:
    total += get_index_of_letter(
        find_common_letter(row[: len(row) // 2], row[len(row) // 2 :])
    )

print(total)

total = 0

groups_of_three_rows = [rows[i : i + 3] for i in range(0, len(rows), 3)]


def find_common_letter(rows):
    for letter in rows[0]:
        if letter in rows[1] and letter in rows[2]:
            return letter


for row_group in groups_of_three_rows:
    total += get_index_of_letter(find_common_letter(row_group))

print(total)
