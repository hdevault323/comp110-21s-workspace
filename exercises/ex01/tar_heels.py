"""An exercise in remainders and boolean logic."""

__author__ = "730236759"


# Begin your solution here...
number: int = input("Enter an int:")

if int(number) % 2 == 0 and int(number) % 7 == 0:
    print ("TAR HEELS")
else: 
    if int(number) % 2 == 0:
        print ("TAR")
    else: 
        if int(number) % 7 == 0: 
            print ("HEELS")
        else: 
            print ("CAROLINA")



