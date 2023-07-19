"""

@author: CanOkan

Lists Course (Write Your Program)

"""

def find_min_avg_max(lst):
    min = float("inf")
    max = float("-inf")
    avg = 0
    for e in lst:
        if e < min:
            min = e
        if e > max:
            max = e
        avg += e
    return min, (avg / len(lst)), max

lst = []
for i in range(4):
    num = int(input("Enter a number: "))
    lst.append(num)
print(find_min_avg_max(lst))