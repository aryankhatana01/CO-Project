print(' ')
print("_____________________Memory Mumbo Jumbo_____________________")
print(' ')
print("PLease enter the memory space")
mem_space=[str(i) for i in input().split()]
value=int(mem_space[0])
size=[]
mem=mem_space[1]
bit_flag=1
true_Sz=[]
int_val=0
a=0
bt=["b","kb","Mb","Gb","Tb","Pb","Eb"]
byt=["B","kB","MB","GB","TB","PB","EB"]

print(mem_space[1])
if mem_space[1] in bt:
    bit_flag=0
else:
    bit_flag=1

int_val_conv=0
pow=1
while(a!=value):
    a=2**pow
    pow=pow+1
int_val_conv=pow-1
if mem=="Bit Addressable Memory":
    int_val_conv=8*int_val_conv
elif mem=="Nibble Addressable Memory":
    int_val_conv=4*int_val_conv
elif mem=="Byte Addressable Memory":
    int_val_conv=int_val_conv
else:
    int_val_conv=int_val_conv


if(bit_flag==1):
    if(mem_space[1]=="B"):
        int_val=0
    elif(mem_space[1]=="KB" or "kB"):
        int_val=10
    elif(mem_space[1]=="MB" or "mB"):
        int_val=20
    elif(mem_space[1]=="GB" or "gB"):
        int_val=30
    elif(mem_space[1]=="TB" or "tB"):
        int_val=40
    elif(mem_space[1]=="PB" or "pB"):
        int_val=50
    elif(mem_space[1]=="EB" or "eB"):
        int_val=60
elif (bit_flag==0):
    if(mem_space[1]=="b"):
        int_val=0
    elif(mem_space[1]=="Kb" or "kb"):
        int_val=10
    elif(mem_space[1]=="Mb" or "mb"):
        int_val=20
    elif(mem_space[1]=="Gb" or "gb"):
        int_val=30
    elif(mem_space[1]=="Tb" or "tb"):
        int_val=40
    elif(mem_space[1]=="Pb" or "pb"):
        int_val=50
    elif(mem_space[1]=="Eb" or "eb"):
        int_val=60

if (bit_flag==1):
    val_conv=int_val+int_val_conv
elif bit_flag==0:
    val_conv=(int_val-3)+int_val_conv

print(' ')
print("The types of memory are...")
print("1).Bit Addressable Memory")
print("2).Nibble Addressable Memory")
print("3).Byte Addressable Memory")
print("4).Word Addressable Memory")
mem_type= str(input("Please enter the type of memory..."))
print(' ')
print(' ')

print("_______________________________Part 1_______________________________")
print(' ')
print("The format for instructions is as follows:")
print("<Q bit opcode> <P-bit address> <n bit register>")
print("<Q bit opcode> <R bits filler> <n bit register> <n bit register>")
print(' ')
print("For the query enter the following values:")
l_ins=int(input("Enter the length of one instruction in bits : "))
l_reg=int(input("Enter the length of one register in bits : "))
print(" ")

tot_bits=val_conv
opcode=l_ins-(tot_bits+l_reg)
fil_bits=l_ins-(opcode+(2*l_reg))
n_ins=2**opcode
n_reg=2**l_reg
print("The number of bits required to represent an address is :",tot_bits)
print("The number of bits needed by the opcode are :",opcode)
print("The number of filler bits required are :",fil_bits)
print("The number of instructions that the given ISA can support are :",n_ins)
print("The number of registers that the given ISA can support are :",n_reg)
print(' ')
print(' ')


print("_______________________________Part 2_______________________________")
print(' ')
print("_______________________________Type 1_______________________________")
print("The initial memory space as given by the user is :",mem_space[0],mem_space[1])
print("The initial type of memory as given by the user is :",mem_type)
print(' ')
print("Enter the number of bits in the cpu")
cpu=[str(i) for i in input().split()]
new_mem=str(input("Enter the type of memory :"))
cpu_value=int(cpu[0])
cpu_value=int(cpu_value/8)
cpu_sz=0
pins_saved=0
a=0
pow=0
val=0
val1=0
val2=0
pow=0
while(val!=cpu_value):
    val=2**pow
    pow=pow+1
val1=pow-1

bt=["b","kb","Mb","Gb","Tb","Pb","Eb"]
byt=["B","kB","MB","GB","TB","PB","EB"]




val=val-3
if new_mem=="Bit Addressable Memory":
    val1=8*val1
elif new_mem=="Nibble Addressable Memory":
    val1=4*val1
elif new_mem=="Byte Addressable Memory":
    val1=val1
# elif new_mem=="Word Addressable Memory" or 'enhanced with word addressable memory':
    
if(mem_type==new_mem):
    print("The number of pins saved is :",0)
else:
    # if new_mem=="Word Addressable Memory" or "enhanced with word addressable memory":
    #     cpu_sz=val_conv-val1
    if mem_type=="Bit Addressable Memory":
        if new_mem=="Nibble Addressable Memory":
            cpu_sz=val_conv-2
        elif new_mem=="Byte Addressable Memory":
            cpu_sz=val_conv-3
        elif new_mem=="Word Addressable Memory":
            cpu_sz=val_conv-val1-3
    elif mem_type=="Nibble Addressable Memory":
        if new_mem=="Bit Addressable Memory":
            cpu_sz=val_conv+2
        elif new_mem=="Byte Addressable Memory":
            cpu_sz=val_conv-2
        elif new_mem=="Word Addressable Memory":
            cpu_sz=val_conv-val1-2
    elif mem_type=="Byte Addressable Memory":
        if new_mem=="Bit Addressable Memory":
            cpu_sz=val_conv+3
        elif new_mem=="Nibble Addressable Memory":
            cpu_sz=val_conv+2
        elif new_mem=="Word Addressable Memory":
            cpu_sz=val_conv-val1

print(cpu_sz)
    
pins_saved=cpu_sz-tot_bits
print("The number of pins saved are :",pins_saved)

print(' ')
print("_______________________________Type 2_______________________________")
print(' ')
print("Please enter the size of cpu :")
size_of_cpu=[str(i) for i in input().split()]
soc=size_of_cpu[0]
v1=0
v2=0
data={
    0 : 'B',
    10 : "kB",
    20 : "MB",
    30 : "GB",
    40 : "TB",
    50 : "PB"
}
print("Please enter the number of address pins :")
add_pins=[str(i) for i in input().split()]
adpns=add_pins[0]
adpns=int(adpns)
adp=0
x1=0
x2=1
print("Please enter the type of memory :")
m_type=str(input())
if m_type!="Word Addressable Memory":
    adp=adpns
    while(adpns%10!=0):
        adpns=adpns-1
        v1=v1+1
    v2=adp-v1
    print("The size of the main memory is :",2**v1,data[v2])
else:
    sc=int(soc)/8
    sc=int(sc)
    while(x1!=sc):
        x1=2**x2
        x2=x2+1
    adpns=adpns+(x2-1)
    adp=adpns
    while(adpns%10!=0):
        adpns=adpns-1
        v1=v1+1
    v2=adp-v1
    print("The size of the main memory is :",2**v1,data[v2])


    