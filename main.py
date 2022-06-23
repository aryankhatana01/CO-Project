import math
import sys
from opcodes_dict import opcode, registers

def decimalToBinary(n):
    return bin(n).replace("0b", "")

reg = ["R0", "R1", "R2", "R3", "R4", "R5", "R6"]

# commands = []
with open("Input.txt", 'r') as f:
    commands = f.read().splitlines() 
# print(opcode)
# print(commands)
ans = []
# print(commands)
for command in commands:
    instruction = command.split(' ')
    if instruction[0]=="mov":
        if instruction[2] in reg:
            a = opcode["mov2"]
            r = registers[instruction[1]] + registers[instruction[2]]
            zeroes = 11-len(r)
            ans.append(a+zeroes+r)
        else:
            a = opcode["mov1"]
            r = registers[instruction[1]]
            num = instruction[2][1:]
            # print(num)
            im = decimalToBinary(int(num))
            im = str(im)
            zeroes = 8-len(im)
            zeroes = "0"*zeroes
            # print(type(im))
            # print(z)
            ans.append(a+r+zeroes+im)
print(ans)