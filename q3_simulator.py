import math
import sys
from opcodes_dict import opcode, registers
from randomAddress import randomaddress
from register_states import reg_states

def floatingbinaryToDecimal(binary, length) :
     
    # Fetch the radix point
    point = binary.find('.')
 
    # Update point if not found
    if (point == -1) :
        point = length
 
    intDecimal = 0
    fracDecimal = 0
    twos = 1
 
    # Convert integral part of binary
    # to decimal equivalent
    for i in range(point-1, -1, -1) :
         
        # Subtract '0' to convert
        # character into integer
        intDecimal += ((ord(binary[i]) -
                        ord('0')) * twos)
        twos *= 2
 
    # Convert fractional part of binary
    # to decimal equivalent
    twos = 2
     
    for i in range(point + 1, length):
         
        fracDecimal += ((ord(binary[i]) -
                         ord('0')) / twos);
        twos *= 2.0
 
    # Add both integral and fractional part
    ans = intDecimal + fracDecimal
     
    return ans

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
reg_codes_l = ["000","001","010","011","100","101","110"]
reg = ["R0", "R1", "R2", "R3", "R4", "R5", "R6","FLAGS"]
error=0
label=[]
with open("Input.txt", 'r') as f:
    commands = f.read().splitlines()

# commands = []
# for line in sys.stdin:
#     commands.append(line.strip())
#     if line.strip()=="0101000000000000":
#         break

# print(commands)
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
        regValue[command[13:16]]=regValue[command[10:13]]+regValue[command[7:10]]
        if regValue[command[13:16]]>127:
            regValue[command[13:16]]=127
            flags["V"]=1
    elif opcode=="10010":
        regValue[command[5:8]]=binaryToDecimal(command[8::])    
    elif opcode=="10011":
        if command[10:13]=="111":
            regValue[command[13:16]]=temp
            
        else:
            regValue[command[13:16]]=regValue[command[10:13]]
    elif opcode=="10110":
        regValue[command[13:16]]=regValue[command[10:13]]*regValue[command[7:10]]
        if regValue[command[13:16]]>127:
            regValue[command[13:16]]=127
            flags["V"]=1

    elif opcode=="10001":
        regValue[command[13:16]]=regValue[command[10:13]]-regValue[command[7:10]]
        if regValue[command[13:16]]<0:
            regValue[command[13:16]]=0
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
        regValue[command[13:16]]=regValue[command[10:13]]|regValue[command[7:10]]
        if regValue[command[13:16]]>127:
            regValue[command[13:16]]=127
    elif opcode=="11100":
        regValue[command[13:16]]=regValue[command[10:13]]&regValue[command[7:10]]
        if regValue[command[13:16]]>127:
            regValue[command[13:16]]=127
    elif opcode=="11010":
        regValue[command[13:16]]=regValue[command[10:13]]^regValue[command[7:10]]
        if regValue[command[13:16]]>127:
            regValue[command[13:16]]=127 
    elif opcode=="11101":
        regValue[command[13:16]]=~regValue[command[10:13]]
    elif opcode=="10100":
        tempaddr=command[8:16]
        zero="0"*8
        zero+=tempaddr
        if zero not in addr.keys():
            addr[zero]=0
        regValue[command[5:8]]=addr[zero]
    elif opcode=="10101":
        tempaddr=command[8:16]
        zero="0"*8
        zero+=tempaddr
        
        addr[zero]=regValue[command[5:8]]
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
    elif opcode=="00010":
        exp = command[8:11]
        mantissa = command[11:16]
        exp = binaryToDecimal(exp)
        a = float(f'1.{mantissa}')*(10**exp)
        val = "{0:.7f}".format(a)
        val = str(float(val))
        val = floatingbinaryToDecimal(val, len(val))
        regValue[command[5:8]] = val
    
    elif opcode=="00000":
        regValue[command[13:16]]=regValue[command[10:13]]+regValue[command[7:10]]
        if regValue[command[13:16]]>127:
            regValue[command[13:16]]=127
            flags["V"]=1
                
    for k, val in regValue.items():
        # val_ = str(val)
        if k in reg_codes_l:
            if int(val)!=val:
                val = str(val)
                templ = val.split(".")
                num_dec_places = len(templ[1])
                im = float_bin(val, num_dec_places)
                temp2 = im.split(".")
                exp = len(temp2[0]) - 1
                mantissa = im[1:].replace('.', '')
                exp = str(DecimalToBinary(int(exp)))
                man_zeros = 5-len(mantissa)
                man_zeros = "0"*man_zeros
                bin_ = str(exp) + mantissa + man_zeros
                zeros = "0" * (16 - len(bin_))
                bin_ = zeros + bin_
                print(bin_, end=" ")
            else:
                bin_ = DecimalToBinary(int(val))
                zeros = "0" * (16 - len(bin_))
                bin_ = zeros + bin_
                print(bin_, end=" ")
    flg_str = "000000000000"
    for k in flags.keys():
        flg_str+=str(flags[k])
    print(flg_str)
    temp=flags["V"]*(2**3)+flags["L"]*(2**2)+flags["G"]*(2**1)+flags["E"]*1

    if jmpflag==0:
        pc+=1
    else:
        continue        

# print(regValue)
for c in commands:
    print(c)
for _ in range(256-len(commands)):
    print("0000000000000000")