"""

@author: CanOkan

Functions Course (Write Your Program)

"""

def calculate_avg_and_lowest(first_quiz, second_quiz):
    lowest = min(first_quiz, second_quiz)
    avg = (first_quiz + second_quiz) / 2
    return avg, lowest

def main():
    students = int(input("Number of students: "))
    while students < 1 or students > 10:
        print("Student number needs to be in range of [1, 10]")
        students = int(input("Reenter number of students: "))

    for student in range(1, students + 1):
        print("Student", student)
        first_quiz = int(input("Enter grade for the first quiz: "))
        second_quiz = int(input("Enter grade for the second quiz: "))
        avg, lowest = calculate_avg_and_lowest(first_quiz, second_quiz)
        print("Student",student,"'s average grade is",avg)
        print("Her/His lowest grade is",lowest)

main()