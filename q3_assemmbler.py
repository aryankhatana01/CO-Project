import math
import sys
from opcodes_dict import opcode, registers
from randomAddress import randomaddress
from register_states import reg_states

def decimalToBinary(n):
    return bin(n).replace("0b", "")

def float_bin(number, places = 3):
 
    # split() separates whole number and decimal
    # part and stores it in two separate variables
    whole, dec = str(number).split(".")
 
    # Convert both whole number and decimal 
    # part from string type to integer type
    whole = int(whole)
    dec = int (dec)
 
    # Convert the whole number part to it's
    # respective binary form and remove the
    # "0b" from it.
    res = bin(whole).lstrip("0b") + "."
 
    # Iterate the number of times, we want
    # the number of decimal places to be
    for x in range(places):
 
        # Multiply the decimal value by 2
        # and separate the whole number part
        # and decimal part
        whole, dec = str((decimal_converter(dec)) * 2).split(".")
 
        # Convert the decimal part
        # to integer again
        dec = int(dec)
 
        # Keep adding the integer parts
        # receive to the result variable
        res += whole
 
    return res
 
# Function converts the value passed as
# parameter to it's decimal representation
def decimal_converter(num):
    while num > 1:
        num /= 10
    return num

# print(op_list_valid)
def if_label(instruction):
    if instruction[-1] == ":":
        return True
    return False    

reg = ["R0", "R1", "R2", "R3", "R4", "R5", "R6","FLAGS"]
error=0

commands = []
for line in sys.stdin:
    commands.append(line.strip())
# print(commands)
# print(opcode)
# print(commands)
ans = []
count=0
# print(commands)
addresses = {}
labels = []
vars=[]
# for c in commands:
#     instruction=c.split()
#     if instruction[0]=="var" and len(instruction)>1:
#         addresses[instruction[1]]=0
#     elif if_label(instruction[0])==True:
#         string=instruction[0]
#         labels.append(string[0:len(string)-1])
#         addresses[string[0:len(string)-1]]=0
#         count+=1
#     else:
#         count+=1
# for ele in addresses:
#     addresses[ele]=count
#     count+=1                


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

op_list_valid = [key for key in opcode.keys()]
# # print(op_list_valid)
# def if_label(instruction):
#     if instruction[-1] == ":":
#         return True
#     return False

# total_var_ins = 0
# for c in commands:
#     instruction = c.split(' ')
#     if instruction[0] == "var":
#         total_var_ins+=1

commands_ = commands.copy()
commands = []
for ele in commands_:
    l = ele.split(' ')
    l = list(filter(('').__ne__, l))
    commands.append(" ".join(l))
# print(commands)
for c in commands:
    instruction=c.split()
    if len(instruction)==0:
        continue
    if instruction[0]=="var" and len(instruction)>1:
        vars.append(instruction[1])
        addresses[instruction[1]]=0
    elif if_label(instruction[0])==True:
        string=instruction[0]
        labels.append(string[0:len(string)-1])
        addresses[string[0:len(string)-1]]=0
        count+=1
    else:
        count+=1
for ele in addresses:
    addresses[ele]=count
    count+=1


# for command in commands:
#     instruction = command.split(' ')
#     if if_label(instruction[0])==True:
#         labels.append(instruction[0:-1])

error = 0

def get_label_address(i, instruction):
    try:
        if instruction[0]=="mov":
                if instruction[2] in reg:
                    if (instruction[1] not in reg) or (instruction[2] not in reg):
                        print(f"Error@Line{i+1}: register not valid")
                        error=1
                    a = opcode["mov2"]
                    r = registers[instruction[1]] + registers[instruction[2]]
                    reg_states[registers[instruction[2]]] = reg_states[instruction[1]]
                    zeroes = 11-len(r)
                    zeroes = "0"*zeroes
                    ans.append(a+zeroes+r)
                else:
                    if (instruction[1] not in reg):
                        print(f"Error@Line{i+1}: register not valid")
                        error=1
                    a = opcode["mov1"]
                    r = registers[instruction[1]]
                    num = instruction[2][1:]
                    reg_states[instruction[1]] = num
                    # print(num)
                    im = decimalToBinary(int(num))
                    im = str(im)
                    zeroes = 8-len(im)
                    if zeroes < 0:
                        print(f"Error@Line{i+1}: number is too large")
                        error=1
                    else:
                        zeroes = "0"*zeroes
                        # print(type(im))
                        # print(z)
                        ans.append(a+r+zeroes+im)

        elif instruction[0]=="add":
            if (instruction[1] not in reg) or (instruction[2] not in reg) or (instruction[3] not in reg):
                print(f"Error@Line{i+1}: register not valid")
                error=1    
            a = opcode["add"]
            r = registers[instruction[1]] + registers[instruction[2]] + registers[instruction[3]]
            zeroes = 11-len(r)
            zeroes = "0"*zeroes
            ans.append(a+zeroes+r)
        
        elif instruction[0]=="mul":
            if (instruction[1] not in reg) or (instruction[2] not in reg) or (instruction[3] not in reg):
                print(f"Error@Line{i+1}: register not valid")
                error=1
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
                print(f"Error@Line{i+1}: register not valid")
                error=1
            a = opcode["sub"]
            r = registers[instruction[1]] + registers[instruction[2]] + registers[instruction[3]]
            zeroes = 11-len(r)
            zeroes = "0"*zeroes
            ans.append(a+zeroes+r)
        
        elif instruction[0]=="div":
            if (instruction[1] not in reg) or (instruction[2] not in reg):
                print(f"Error@Line{i+1}: register not valid")
                error=1
            a = opcode["div"]
            r = registers[instruction[1]] + registers[instruction[2]]
            zeroes = 11-len(r)
            zeroes = "0"*zeroes
            ans.append(a+zeroes+r)
        
        elif instruction[0]=="ls":
            if (instruction[1] not in reg):
                print(f"Error@Line{i+1}: register not valid")
                error=1
            a = opcode["ls"]
            r = registers[instruction[1]]
            num = instruction[2][1:]
            # print(num)
            im = decimalToBinary(int(num))
            im = str(im)
            zeroes = 8-len(im)
            if zeroes < 0:
                print(f"Error@Line{i+1}: number is too large")
                error=1
            else:
                zeroes = "0"*zeroes
                # print(type(im))
                # print(z)
                ans.append(a+r+zeroes+im)
        
        elif instruction[0]=="rs":
            if (instruction[1] not in reg):
                print(f"Error@Line{i+1}: register not valid")
                error=1
            a = opcode["rs"]
            r = registers[instruction[1]]
            num = instruction[2][1:]
            # print(num)
            im = decimalToBinary(int(num))
            im = str(im)
            zeroes = 8-len(im)
            if zeroes < 0:
                print(f"Error@Line{i+1}: number is too large")
                error=1
            else:
                zeroes = "0"*zeroes
                # print(type(im))
                # print(z)
                ans.append(a+r+zeroes+im)
        
        elif instruction[0]=="xor":
            if (instruction[1] not in reg) or (instruction[2] not in reg) or (instruction[3] not in reg):
                print(f"Error@Line{i+1}: register not valid")
                error=1
            a = opcode["xor"]
            r = registers[instruction[1]] + registers[instruction[2]] + registers[instruction[3]]
            zeroes = 11-len(r)
            zeroes = "0"*zeroes
            ans.append(a+zeroes+r)
        
        elif instruction[0]=="st":
            if (instruction[1] not in reg):
                print(f"Error@Line{i+1}: register not valid")
                error=1
            if(instruction[2] not in addresses.keys()):
                print(f"Error@Line{i+1}: variable not defined")
                error=1
            a = opcode["st"]
            r = registers[instruction[1]]
            # d = randomaddress()
            # x = var_addresses[instruction[2]]
            x=decimalToBinary(addresses[instruction[2]])
            zeroes=8-len(x)
            zeroes="0"*zeroes
            ans.append(a+r+zeroes+x)
            
        elif instruction[0]=="or":
            if (instruction[1] not in reg) or (instruction[2] not in reg) or (instruction[3] not in reg):
                print(f"Error@Line{i+1}: register not valid")
                error=1
            a=opcode["or"]
            r=registers[instruction[1]] + registers[instruction[2]] + registers[instruction[3]]
            zeroes="0"*2
            ans.append(a+zeroes+r)

        elif instruction[0]=="and":
            if (instruction[1] not in reg) or (instruction[2] not in reg) or (instruction[3] not in reg):
                print(f"Error@Line{i+1}: register not valid")
                error=1
            a=opcode["and"]
            r=registers[instruction[1]] + registers[instruction[2]] + registers[instruction[3]]
            zeroes="0"*2
            ans.append(a+zeroes+r)

        elif instruction[0]=="not":
            if (instruction[1] not in reg) or (instruction[2] not in reg):
                print(f"Error@Line{i+1}: register not valid")
                error=1
            a=opcode["not"]
            r=registers[instruction[1]] + registers[instruction[2]]
            zeroes="0"*5
            ans.append(a+zeroes+r)

        elif instruction[0]=="cmp":
            if (instruction[1] not in reg) or (instruction[2] not in reg):
                print(f"Error@Line{i+1}: register not valid")
                error=1
            a=opcode["cmp"]
            r=registers[instruction[1]] + registers[instruction[2]]
            zeroes="0"*5
            ans.append(a+zeroes+r)
            
        elif instruction[0]=="jmp":
            a=opcode["jmp"]
            if (instruction[1] in labels):
                x=decimalToBinary(addresses[instruction[1]])
                zeroes=16 - (len(x)+5)
                zeroes="0"*zeroes
                ans.append(a+zeroes+x)
            else:
                error = 1
                print(f"Error@Line{i+1}: label not defined")

        elif instruction[0]=="jlt":
            a=opcode["jlt"]
            if (instruction[1] in labels):
                x=decimalToBinary(addresses[instruction[1]])
                zeroes=16 - (len(x)+5)
                zeroes="0"*zeroes
                ans.append(a+zeroes+x)
            else:
                error = 1
                print(f"Error@Line{i+1}: label not defined")

        elif instruction [0]=="jgt":
            a=opcode["jgt"]
            if (instruction[1] in labels):
                x=decimalToBinary(addresses[instruction[1]])
                zeroes=16 - (len(x)+5)
                zeroes="0"*zeroes
                ans.append(a+zeroes+x)
            else:
                error = 1
                print(f"Error@Line{i+1}: label not defined")

        elif instruction[0]=="je":
            a=opcode["je"]
            if (instruction[1] in labels):
                x=decimalToBinary(addresses[instruction[1]])
                zeroes=16 - (len(x)+5)
                zeroes="0"*zeroes
                ans.append(a+zeroes+x)
            else:
                error = 1
                print(f"Error@Line{i+1}: label not defined")
    except:
        pass


commands = list(filter(('').__ne__, commands))

if commands[-1] != "hlt":
    print("hlt not being used as the last instruction")
else:
    for i, command in enumerate(commands):
        instruction = command.split(' ')
        if len(command)==0:
            continue
        # if len(instruction)==1 and if_label(instruction[0])==False:
        #     print(f"Error@Line{i+1}: instruction not valid")
        #     error=1
        #     break
        if (if_label(instruction[0])==False):
            if (instruction[0] not in op_list_valid):
                print(instruction[0])
                error=1
                print(f"Error@Line{i+1}: instruction not valid")
                break
        if instruction[0]=="mov":
            if instruction[2] in reg:
                if (instruction[1] not in reg) or (instruction[2] not in reg):
                    print(f"Error@Line{i+1}: register not valid")
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
                    print(f"Error@Line{i+1}: register not valid")
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
                    print(f"Error@Line{i+1}: number is too large")
                    error=1
                    break
                else:
                    zeroes = "0"*zeroes
                    # print(type(im))
                    # print(z)
                    ans.append(a+r+zeroes+im)

        elif instruction[0]=="add":
            if (instruction[1] not in reg) or (instruction[2] not in reg) or (instruction[3] not in reg):
                print(f"Error@Line{i+1}: register not valid")
                error=1
                break
            if ("FLAGS" in instruction):
                print(f"Error@Line{i+1}: illegal use of flag")
                error=1
                break
            a = opcode["add"]
            r = registers[instruction[1]] + registers[instruction[2]] + registers[instruction[3]]
            zeroes = 11-len(r)
            zeroes = "0"*zeroes
            ans.append(a+zeroes+r)
        
        elif instruction[0]=="mul":
            if (instruction[1] not in reg) or (instruction[2] not in reg) or (instruction[3] not in reg):
                print(f"Error@Line{i+1}: register not valid")
                error=1
                break
            if ("FLAGS" in instruction):
                print(f"Error@Line{i+1}: illegal use of flag")
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
                print(f"Error@Line{i+1}: register not valid")
                error=1
                break
            if ("FLAGS" in instruction):
                print(f"Error@Line{i+1}: illegal use of flag")
                error=1
                break
            a = opcode["sub"]
            r = registers[instruction[1]] + registers[instruction[2]] + registers[instruction[3]]
            zeroes = 11-len(r)
            zeroes = "0"*zeroes
            ans.append(a+zeroes+r)
        
        elif instruction[0]=="div":
            if (instruction[1] not in reg) or (instruction[2] not in reg):
                print(f"Error@Line{i+1}: register not valid")
                error=1
                break
            if ("FLAGS" in instruction):
                print(f"Error@Line{i+1}: illegal use of flag")
                error=1
                break
            a = opcode["div"]
            r = registers[instruction[1]] + registers[instruction[2]]
            zeroes = 11-len(r)
            zeroes = "0"*zeroes
            ans.append(a+zeroes+r)
        
        elif instruction[0]=="ls":
            if (instruction[1] not in reg):
                print(f"Error@Line{i+1}: register not valid")
                error=1
                break
            if ("FLAGS" in instruction):
                print(f"Error@Line{i+1}: illegal use of flag")
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
                print(f"Error@Line{i+1}: number is too large")
                error=1
                break
            else:
                zeroes = "0"*zeroes
                # print(type(im))
                # print(z)
                ans.append(a+r+zeroes+im)
        
        elif instruction[0]=="rs":
            if (instruction[1] not in reg):
                print(f"Error@Line{i+1}: register not valid")
                error=1
                break
            if ("FLAGS" in instruction):
                print(f"Error@Line{i+1}: illegal use of flag")
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
                print(f"Error@Line{i+1}: number is too large")
                error=1
                break
            else:
                zeroes = "0"*zeroes
                # print(type(im))
                # print(z)
                ans.append(a+r+zeroes+im)
        
        elif instruction[0]=="xor":
            if (instruction[1] not in reg) or (instruction[2] not in reg) or (instruction[3] not in reg):
                print(f"Error@Line{i+1}: register not valid")
                error=1
                break
            if ("FLAGS" in instruction):
                print(f"Error@Line{i+1}: illegal use of flag")
                error=1
                break
            a = opcode["xor"]
            r = registers[instruction[1]] + registers[instruction[2]] + registers[instruction[3]]
            zeroes = 11-len(r)
            zeroes = "0"*zeroes
            ans.append(a+zeroes+r)
        
        elif instruction[0]=="st":
            if instruction[2] not in vars:
                print(f"Error@Line{i+1}: variable not defined")
                error=1
                break
            if (instruction[1] not in reg):
                print(f"Error@Line{i+1}: register not valid")
                error=1
                break
            if ("FLAGS" in instruction):
                print(f"Error@Line{i+1}: illegal use of flag")
                error=1
                break
            if(instruction[2] not in addresses.keys()):
                print(f"Error@Line{i+1}: variable not defined")
                error=1
                break
            a = opcode["st"]
            r = registers[instruction[1]]
            # d = randomaddress()
            # x = var_addresses[instruction[2]]
            x=decimalToBinary(addresses[instruction[2]])
            zeroes=8-len(x)
            zeroes="0"*zeroes
            ans.append(a+r+zeroes+x)
        elif instruction[0]=="ld":
            if instruction[2] not in vars:
                print(f"Error@Line{i+1}: variable not defined")
                error=1
                break
            if (instruction[1] not in reg):
                print(f"Error@Line{i+1}: register not valid")
                error=1
                break
            if("FLAGS" in instruction):
                print(f"Error@Line{i+1}: illegal use of flag")
                error=1
                break
            if(instruction[2] not in addresses.keys()):
                print(f"Error@Line{i+1}: variable not defined")
                error=1
                break
            a = opcode["ld"]
            r = registers[instruction[1]]
            # d = randomaddress()
            # x = var_addresses[instruction[2]]
            x=decimalToBinary(addresses[instruction[2]])
            zeroes=8-len(x)
            zeroes="0"*zeroes
            ans.append(a+r+zeroes+x)

            
        elif instruction[0]=="or":
            if (instruction[1] not in reg) or (instruction[2] not in reg) or (instruction[3] not in reg):
                print(f"Error@Line{i+1}: register not valid")
                error=1
                break
            if ("FLAGS" in instruction):
                print(f"Error@Line{i+1}: illegal use of flag")
                error=1
                break
            a=opcode["or"]
            r=registers[instruction[1]] + registers[instruction[2]] + registers[instruction[3]]
            zeroes="0"*2
            ans.append(a+zeroes+r)

        elif instruction[0]=="and":
            if (instruction[1] not in reg) or (instruction[2] not in reg) or (instruction[3] not in reg):
                print(f"Error@Line{i+1}: register not valid")
                error=1
                break
            if ("FLAGS" in instruction):
                print(f"Error@Line{i+1}: illegal use of flag")
                error=1
                break
            a=opcode["and"]
            r=registers[instruction[1]] + registers[instruction[2]] + registers[instruction[3]]
            zeroes="0"*2
            ans.append(a+zeroes+r)

        elif instruction[0]=="not":
            if (instruction[1] not in reg) or (instruction[2] not in reg):
                print(f"Error@Line{i+1}: register not valid")
                error=1
                break
            if ("FLAGS" in instruction):
                print(f"Error@Line{i+1}: illegal use of flag")
                error=1
                break
            a=opcode["not"]
            r=registers[instruction[1]] + registers[instruction[2]]
            zeroes="0"*5
            ans.append(a+zeroes+r)

        elif instruction[0]=="cmp":
            if (instruction[1] not in reg) or (instruction[2] not in reg):
                print(f"Error@Line{i+1}: register not valid")
                error=1
                break
            if ("FLAGS" in instruction):
                print(f"Error@Line{i+1}: illegal use of flag")
                error=1
                break
            a=opcode["cmp"]
            r=registers[instruction[1]] + registers[instruction[2]]
            zeroes="0"*5
            ans.append(a+zeroes+r)
            
        elif instruction[0]=="jmp":
            a=opcode["jmp"]
            if (instruction[1] in labels):
                x=decimalToBinary(addresses[instruction[1]])
                zeroes=16 - (len(x)+5)
                zeroes="0"*zeroes
                ans.append(a+zeroes+x)
            else:
                error = 1
                print(f"Error@Line{i+1}: label not defined")
                break

        elif instruction[0]=="jlt":
            a=opcode["jlt"]
            if (instruction[1] in labels):
                x=decimalToBinary(addresses[instruction[1]])
                zeroes=16 - (len(x)+5)
                zeroes="0"*zeroes
                ans.append(a+zeroes+x)
            else:
                error = 1
                print(f"Error@Line{i+1}: label not defined")
                break

        elif instruction [0]=="jgt":
            a=opcode["jgt"]
            if (instruction[1] in labels):
                x=decimalToBinary(addresses[instruction[1]])
                zeroes=16 - (len(x)+5)
                zeroes="0"*zeroes
                ans.append(a+zeroes+x)
            else:
                error = 1
                print(f"Error@Line{i+1}: label not defined")
                break

        elif instruction[0]=="je":
            a=opcode["je"]
            if (instruction[1] in labels):
                x=decimalToBinary(addresses[instruction[1]])
                zeroes=16 - (len(x)+5)
                zeroes="0"*zeroes
                ans.append(a+zeroes+x)
            else:
                error = 1
                print(f"Error@Line{i+1}: label not defined")
                break
        elif instruction[0]=="addf":
            if (instruction[1] not in reg) or (instruction[2] not in reg) or (instruction[3] not in reg):
                print(f"Error@Line{i+1}: register not valid")
                error=1
                break
            if ("FLAGS" in instruction):
                print(f"Error@Line{i+1}: illegal use of flag")
                error=1
                break
            a = '00000'
            r = registers[instruction[1]] + registers[instruction[2]] + registers[instruction[3]]
            zeroes = 11-len(r)
            zeroes = "0"*zeroes
            ans.append(a+zeroes+r)
        
        elif instruction[0]=="subf":
            if (instruction[1] not in reg) or (instruction[2] not in reg) or (instruction[3] not in reg):
                print(f"Error@Line{i+1}: register not valid")
                error=1
                break
            if ("FLAGS" in instruction):
                print(f"Error@Line{i+1}: illegal use of flag")
                error=1
                break
            a = '00001'
            r = registers[instruction[1]] + registers[instruction[2]] + registers[instruction[3]]
            zeroes = 11-len(r)
            zeroes = "0"*zeroes
            ans.append(a+zeroes+r)
        
        elif instruction[0]=="movf":
            if (instruction[1] not in reg):
                    print(f"Error@Line{i+1}: register not valid")
                    error=1
                    break
            a = '00010'
            r = registers[instruction[1]]
            num = instruction[2][1:]
            reg_states[instruction[1]] = num
            templ = num.split(".")
            num_dec_places = len(templ[1])
            im = float_bin(num, num_dec_places)
            temp2 = im.split(".")
            exp = len(temp2[0]) - 1
            mantissa = im[1:].replace('.', '')
            zeroes_mantissa = 5-len(mantissa)
            zeroes_exp = 3-len(exp)
            zeroes = "0"*3
            # print(type(im))
            # print(z)
            ans.append(a+zeroes+zeroes_exp+exp+zeroes_mantissa+mantissa)
            
        
        elif instruction[0][-1]==":":
            get_label_address(i, instruction[1:])
            
    if error!=1:
        for a in ans:
            print(a)
        # print(labels)
