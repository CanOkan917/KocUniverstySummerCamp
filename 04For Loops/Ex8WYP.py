"""

@author: CanOkan

For Loops Course (Write Your Program)

"""

start = int(input("Enter start value: "))
final = int(input("Enter final value: "))

for _ in range(5):
    for i in range(start, final+1):
        print(i, end=' ')
    print()