"""

@author: CanOkan

Conditional Statements Course (Write Your Program)

"""

# Variant 1
s= int(input('Enter your standing number:  '))
if s==1:
    print('You are a Freshman')
elif s==2:
    print('You are a Sophomore')
elif s==3:
    print('You are a Junior')
elif s==4:
    print('You are a Senior')
elif s==5 or s==6:
    print('You are a graduate student')
else:
    print('Please give a number between 1-6')

# Variant 2
s= int(input('Enter your standing number:  '))
if s<1 or s>6:
    print('Please give a number between 1-6')
elif s==1:
    print('You are a Freshman')
elif s==2:
    print('You are a Sophomore')
elif s==3:
    print('You are a Junior')
elif s==4:
    print('You are a Senior')
else:
    print('You are a graduate student')

# Variant 3
s= int(input('Enter your standing number:  '))
if s==1:
    print('You are a Freshman')
if s==2:
    print('You are a Sophomore')
if s==3:
    print('You are a Junior')
if s==4:
    print('You are a Senior')
if s==5 or s==6:
    print('You are a graduate student')
if s<1 or s>6:
    print('Please give a number between 1-6')


# Benim çözümüm
s = int(input('Enter your standing number:  '))
grade = ["Freshman", "Sophomore", "Junior", "Senior", "Master student", "PhD student"]
if s <= 0 or s > len(grade):
    print("You can only give numbers 1-6")
else:
    print(f'You are a {grade[s-1]}')