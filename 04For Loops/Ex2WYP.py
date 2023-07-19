"""

@author: CanOkan

For Loops Course (Write Your Program)

"""

how_many_num = int(input("How many numbers do you want to give: "))
for i in range(how_many_num):
    num = float(input("Enter number: "))
    print("You entered:",num)


n =  int(input("Enter n:"))
for i in range(1, n+1):
    print(i, i**2, i**3)