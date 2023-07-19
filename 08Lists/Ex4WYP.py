"""

@author: CanOkan

Lists Course (Write Your Program)

"""

def find_min(list):
    minn = float("inf")
    for i in list:
        if i < minn:
            minn = i
    return minn

list = [2.3, 5.7, -13, 1.6, -4.5]
print(find_min(list))