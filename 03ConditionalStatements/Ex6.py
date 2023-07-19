"""

@author: CanOkan

Conditional Statements Course

"""

age = int(input("Enter your age: "))

if age < 13:
    print("You are a child.")
else:
    # age >= 13
    if age >= 13:
        print("You are an adult.")
    else: # >= 13 and age < 18
        print("You are a teenager.")