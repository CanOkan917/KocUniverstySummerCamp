"""

@author: CanOkan

Functions Course (Write Your Program)

"""

def my_abs(a):
    if a >= 0:
        return a
    return -a

num = float(input("Enter a number: "))
print("Its absoulute value is", my_abs(num))