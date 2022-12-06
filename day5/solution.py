with open("./input_stacks.txt", "r") as file:
    stacks_data = file.read()

with open("./input_commands.txt", "r") as file:
    commands_data = file.read()


def create_stacks(data):
    lines = data.splitlines()

    number_of_stacks = len(lines[-1].split(" "))

    stacks = [[] for _ in range(number_of_stacks)]

    for line in lines:
        for i in range(1, len(line), 4):
            if line[i] != " ":
                stacks[i // 4].append(line[i])

    return stacks


stacks = create_stacks(stacks_data)

stacks_deep_copy = [stack.copy() for stack in stacks]

commands = commands_data.splitlines()

for command in commands:
    command_split = command.split(" ")
    command = [int(command_split[1]), int(command_split[3]), int(command_split[5])]

    for i in range(command[0]):
        stacks[command[2] - 1].insert(0, stacks[command[1] - 1].pop(0))

    stacks_deep_copy[command[2] - 1] = [
        *stacks_deep_copy[command[1] - 1][0 : command[0]],
        *stacks_deep_copy[command[2] - 1],
    ]
    stacks_deep_copy[command[1] - 1] = stacks_deep_copy[command[1] - 1][command[0] :]


result = "".join([s[0] for s in stacks])
result_1 = "".join([s[0] for s in stacks_deep_copy])

print(result)
print(result_1)
