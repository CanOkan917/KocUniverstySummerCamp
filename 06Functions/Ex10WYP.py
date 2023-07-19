"""

@author: CanOkan

Functions Course (Write Your Program)

"""

TAX_RATE = 0.08
CUSTOMER_TRESHOLD = 5
HIGH_TIP_RATE = 0.2
LOW_TIP_RATE = 0.15

def get_tip(bill, customers):
    if customers >= CUSTOMER_TRESHOLD:
        return bill * HIGH_TIP_RATE
    return bill * LOW_TIP_RATE

def get_tax(bill):
    return bill * TAX_RATE

def calculate_meal_total():
    bill = float(input("Emter the cost of meal: "))
    n_people = int(input("Enter the number of customers: "))
    tip = get_tip(bill, n_people)
    tax = get_tax(bill)
    total = bill + tip + tax
    return tip, tax, total

tip, tax, total = calculate_meal_total()
print("Tax:",tax)
print("Tip:",tip)
print("Total:",total)