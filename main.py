import math
import sys

commands = []
with open("Input.txt", 'r') as f:
    commands_ = f.readlines()
    for command in commands_:
        commands.append(command[:-1])
print(commands)