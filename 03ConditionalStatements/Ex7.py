"""

@author: CanOkan

Conditional Statements Course

"""

age = int(input("Enter your age: "))

if age >= 1 and age < 5:
    print("You are a baby.")
elif age > 5 and age < 12:
    print("You are a child.")
elif age >= 12 and age < 18:
    print("You are a teenager.")
else:
    print("You are old.")