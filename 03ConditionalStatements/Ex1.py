"""

@author: CanOkan

Conditional Statements Course

"""

# Area of a triangle
base_lenght = float(input("Enter base lenght: "))
height = float(input("Enter height: "))

if base_lenght <= 0 or height <= 0:
    print("You need to enter a positive number.")

if base_lenght > 0 and height > 0:
    area = (base_lenght * height) / 2

    print(f'Area of Triangle with b={base_lenght} and h={height} is {area}')