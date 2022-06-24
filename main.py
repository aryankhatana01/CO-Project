import math
import sys
from opcodes_dict import opcode, registers
from randomAddress import randomaddress

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
if commands[-1] != "hlt":
    print("hlt not being used as the last instruction")
else:
    for command in commands:
        instruction = command.split(' ')
        if instruction[0]=="mov":
            if instruction[2] in reg:
                a = opcode["mov2"]
                r = registers[instruction[1]] + registers[instruction[2]]
                zeroes = 11-len(r)
                zeroes = "0"*zeroes
                ans.append(a+zeroes+r)
            else:
                a = opcode["mov1"]
                r = registers[instruction[1]]
                num = instruction[2][1:]
                # print(num)
                im = decimalToBinary(int(num))
                im = str(im)
                zeroes = 8-len(im)
                if zeroes < 0:
                    print("Error: number is too large")
                    break
                else:
                    zeroes = "0"*zeroes
                    # print(type(im))
                    # print(z)
                    ans.append(a+r+zeroes+im)

        elif instruction[0]=="add":
            a = opcode["add"]
            r = registers[instruction[1]] + registers[instruction[2]] + registers[instruction[3]]
            zeroes = 11-len(r)
            zeroes = "0"*zeroes
            ans.append(a+zeroes+r)
        
        elif instruction[0]=="mul":
            a = opcode["mul"]
            r = registers[instruction[1]] + registers[instruction[2]] + registers[instruction[3]]
            zeroes = 11-len(r)
            zeroes = "0"*zeroes
            ans.append(a+zeroes+r)
        
        elif instruction[0]=="hlt":
            a = opcode["hlt"]
            zeroes = 11
            zeroes = "0"*zeroes
            ans.append(a+zeroes)
        
        elif instruction[0]=="sub":
            a = opcode["sub"]
            r = registers[instruction[1]] + registers[instruction[2]] + registers[instruction[3]]
            zeroes = 11-len(r)
            zeroes = "0"*zeroes
            ans.append(a+zeroes+r)
        
        elif instruction[0]=="div":
            a = opcode["div"]
            r = registers[instruction[1]] + registers[instruction[2]]
            zeroes = 11-len(r)
            zeroes = "0"*zeroes
            ans.append(a+zeroes+r)
        
        elif instruction[0]=="ls":
            a = opcode["ls"]
            r = registers[instruction[1]]
            num = instruction[2][1:]
            # print(num)
            im = decimalToBinary(int(num))
            im = str(im)
            zeroes = 8-len(im)
            if zeroes < 0:
                print("Error: number is too large")
                break
            else:
                zeroes = "0"*zeroes
                # print(type(im))
                # print(z)
                ans.append(a+r+zeroes+im)
        
        elif instruction[0]=="rs":
            a = opcode["rs"]
            r = registers[instruction[1]]
            num = instruction[2][1:]
            # print(num)
            im = decimalToBinary(int(num))
            im = str(im)
            zeroes = 8-len(im)
            if zeroes < 0:
                print("Error: number is too large")
                break
            else:
                zeroes = "0"*zeroes
                # print(type(im))
                # print(z)
                ans.append(a+r+zeroes+im)
        
        elif instruction[0]=="xor":
            a = opcode["xor"]
            r = registers[instruction[1]] + registers[instruction[2]] + registers[instruction[3]]
            zeroes = 11-len(r)
            zeroes = "0"*zeroes
            ans.append(a+zeroes+r)
        
        elif instruction[0]=="st":
            a = opcode["st"]
            r = registers[instruction[1]]
            d = randomaddress()
            x = d[instruction[2]]
            ans.append(a+r+x)
            
    print(ans)
#print ans
