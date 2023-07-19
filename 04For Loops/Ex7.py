"""

@author: CanOkan

For Loops Course

"""

start = int(input("Enter start value: "))
final = int(input("Enter final value: "))

x = int(input("Enter x value: "))
y = int(input("Enter y value: "))

print()

found_x = False
found_y = False

for i in range(start, final+1):
    if i % x == 0:
        found_x = True
    
    if i % y == 0:
        found_y = True
        
if found_x:
    print("There is multiple of",x)
else:
    print("There is no multiple of",x)
    
if found_y:
    print("There is multiple of",y)
else:
    print("There is no multiple of",y)