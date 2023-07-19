"""

@author: CanOkan

Functions Course

"""

def mult10():
    n = int (input("Enter a num: "))
    result = n * 10
    return result

def find_sqrt():
    output = mult10() ** 0.5
    return output

print(find_sqrt())