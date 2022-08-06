import math
import sys
import matplotlib.pyplot as plt
from rev_opcode_dict import rev_opcode
x_axis=[]
y_axis=[]
data=[]
ldst=2
opcd=1
with open("Input.txt",'r') as ip:
    dat=ip.read().splitlines()
    data.append(dat)
ip1=[]
cnt=0
for v in dat:
    opcode=v[0:5]
    if opcode=="10100" or opcode=="10101":
        y_axis.append(ldst)
    else:
        y_axis.append(opcd)
    x_axis.append(cnt+1)
    cnt=cnt+1
plt.style.use('seaborn')
plt.xlabel("Number of cycles")
plt.ylabel("Instances of memory access")
plt.scatter(x_axis,y_axis,s=10)
plt.tight_layout()
plt.show()
