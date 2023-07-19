"""

@author: CanOkan

While Loops Course (Write Your Program)

"""

import math

# Variant 1
num = int(input("Enter a value: "))
k = num + 1
while k % 7 != 0:
    k += 1
print("First number >",num,"and divisible by 7 is",k)

# Variant 2
num = int(input("Enter a value: "))
k = 0
while k <= num:
    k += 7
print("First number >",num,"and divisible by 7 is",k)

# Variant 3
num = int(input("Enter a value: "))
for k in range(num + 1, num + 8):
    if k % 7 == 0:
        print("First number >",num,"and divisible by 7 is",k)

# Variant 4
num = int(input("Enter a value: "))
k = num - num % 7 + 7
print("First number >",num,"and divisible by 7 is",k)

# Variant 5
num = int(input("Enter a value: "))
k = math.ceil(num / 7)
if num == k ** 7:
    print("First number >",num,"and divisible by 7 is",k + 7)
else:
    print("First number >",num,"and divisible by 7 is",k * 7)