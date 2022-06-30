import math
import sys
from opcodes_dict import opcode, registers
from randomAddress import randomaddress
from register_states import reg_states

def decimalToBinary(n):
    return bin(n).replace("0b", "")

reg = ["R0", "R1", "R2", "R3", "R4", "R5", "R6"]
error=0

# commands = []
with open("Input.txt", 'r') as f:
    commands = f.read().splitlines() 
# print(opcode)
# print(commands)
ans = []
# print(commands)

var_addresses = {}

# def add(reg_):
#     if (instruction[1] not in reg) or (instruction[2] not in reg) or (instruction[3] not in reg):
#         print("Error: register not valid")
#         error=1
#         return
#     else:
#         a = opcode["add"]
#         print(registers)
#         r = registers[reg_[0]] + registers[reg_[1]] + registers[reg_[2]]
#         zeroes = 11-len(r)
#         zeroes = "0"*zeroes
#         k = a+zeroes+r
#         ans.append(k)
#         s = reg_states[reg_[0]] + reg_states[reg_[1]]
#         reg_states[reg_[2]] = s
#         return k, s

total_var_ins = 0
for c in commands:
    instruction = c.split(' ')
    if instruction[0] == "var":
        total_var_ins+=1

what_to_add = 0

if commands[-1] != "hlt":
    print("hlt not being used as the last instruction")
else:
    for command in commands:
        instruction = command.split(' ')
        if instruction[0]=="mov":
            if instruction[2] in reg:
                if (instruction[1] not in reg) or (instruction[2] not in reg):
                    print("Error: register not valid")
                    error=1
                    break
                a = opcode["mov2"]
                r = registers[instruction[1]] + registers[instruction[2]]
                reg_states[registers[instruction[2]]] = reg_states[instruction[1]]
                zeroes = 11-len(r)
                zeroes = "0"*zeroes
                ans.append(a+zeroes+r)
            else:
                if (instruction[1] not in reg):
                    print("Error: register not valid")
                    error=1
                    break
                a = opcode["mov1"]
                r = registers[instruction[1]]
                num = instruction[2][1:]
                reg_states[instruction[1]] = num
                # print(num)
                im = decimalToBinary(int(num))
                im = str(im)
                zeroes = 8-len(im)
                if zeroes < 0:
                    print("Error: number is too large")
                    error=1
                    break
                else:
                    zeroes = "0"*zeroes
                    # print(type(im))
                    # print(z)
                    ans.append(a+r+zeroes+im)

        elif instruction[0]=="add":
            if (instruction[1] not in reg) or (instruction[2] not in reg) or (instruction[3] not in reg):
                print("Error: register not valid")
                error=1
                break
            a = opcode["add"]
            r = registers[instruction[1]] + registers[instruction[2]] + registers[instruction[3]]
            zeroes = 11-len(r)
            zeroes = "0"*zeroes
            ans.append(a+zeroes+r)
        
        elif instruction[0]=="mul":
            if (instruction[1] not in reg) or (instruction[2] not in reg) or (instruction[3] not in reg):
                print("Error: register not valid")
                error=1
                break
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
            if (instruction[1] not in reg) or (instruction[2] not in reg) or (instruction[3] not in reg):
                print("Error: register not valid")
                error=1
                break
            a = opcode["sub"]
            r = registers[instruction[1]] + registers[instruction[2]] + registers[instruction[3]]
            zeroes = 11-len(r)
            zeroes = "0"*zeroes
            ans.append(a+zeroes+r)
        
        elif instruction[0]=="div":
            if (instruction[1] not in reg) or (instruction[2] not in reg):
                print("Error: register not valid")
                error=1
                break
            a = opcode["div"]
            r = registers[instruction[1]] + registers[instruction[2]]
            zeroes = 11-len(r)
            zeroes = "0"*zeroes
            ans.append(a+zeroes+r)
        
        elif instruction[0]=="ls":
            if (instruction[1] not in reg):
                print("Error: register not valid")
                error=1
                break
            a = opcode["ls"]
            r = registers[instruction[1]]
            num = instruction[2][1:]
            # print(num)
            im = decimalToBinary(int(num))
            im = str(im)
            zeroes = 8-len(im)
            if zeroes < 0:
                print("Error: number is too large")
                error=1
                break
            else:
                zeroes = "0"*zeroes
                # print(type(im))
                # print(z)
                ans.append(a+r+zeroes+im)
        
        elif instruction[0]=="rs":
            if (instruction[1] not in reg):
                print("Error: register not valid")
                error=1
                break
            a = opcode["rs"]
            r = registers[instruction[1]]
            num = instruction[2][1:]
            # print(num)
            im = decimalToBinary(int(num))
            im = str(im)
            zeroes = 8-len(im)
            if zeroes < 0:
                print("Error: number is too large")
                error=1
                break
            else:
                zeroes = "0"*zeroes
                # print(type(im))
                # print(z)
                ans.append(a+r+zeroes+im)
        
        elif instruction[0]=="xor":
            if (instruction[1] not in reg) or (instruction[2] not in reg) or (instruction[3] not in reg):
                print("Error: register not valid")
                error=1
                break
            a = opcode["xor"]
            r = registers[instruction[1]] + registers[instruction[2]] + registers[instruction[3]]
            zeroes = 11-len(r)
            zeroes = "0"*zeroes
            ans.append(a+zeroes+r)
        
        elif instruction[0]=="st":
            if (instruction[1] not in reg):
                print("Error: register not valid")
                error=1
                break
            a = opcode["st"]
            r = registers[instruction[1]]
            # d = randomaddress()
            x = var_addresses[instruction[2]]
            ans.append(a+r+x)
        elif instruction[0]=="or":
            if (instruction[1] not in reg) or (instruction[2] not in reg) or (instruction[3] not in reg):
                print("Error: register not valid")
                error=1
                break
            a=opcode["or"]
            r=registers[instruction[1]] + registers[instruction[2]] + registers[instruction[3]]
            zeroes="0"*2
            ans.append(a+zeroes+r)
        elif instruction[0]=="and":
            if (instruction[1] not in reg) or (instruction[2] not in reg) or (instruction[3] not in reg):
                print("Error: register not valid")
                error=1
                break
            a=opcode["and"]
            r=registers[instruction[1]] + registers[instruction[2]] + registers[instruction[3]]
            zeroes="0"*2
            ans.append(a+zeroes+r)
        elif instruction[0]=="not":
            if (instruction[1] not in reg) or (instruction[2] not in reg):
                print("Error: register not valid")
                error=1
                break
            a=opcode["not"]
            r=registers[instruction[1]] + registers[instruction[2]]
            zeroes="0"*5
            ans.append(a+zeroes+r)
        elif instruction[0]=="cmp":
            if (instruction[1] not in reg) or (instruction[2] not in reg):
                print("Error: register not valid")
                error=1
                break
            a=opcode["cmp"]
            r=registers[instruction[1]] + registers[instruction[2]]
            zeroes="0"*5
            ans.append(a+zeroes+r) 
        elif instruction[0]=="var":
            instruction = instruction[1:]
            for var in instruction:
                binary_address = randomaddress(total_var_ins, len(commands), what_to_add)
                var_addresses[var] = binary_address
                what_to_add += 1
            
    if error!=1:
        print(ans)

