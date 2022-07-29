import math
import sys
from opcodes_dict import opcode, registers
from randomAddress import randomaddress
from register_states import reg_states
def binaryToDecimal(n):
    return int(n,2)    
def decimalToBinary(n):
    return bin(n).replace("0b", "")

def DecimalToBinary(n):
    return "{0:b}".format(int(n))

# print(op_list_valid)
def if_label(instruction):
    if instruction[-1] == ":":
        return True
    return False    
# opcodeDict={
#     "10000":3,
#     "10001":3,
#     "10010":1,
#     ""
# }
addr={}
regValue={
    "000":0,
    "001":0,
    "010":0,
    "011":0,
    "100":0,
    "101":0,
    "110":0,
}
reg = ["R0", "R1", "R2", "R3", "R4", "R5", "R6","FLAGS"]
error=0
label=[]
# commands = []
with open("Input.txt", 'r') as f:
    commands = f.read().splitlines()
# print(opcode)
# flags={
#     "V":0,
#     "L":0,
#     "G":0,
#     "E":0,

# }

flagval=0
pc=0
while pc<len(commands):
    flags={
    "V":0,
    "L":0,
    "G":0,
    "E":0,

    }
    pc_ = DecimalToBinary(int(pc))
    zeros = "0" * (8 - len(pc_))
    pc_ = zeros + pc_
    print(pc_, end=" ")
    jmpflag=0
    command=commands[pc]
    opcode=command[0:5]
    if opcode=="10000":
        regValue[command[10:16]]=regValue[command[10:13]]+regValue[command[7:10]]
        if regValue[command[10:16]]>127:
            regValue[command[10:16]]=127
            flags["V"]=1
    elif opcode=="10010":
        regValue[command[5:8]]=binaryToDecimal(command[8::])    
    elif opcode=="10011":
        if command[10:13]=="111":
            regValue[command[13:16]]=temp
            
        else:
            regValue[command[13:16]]=regValue[command[10:13]]
    elif opcode=="10110":
        regValue[command[10:16]]=regValue[command[10:13]]*regValue[command[7:10]]
        if regValue[command[10:16]]>127:
            regValue[command[10:16]]=127
            flags["V"]=1

    elif opcode=="10001":
        regValue[command[10:16]]=regValue[command[10:13]]-regValue[command[7:10]]
        if regValue[command[10:16]]<0:
            regValue[command[10:16]]=0
            flags["V"]=1
    elif opcode=="10111":
        q=regValue[command[10:13]]//regValue[command[13:16]] 
        rem=regValue[command[10:13]]%regValue[command[13:16]]
        regValue["000"]=q
        regValue["001"]=rem
    elif opcode=="11000":
        r1=command[5:8]
        im=command[8:16]
        regValue[r1]=regValue[r1]>>im
    elif opcode=="11001":
        r1=command[5:8]
        im=command[8:16]
        regValue[r1]=regValue[r1]<<im
    elif opcode=="11011":
        regValue[command[10:16]]=regValue[command[10:13]]|regValue[command[7:10]]
        if regValue[command[10:16]]>127:
            regValue[command[10:16]]=127
    elif opcode=="11100":
        regValue[command[10:16]]=regValue[command[10:13]]&regValue[command[7:10]]
        if regValue[command[10:16]]>127:
            regValue[command[10:16]]=127
    elif opcode=="11010":
        regValue[command[10:16]]=regValue[command[10:13]]^regValue[command[7:10]]
        if regValue[command[10:16]]>127:
            regValue[command[10:16]]=127 
    elif opcode=="11101":
        regValue[command[13:16]]=~regValue[command[10:13]]
    elif opcode=="10100":
        tempaddr=command[8:16]
        zero="0"*8
        zero+=tempaddr
        if zero not in addr.keys():
            addr[zero]=0
        regValue[command[0:5]]=addr[zero]
    elif opcode=="10101":
        tempaddr=command[8:16]
        zero="0"*8
        zero+=tempaddr
        
        addr[zero]=regValue[command[0:5]]
    elif opcode=="11110":
        if regValue[command[10:13]]==regValue[command[13:16]]:
            flags["E"]=1
        elif regValue[command[10:13]]>regValue[command[13:16]]:
            flags["G"]=1
        else:
            flags["L"]=1
        # print(flags)    
    elif opcode=="11111":
        zero="0"*8
        zero+=command[8:16]
        if zero not in label:
            label.append(zero)
        pc=binaryToDecimal(command[8:16])
        jmpflag=1
        continue
    elif opcode=="01100":
        if flags["L"]==1:
            zero="0"*8
            zero+=command[8:16]
            if zero not in label:
                label.append(zero)
            pc=binaryToDecimal(command[8:16])
            jmpflag=1
    elif opcode=="01101":
        if flags["G"]==1:
            zero="0"*8
            zero+=command[8:16]
            if zero not in label:
                label.append(zero)
            pc=binaryToDecimal(command[8:16])
            jmpflag=1
    elif opcode=="01111":
        if flags["E"]==1:
            zero="0"*8
            zero+=command[8:16]
            if zero not in label:
                label.append(zero)
            pc=binaryToDecimal(command[8:16])
            jmpflag=1
    # elif opcode=="01010":
    #     break        
            
                
    for k in regValue.values():
        bin = DecimalToBinary(int(k))
        zeros = "0" * (16 - len(bin))
        bin = zeros + bin
        print(bin, end=" ")
    flg_str = "000000000000"
    for k in flags.keys():
        flg_str+=str(flags[k])
    print(flg_str)
    temp=flags["V"]*(2**3)+flags["L"]*(2**2)+flags["G"]*(2**1)+flags["E"]*1
                        
    if jmpflag==0:
        pc+=1
    else:
        continue        

        
for c in commands:
    print(c)
for _ in range(256-len(commands)):
    print("0000000000000000")