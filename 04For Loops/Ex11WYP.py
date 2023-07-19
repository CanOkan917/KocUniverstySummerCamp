"""

@author: CanOkan

For Loops Course (Write Your Program)

"""

tickets = int(input("How many tickets do you have?: "))

total_earnings = 0
for ticket in range(1, tickets + 1):
    print("\t\t\tTicket #",ticket)
    for row in range(1, 4):
        print("\tRow #",row)
        digits = int(input("What is your four digit code this row?: "))
        if digits % 7 == 0:
            total_earnings += 10
        else:
            total_earnings += 1
print("You won",total_earnings,"dollars!")