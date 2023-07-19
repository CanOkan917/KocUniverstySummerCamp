"""

@author: CanOkan

While Loops Course

"""

num = int(input("Enter a number: "))
s = num
while num != 0:
    num = int(input("Enter a number: "))
    s += num
print("The sum of the given numbers is",s)