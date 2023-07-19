"""

@author: CanOkan

Conditional Statements Course

"""

# Variant 1
base_lenght = float(input("Enter base lenght: "))

if base_lenght <= 0:
    print("Base must be positive!")
else:
    height = float(input("Enter height: "))

    if height <= 0:
        print("Height must be positive!")
    else:
        area = (base_lenght * height) / 2
        
        print(f'Area of Triangle with b={base_lenght} and h={height} is {area}')

# Variant 2
base_lenght = float(input("Enter base lenght: "))
height = float(input("Enter height: "))
if base_lenght <= 0:
    print("Base must be positive!")
elif height <= 0:
    print("Height must be positive!")
else:
    area = (base_lenght * height) / 2
    print(f'Area of Triangle with b={base_lenght} and h={height} is {area}')

# Variant 3
base_lenght = float(input("Enter base lenght: "))
height = float(input("Enter height: "))
if base_lenght <= 0 and height <= 0:
    print('Both base and height must be positive!')
elif base_lenght <= 0:
    print("Base must be positive!")
elif height <= 0:
    print("Height must be positive!")
else:
    area = (base_lenght * height) / 2
    print(f'Area of Triangle with b={base_lenght} and h={height} is {area}')

# Variant 4
base_lenght = float(input('Enter base length:  '))
height = float(input('Enter height:  '))
if base_lenght <= 0:
    print('Base must be positive!')
if height <= 0:
    print('Height must be positive!')
if base_lenght > 0 and height > 0:
    area = (base_lenght * height) / 2
    print(f'Area of Triangle with b={base_lenght} and h={height} is {area}')

# Variant 5
base_lenght = float(input('Enter base length:  '))
height = float(input('Enter height:  '))
if base_lenght <= 0 or height <= 0:
    print('Base and height must be positive!')
else:
    area = (base_lenght * height) / 2
    print(f'Area of Triangle with b={base_lenght} and h={height} is {area}')