import random
import string

# Helper function
def decimalToBinary(n):
    return bin(n).replace("0b", "")

def randomaddress(total_var_ins, total_ins, add):
    # d = {}
    diff = total_ins - total_var_ins
    total_add = diff+add
    partial = decimalToBinary(total_add)
    zeros = 8-len(partial)
    zeros = "0"*zeros
    final = zeros+partial
    return final

# print(randomaddress())

# print(randomaddress())