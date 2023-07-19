"""

@author: CanOkan

Functions Course (Write Your Program)

"""

import random
random.seed(199)

def roll_dice(money):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    print("You rolled", dice1, dice2)
    if dice1 == dice2:
        money *= 2
    elif dice1 > dice2:
        money += 50
    else:
        money -= 50
    return money

def play_game(curr, target):
    counter = 0
    while curr < target:
        curr = roll_dice(curr)
        print("Current money = $",curr)
        counter += 1
    print("\nIt took",counter,'turns to reach (or exceed) $',target)

def main():
    start = int(input('How much money do you have: '))
    target = int(input('How much money do you want: '))
    play_game(start, target)

main()