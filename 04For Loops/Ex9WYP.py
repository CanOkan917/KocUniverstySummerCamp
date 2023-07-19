"""

@author: CanOkan

For Loops Course (Write Your Program)

"""

days = int(input("How many days? : "))
if days > 7 or days < 0:
    print("Are you living in Mars?")
else:
    exercises = int(input("Workout per day: "))
    total_calories = 0
    for day in range(1, days + 1):
        for exercise in range(1, exercises + 1):
            print("Day", day, ", Workout", exercise)
            exercise_type = int(input("Enter what move will you perform (1:pullup, 2:situp): "))
            if exercise_type != 1 and exercise_type != 2:
                print("Invalid movement")
            elif exercise_type == 1:
                total_calories += 20
            else:
                total_calories += 30
    print("Total", total_calories, "calories spend in this workout plan!")