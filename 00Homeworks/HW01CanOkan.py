"""

@author: CanOkan

This program was written as an homework for
KOC University Summer Python Camp

Due Date: July 6, 2023, Thursday, 23:59

Until this assignment was finished,
I only used the features and commands I learned.

Conditional Statements: Grocery Shopping

"""

import math

grocery_shop = int(input("Wich grocery shop do you want to select (1/2/3): "))

if grocery_shop != 1 and grocery_shop != 2 and grocery_shop != 3:
    print("Invalid selection!")
else:
    coast = float(input("How much do your groceries cost?: "))
    if grocery_shop == 2:
        add_granola = int(input("Granola is on sale ($9.45)! Do you want to add it to the basket? (0:No/1:Yes): "))
        if add_granola != 1 and add_granola != 0:
            print("Invalid selection!")
        elif add_granola == 1:
            coast += 9.45

    delivery_type = int(input("Do you want to get free delivery or in-store pick up? (Delivery:0/Pickup:1): "))
    if delivery_type == 0:
        total_items = int(input("How many items did you buy?: "))
        bag_type = int(input("Bag type (0:Plastic/1:Reusable): "))
        if bag_type != 1 and bag_type != 0:
            print("Invalid selection!")
        elif bag_type == 0 and total_items > 0:
            bags = math.ceil(total_items / 4)
            coast += (bags * 1.5)
            print(bags, "bags are needed for your basket.")
        elif bag_type == 1 and total_items > 0:
            bags = math.ceil(total_items / 6)
            coast += (bags * 3)
            print(bags, "bags are needed for your basket.")
    elif delivery_type == 1:
        coast -= (coast/100) * 5
    else:
        print("Invalid selection!")
    
    print("Total cost: $", coast)