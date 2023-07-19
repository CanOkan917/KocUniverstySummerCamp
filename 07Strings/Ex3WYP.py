"""

@author: CanOkan

Strings Course (Write Your Program)

"""

def reverse_string(str):
    return str[-1::-1]

print(f'The reversed string is {reverse_string(input("Enter a string: "))}')