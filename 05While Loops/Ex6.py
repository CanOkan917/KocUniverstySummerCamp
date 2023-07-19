"""

@author: CanOkan

While Loops Course

"""

import math

start = float(input("Enter the start value: "))
final = float(input("Enter the final value: "))

while start >= final:
    print("Incorrect values! Start must be less than final!")
    start = float(input("Enter the start value: "))
    final = float(input("Enter the final value: "))

for i in range(math.ceil(start), math.floor(final) + 1):
    print(i, end=' ')