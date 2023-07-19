"""

@author: CanOkan

Strings Course

"""

s = input("Enter a string: ")
a = input("Enter a characther: ")
vowels = "aeiouAEIOU"
for v in vowels:
    s = s.replace(v, a)
print(s)