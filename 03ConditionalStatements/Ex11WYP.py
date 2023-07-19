"""

@author: CanOkan, Kaan

Conditional Statements Course (Write Your Program)

"""

income = float(input("Amount of income per year: "))
loan = float(input("Amount of credit: "))
years = int(input("Number of years to pey back: "))

if income < 60000:
    print("You are not eligible for a loan.")
elif years < 1 or years > 5:
    print("Number of years has to be at least 1, at most 5.")
else:
    if loan / years < income / 2:
        print("You are eligible for a loan.")
    else:
        print("You are not eligible for a loan.")