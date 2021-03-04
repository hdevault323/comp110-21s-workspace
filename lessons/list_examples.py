"""Some examples of list concepts."""

rolls: list[int] #declare a variable whose type is listof ints

rolls = [2, 3, 2, 6] #Initialize w/list literal syntax

print(f"Length of rolls is {len(rolls)}")
print(f"The last item in the list is {rolls[len(rolls)-1]}")


from random import randint
rolls.append(randint(1, 6)) #List's append method adds to the end of a list
print(rolls)

rolls.pop() #List's pop method with no argument removes the last item of the list
rolls.pop(0) #List pop method with one argument, pops a specific index
print(rolls)

words: list[str] = list() #construct an empty list using the list constructor
words.append("Hello")
print(words)