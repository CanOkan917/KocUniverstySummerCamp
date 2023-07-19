"""

@author: CanOkan, Kaan

Conditional Statements Course (Write Your Program)

"""

import math

initial_floor = int(input("Enter te initial floor: "))
destination_floor = int(input("Enter the final floor: "))
load = int(input("Load: "))

if initial_floor <= 0 or initial_floor > 9 or destination_floor <= 0 or destination_floor > 9 or load <= 0:
    print("Either your floor numbers or load is invalid")
else:
    min_load = 0
    max_load = 0

    if destination_floor % 2 == 1:
        # even
        min_load = math.pow(destination_floor, 2) - math.pow(initial_floor, 2)
        max_load = math.pow(destination_floor, 2) + math.pow(initial_floor, 2)
    else:
        # odd
        min_load = math.pow(destination_floor, 3) - math.pow(initial_floor, 3)
        max_load = math.pow(destination_floor, 3) + math.pow(initial_floor, 3)

    if initial_floor == destination_floor:
        print("Elevator will stay floor:",initial_floor)
    elif min_load < load and load < max_load:
        print("Elevator will move")
    else:
        print("Elevator will not move")