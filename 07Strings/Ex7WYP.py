"""

@author: CanOkan

Strings Course (Write Your Program)

"""

s = input("Enter a string: ")
char = input("Enter the character you do not want: ")

out = ""
for x in s:
    if x != char:
        out += x

print("Output string:",out)