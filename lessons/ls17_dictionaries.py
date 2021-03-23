"""Examples of dictionaries."""

#Establish a type with dict[key type, value type]
#Empty dictionary literal is {}
#key type always preceeds value type
players: dict[str, int] = {}

#Insert a new key-value pair
#Refernce keys inside subscription notation, associated values are assigned
players["Brooks"] = 15
players{"Love"] = 2
players["Bacot"] = 5
print(players)


#How to update values
players["Brooks"] = 15
players{"Love"] = 2
players["Bacot"] = 4 #This is intentionally off by one 
players["Bacot"] = players["Bacot"] + 1 #replaces Bacot value and increases it by one
print(players)


#for...in loops will give you each key one-by-one
#Player_name could be any variable
#when you use a for... in loop in python with dictionaries, it willg ive you each key one after another by default
#this will be in order you input them into program in python but not in most languages
#values do not need to be uniwue in python but keys do 
for player_name in players:
    print(f"{player_name} -> {players[player_name]}")


#You can have keys and values of any types 
#Notice this is the opposite mapping 
#that we had above. Additonally this is an example of a dictionary literal
jerseys: dict[int, str] = {15: "Brooks", 2: "Love", 5: "Bacot"} #shorthand for creating dictionary if you can write it this way
jerseys[23] = "Jordan" #inserts jordan into dictionary
print(jerseys)


#The pop method allows you to remove a key-value pair by its key. The 
#pop method returns the value associated with the popped key
popped_name: str = jersey.pop(23)
print(popped_name)
print(jerseys)