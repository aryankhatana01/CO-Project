import math
import sys
from opcodes_dict import opcode, registers

def decimalToBinary(n):
    return bin(n).replace("0b", "")

reg = ["R0", "R1", "R2", "R3", "R4", "R5", "R6"]

commands = []
with open("Input.txt", 'r') as f:
    commands_ = f.readlines()
    for command in commands_:
        commands.append(command[:-1])
# print(opcode)
# print(commands)
ans = []
for command in commands:
    instruction = command.split(' ')
    # if instruction[0]=="mov":
    #     if instruction[2] in reg:
