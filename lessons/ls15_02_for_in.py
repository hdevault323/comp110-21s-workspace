"""for...in loop examples."""

#Iterate tthrough each item in a list
letters: list[str] = ["a", "b", "c", "d", "e", "f", "g"]

#print each letter in letters list one by one
print("Each letter...")
for letter in letters: 
    print(letter)


#What if you wanted to print every other letter in letters list?
print("Every other letter...")
for i in range(0, len(letters), 2):
    print(letters[i])
    #the reason we can write a for in loop for a list and a 
    #range goes back to the idea that we are able to iterate through each item in 
    #a sequence
    #We can fo all these things and more with while loops
    #For most things we will do, for in loops will be sufficient


print("If we had started our range at index of 1... ")
for i in range(1, len(letters), 2): #starts at b and not a and then excludes the g at the end
    print(letters[i])


#Use range to iterate through each index in a sequence
print("Every Index....")
for i in range(len(letters)):
    print(f"{i} - leetters[i]: {letters[i]}")
    