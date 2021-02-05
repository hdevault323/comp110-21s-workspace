"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730236759"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...


print("Your fortune cookie says...")

cookie_input= int(randint (0,100)) 
if cookie_input < 25:
    print("Good fortunes are coming your way!")
else: 
    if cookie_input < 50:
        print("You will have a fantastic day!")
    else: 
        if cookie_input < 75:
            print("You will have a long and happy life!")
        else: 
            if cookie_input <= 100:
                print("Someone specail is coming into your life!")

print("Now, go spread positive vibes!")