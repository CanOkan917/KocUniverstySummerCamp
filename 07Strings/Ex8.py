"""

@author: CanOkan

Strings Course

"""

password = input("Enter the password: ")

def vaild(password):
    limit = False
    upper = False
    number = False
    if len(password) >= 7:
        limit = True
        for i in password:
            if i.isupper():
                upper = True
            if i.isdigit():
                number = True
    return limit and upper and number
print(vaild(password))