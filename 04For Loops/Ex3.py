"""

@author: CanOkan

For Loops Course

"""

# 1 + 2 + ...... + 10

# n = int(input("Until wich number do you want to sum up?: "))
# s = 0
# for i in range(1, n + 1):
#     s += i
# print(s)

n = int(input("Enter n: "))
f = 1
for i in range(1, n+1):
    f *= i
print(n, "!=", f)