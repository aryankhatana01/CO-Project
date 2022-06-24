import random
import string

# Helper function
def decimalToBinary(n):
    return bin(n).replace("0b", "")

def randomaddress():
    d = dict(zip(string.ascii_uppercase, range(1, 27)))
    for key, val in d.items():
        partial = str(decimalToBinary(val))
        zeros = 8-len(partial)
        zeros = "0"*zeros
        final = zeros+partial
        d[key] = final
    return d
# print(randomaddress())

# print(randomaddress())