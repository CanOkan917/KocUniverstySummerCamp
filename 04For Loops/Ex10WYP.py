"""

@author: CanOkan

For Loops Course (Write Your Program)

"""

size = int(input("Size of the table: "))

for col in range(1, size + 1):
    row_sum = 0
    for row in range(1, size + 1):
        row_sum += col + row
        print(col + row, end='\t')
    print("Row sum =", row_sum)