"""

@author: CanOkan

This program was written as an homework for
KOC University Summer Python Camp

Due Date: July 10, 2023, Monday, 23:59

Until this assignment was finished,
I only used the features and commands I learned.

For Loops: Work & Go on Vacation

"""

vacation_days = int(input("Desired number of vacation days: "))
if vacation_days < 4:
    print("Error! Desired vacation days cannot be less than 4.")
else:
    off_day_1 = int(input("Off-day1 (1-7): "))
    off_day_2 = int(input("Off-day2 (1-7): "))
    if off_day_1 < 1 or off_day_1 > 7 or off_day_2 < 1 or off_day_2 > 7:
        print("Error! Off days needs to be in range of 1 and 7.")
    elif off_day_1 == off_day_2:
        print("Off-days must be different.")
    else:
        weeks = int(input("Number of weeks: "))
        if weeks < 1:
            print("Error! Invalid weeks value.")
        else:
            total_earnings = 0
            for week in range(1, weeks + 1):
                for day in range(1, 8):
                    if day != off_day_1 and day != off_day_2:
                        total_earnings += day * week
            print("Total Money = ",total_earnings)
            for day in range(1, vacation_days + 1):
                day_spent = day + 10
                if day - (day // 7 * 7) == 6 or day - (day // 7 * 7) == 0: # weekend
                    day_spent *= 2
                if day_spent > total_earnings:
                    print("You do not have enough money for day", day)
                else:
                    total_earnings -= day_spent
                    print("At the end of day",day,"you have $",total_earnings,"left")