from collections import defaultdict

with open("./input.txt", "r") as file:
    data = file.read()

lines = data.splitlines()

structure_dict = defaultdict(int)

current_dir = ""


def add_size_to_dirs(dir_path, size):
    if dir_path == "":
        structure_dict[dir_path] += size
        return
    else:
        structure_dict[dir_path] += size
        add_size_to_dirs(
            "/".join(dir_path.split("/")[0 : (len(dir_path.split("/")) - 1)]), size
        )


for line in lines:
    line_s = line.split(" ")
    if line_s[0] == "$" and line_s[1] == "cd":
        if line_s[2] == "..":
            current_dir = "/".join(
                current_dir.split("/")[0 : (len(current_dir.split("/")) - 1)]
            )
        elif line_s[2] != "/":
            current_dir = current_dir + "/" + line_s[2]
    elif line[0] != "$":
        if line_s[0] != "dir":
            add_size_to_dirs(current_dir, int(line_s[0]))


total_sum = 0
space_after_deletion = float("inf")
used_space = structure_dict[""]
total_space = 70000000
needed_space = 30000000
directory_to_delete = ""


for key, value in structure_dict.items():
    if value <= 100000:
        total_sum += value
    if (
        total_space - (used_space - value) >= needed_space
        and total_space - (used_space - value) < space_after_deletion
    ):
        space_after_deletion = total_space - (used_space - value)
        directory_to_delete = value

print(total_sum)
print(directory_to_delete)
