"""

@author: CanOkan

Functions Course

"""

def sum_sq(a, b):
    return a ** 2 + b ** 2

n1 = int(input("Enter a number: "))
n2 = int(input("Enter a number: "))

# Variant 1
print(sum_sq(n1, n2))

# Variant 2
output = sum_sq(n1, n2)
print(output)