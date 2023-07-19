"""

@author: CanOkan

For Loops Course (Write Your Program)

"""

import math

a = float(input("Enter start value: "))
b = float(input("Enter final value: "))

if a < b:
    for i in range(math.ceil(a), math.floor(b)+1):
        print(i, end=' ')