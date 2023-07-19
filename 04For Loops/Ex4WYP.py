"""

@author: CanOkan

For Loops Course (Write Your Program)

"""

n = int(input("How many numbers do you want to sum? "))
s = 0
for i in range(n):
    num = float(input("Enter a number: "))
    s += num
print("The sum of given numbers is", s)
