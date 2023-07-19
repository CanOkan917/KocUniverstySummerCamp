"""

@author: CanOkan

While Loops Course

"""

import random

secret = random.randint(1, 50)
n = 1

guess = int(input("Enter your guess: "))

while secret != guess and n < 5:
    if guess > secret:
        print("Go down!")
    else:
        print("Go up!")
    guess = int(input("Enter your guess: "))
    n += 1

if guess == secret:
    print("Congrats! You guessed it!")
else:
    print("You busted! The secret number was", secret)