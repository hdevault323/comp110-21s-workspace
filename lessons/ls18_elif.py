"""Example of elif."""

number: int = int(input("Pick a number: "))
answer: int = 50 


#This form of else-if statement....
number < answer: 
    print("too low")
else: 
    if number > answer: 
        print("Too high.")
    else: 
        print("You got it!")


#Is the same as using elif in this way
if number < answer:
    print("too low")
elif number > answer:
    print("Too high.")
else:
    print("you got it!")


