"""Pet care CYOA."""

from random import randint

__author__ = "730236759"

POINTS_INCREASE: int = 10 
POINTS_DECREASE: int = 5
CHOCOLATE_EMOJI: str = "\U0001F36B"
BEEF_EMOJI: str = "\U0001F969"
CHICKEN_EMOJI: str = "\U0001F357"
PORK_EMOJI: str = "\U0001F953"
HAPPY_EMOJI: str = "\U0001F604"
SAD_EMOJI: str = "\U0001F622"
PARTY_EMOJI: str = "\U0001F973"


player: str
points: int
pet_name: str
rand_food: int


def main() -> None: 
    """Main function of program."""
    greet()
    global points 
    points = int(0)
    while input("Would you like to continue caring for your dog? yes/no - ") == "yes":
        print("Great!") 
        user_input = int(input("Would you like to feed (1), walk (2), play with your dog (3)? "))
        if user_input == 1:
            feed()
            print(f"Great job {player}! your current happiness score after feeding {pet_name} is {points}")
        else:
            if user_input == 2:
                walk()
                print(f"Great job {player}! your current happiness score after the walk is {points}")
            else:
                if user_input == 3:
                    play()
                    print(f"Your current happiness score is {points}")
    print(f"Your final score is {points}!")
    print(f"Good job taking care of {pet_name}!")
    print(f"Come visit {pet_name} again!")
    print(f"Goodbye, {player}!")

    
def greet() -> None:
    """Greets and welcomes player and asks for their name."""
    print("Welcome to the pet simulator! What is your name?")
    global player
    player = str(input(""))
    print(f"Welcome {player}!")
    global pet_name
    pet_name = str(input("What would you like your pet's name to be? "))
    print(f"In this simulator, you will be able to choose how you take care of your dog {pet_name}.")
    print(f"When you interact with {pet_name} in ways they like you will gain 10 happiness points!")
    print(f"When you interact with {pet_name} in ways they do not like, you will lose 5 happiness points!")
    print("In some cases, you may lose more or less points. This will be stated.")
    print("The goal is to get as many happy points as possible.")
    print("You lose the game if your happiness score is below zero when you say you are done.")
    print(f"Now go take care of and have fun with {pet_name}")


def feed() -> None:
    """Determines points for feeding."""
    print(f"Good idea! {pet_name} was really hungry!")
    global rand_food 
    rand_food = randint(0, 90)
    food_type: str = pet_food(int(rand_food))
    global points
    if food_type != (f"Chocolate {CHOCOLATE_EMOJI}"):
        print(f"You went to the pet store looking for pet food. The only flavor they had was {food_type}")
        print(f"Luckily, {pet_name} likes {food_type}!")
        print(f"{pet_name}'s happiness score has increased {HAPPY_EMOJI}")
        points += POINTS_INCREASE
        print(f"Now {pet_name}'s happiness is {points}")
    else: 
        print(f"Oh no! Dogs cant have {food_type}!")
        print(f"{pet_name}'s happiness score has decreased {SAD_EMOJI}")
        points -= POINTS_DECREASE
        print(f"Now {pet_name}'s happiness is {points}")
    

def pet_food(x: int) -> str:
    """Food decided on."""
    global rand_food 
    if int(rand_food) < 25:
        return f"Chicken {CHICKEN_EMOJI}"
    else:
        if int(rand_food) < 50:
            return f"Beef {BEEF_EMOJI}"
        else: 
            if int(rand_food) < 75:
                return f"Pork {PORK_EMOJI}"
            return f"Chocolate {CHOCOLATE_EMOJI}"


def walk() -> None:
    """Walk location choices."""
    print(f"Great choice {player}! {pet_name} is so excited to go for a walk!")
    print(f"This instantly increases {pet_name}'s happiness score by 3!")
    global points
    points += 3
    print(f"Your current happiness score is {points}")
    print(f"Now, decide where to take {pet_name}.")
    location: int = int(input("Choose the lake (1), the park (2), or around the neighborhood (3) - "))
    if int(location) == 1:
        lake()
    else: 
        if int(location) == 2:
            park()
        else: 
            if int(location) == 3:
                neighborhood()

        
def lake() -> None: 
    """Lake walke paths."""
    global points 
    print(f"Great choice {player}, {pet_name} loves the lake!")
    print("There are two paths around the lake.")
    print("To the left, there is a 3 mile loop through the woods")
    print("To the right, there is a shorter 1.5 mile scenic route by the lake")
    path: str = str(input("Do you want to walk to the left or right around the lake? "))
    print(f"Good choice {player}! This is a beautiful route!")
    print(f"{pet_name}'s happiness score increased {HAPPY_EMOJI}.")
    points += POINTS_INCREASE
    print(f"Now {pet_name}'s happiness is {points}")
    if path == "right":
        water()
        x: int = int(randint(10, 100))
        geese(x) 
        print(f"Wow {player}! that was a nice walk!")
        print(f"Overall, {pet_name} had fun! Their happiness score increased by 20 this time {HAPPY_EMOJI}!")
        points += 2 * POINTS_INCREASE
        print(f"Now {pet_name}'s happiness is {points}")
    else: 
        if path == "left":
            dog_friend()
            print(f"Wow {player}! that was a nice walk!")
            print(f"Overall, {pet_name} had fun! Their happiness score increased by 20 this time {HAPPY_EMOJI}!")
            points += 2 * POINTS_INCREASE
            print(f"Now {pet_name}'s happiness is {points}")

    
def geese(x: int) -> None:
    """Geese encounter."""
    global points
    number_geese: int = x // 10
    print(f"There is now a flock of {number_geese} geese in the path. {pet_name} wants to chase them. What do you do?")
    geese = int(input(f"turn around (1), let {pet_name} chase them (2), walk by the geese with {pet_name} (3): "))
    if geese == 1: 
        print(f"{pet_name} is sad the walk ended early over your fear of geese!")
        print(f"{pet_name}'s happiness score has decreased {SAD_EMOJI}")
        points -= POINTS_DECREASE
        print(f"Now {pet_name}'s happiness is {points}")
    else:
        if geese == 2:
            outcome: int = randint(0, 100)
            if outcome > 50:
                print(f"Uh oh {player} they flew right towards you! You are okay and had a good laugh but...")
                print(f"You decided to turn around so {pet_name}'s happiness score has decreased {SAD_EMOJI}")
                points -= POINTS_DECREASE
                print(f"Now {pet_name}'s happiness is {points}")
            else: 
                print(f"Aw look {player}, {pet_name} is so happy chasing the geese!")
                print("and the geese are okay!")
                points += POINTS_INCREASE
                print(f"Great choice {player}, {pet_name}'s happiness increased {HAPPY_EMOJI}")
                print(f"Now {pet_name}'s happiness is {points}")
        else: 
            print(f"Oh good {player}!")
            print("You passed the geese with no issue and the rest of your walk will be fun and relaxing!")
            print(f"There was no increase or decrease in {pet_name}'s happiness.")
            print(f"Now {pet_name}'s happiness is {points}")


def water() -> None:
    """Swimming on walk."""
    global points
    print(f"{pet_name} sees the water.")
    swim: str = str(input(f"Can {pet_name} swim? yes/no - "))
    if swim == "yes":
        while input(f"Do you want to throw a stick into the water for {pet_name}? yes/no - ") == "yes":
            print(f"Yay! {pet_name} is so excited! {PARTY_EMOJI}")
            print(f"Their happiness score increased {HAPPY_EMOJI}!")
            points += POINTS_INCREASE
            print(f"Now {pet_name}'s happiness is {points}")
        while input(f"{pet_name} wants to splash in the water now! Is that okay? yes/no - ") == "yes":
            print(f"Look at how happy {pet_name} is!")
            print(f"{pet_name}'s happiness score increased {HAPPY_EMOJI}!")
            points += POINTS_INCREASE 
            print(f"Now {pet_name}'s happiness is {points}")
        print(f"Thanks {player}! {pet_name} had a great time in the water!")
    else: 
        if swim == "no": 
            print(f"Thats okay {player}, you and {pet_name} can still have fun! ")
            print(f"But, {pet_name}'s happiness score still decreased {SAD_EMOJI}")
            points -= POINTS_DECREASE
            print(f"Now {pet_name}'s happiness is {points}")


def dog_friend() -> None:
    """Meet dog friend on walk."""
    global points
    print(f"Oh look! It's {pet_name}'s friend Lucy!")
    print(f"Can {pet_name} play with Lucy?")
    print(f"No, there's no time {SAD_EMOJI}; or of course! Its good to catch up with Lucy's owner {HAPPY_EMOJI}")
    choice_friend: str = str(input("yes/no - "))
    if choice_friend == "yes":
        print(f"Awesome! {pet_name} is having so much fun!")
        print(f"Their happiness score increased by 20 {HAPPY_EMOJI}!")
        points += (POINTS_INCREASE * 2)
        print(f"Now {pet_name}'s happiness is {points}")
    if choice_friend == "no":
        print(f"{pet_name} walked away with their tail between their legs.")
        print(f"{pet_name} is so sad that their happiness score decreased by 15 {SAD_EMOJI}")
        points -= POINTS_DECREASE * 3
        print(f"Now {pet_name}'s happiness is {points}")


def park() -> None: 
    """Walk in park."""
    print(f"Great choice {player}, {pet_name} loves the park!")
    print(f"{player}, what distance (in miles) would you like to walk with {pet_name}?")
    distance: float = float(input("Enter number from 0.1 - 5.0: "))
    fetch(distance)
    print(f"Wow! {pet_name} had lots of fun at the park! Time to head back to the car!")


def fetch(x: float) -> None: 
    """Play fetch with dog."""
    global points
    halfway = float(x / 2) 
    print(f"At {halfway} miles, there is an open field on your walk and {pet_name} wants you to play fetch.")
    print("To play fetch, type \"yes\" after the question \"Throw?\" until you're done throwing.")
    print("Type \"done\" to stop throwing.")
    while input("Throw? ") == "yes": 
        distance = randint(0, 50)
        if distance <= 5:
            print(f"Oops. You only threw it {distance} feet. {pet_name} was disappointed.")
            print(f"{pet_name}'s happiness decreased by {distance} {SAD_EMOJI}")
            points -= int(distance)
            print(f"Now {pet_name}'s happiness is {points}")
        else:
            if distance >= 5 and distance <= 45:
                print(f"Nice! You threw it {distance} feet and {pet_name} is having fun.")
                print(f"Your score increased by the amount of feet you threw {HAPPY_EMOJI}!")
                points += int(distance)
                print(f"Now {pet_name}'s happiness is {points}")
            else:
                if distance <= 50:
                    print(f"Wow {player}! That throw was really impressive! You threw {distance} feet!")
                    print(f"{pet_name} really had fun fetching that one!")
                    print(f"Your score increased by the amount of feet you threw times 1.5 {HAPPY_EMOJI}!")
                    points += int(distance * 1.5)
                    print(f"Now {pet_name}'s happiness is {points}")


def neighborhood() -> None: 
    """Choices in neighborhood."""
    print(f"Great choice {player}! {pet_name} loves walking through the neighborhood!")
    distance = float(input(f"How far will you walk {pet_name} through your neighborhood today (in miles)? "))
    print(f"Great {player}! {pet_name} is excited! Put their leash on and head out!")
    tennis_ball(distance)
    chase()


def tennis_ball(x: float) -> None:
    """Tennis ball found and reward."""
    global points
    found_ball = float(x / 3)
    print(f"At {found_ball} miles, {pet_name} found a tennis ball. Do you let them keep it? ")
    if input("yes/no - ") == "yes":
        print(f"Look at how happy {pet_name} is!")
        print(f"Their happiness score increased {HAPPY_EMOJI}!")
        points += POINTS_INCREASE 
        if input("What color is the ball? ") != "green":
            print(f"Wow {player}! This ball must be special since its not green!")
            print(f"{pet_name} is extra happy with their new ball!")
            print(f"Their happiness score increased again {HAPPY_EMOJI}!")
            points += POINTS_INCREASE 
            print(f"Now {pet_name}'s happiness is {points}")
        else: 
            print("Since its just a green tennis ball, there is no further increase or decrease in points")
    else: 
        print(f"{pet_name} had too many toys anyways.")
        print(f"But, {pet_name}'s happiness score still decreased {SAD_EMOJI}")
        points -= POINTS_DECREASE
        print(f"Now {pet_name}'s happiness is {points}")
        

def chase() -> None:
    """What the pet starts to chase."""
    global points
    chase_object = ["car", "squirrel", "biker", "dog"]
    print(f"{pet_name} took off after a {chase_object[randint(0,3)]}.")
    if input("Do you chase after them? yes/no - ") == "yes":
        print(f"Good job {player} you got {pet_name} back.")
        print(f"But, {pet_name}'s happiness score still decreased {SAD_EMOJI} because {pet_name} was mad at you")
        points -= POINTS_DECREASE
    else: 
        print(f"All is well, but {pet_name} could have gotten lost.")
        print(f"Since {pet_name} loved the chase, and did not get lost,")
        print(f"their happiness score increased again {HAPPY_EMOJI}!")
        print(f"But next time, you shuold chase {pet_name}")
        points += POINTS_INCREASE 


def play() -> None:
    """The choice how to play with pet."""
    print(f"Great choice! {pet_name} loves playing!")
    while input("You ready to play? yes/no - ") == "yes":
        print(f"What would you like to do with {pet_name}, {player}?")
        activity: int = int(input("tug of war (1) or frisbee (2)? "))
        if activity == 1:
            tug_of_war()
        else: 
            if activity == 2:
                frisbee()


def tug_of_war() -> None:
    """Play Tug of war with pet."""
    global points
    print(f"Okay! get ready to pull, {player}!")
    war = int(input("Choose a number between 0 and 1000: "))
    if war % 2 == 0:
        print(f"{pet_name} won!")
        print(f"{pet_name}'s happiness score increased {HAPPY_EMOJI}!")
        points += POINTS_INCREASE 
        print(f"Now {pet_name}'s happiness is {points}")
    else:
        if war % 5 == 0:
            print(f"{player}, you won!")
            print(f"{pet_name}'s happiness score has decreased {SAD_EMOJI}. They wanted to win.")
            points -= POINTS_DECREASE
            print(f"Now {pet_name}'s happiness is {points}")
        else: 
            if war % 5 != 0 and war % 2 != 0:
                print(f"{player}, you and {pet_name} tied!")
                print("There was no increase or decrease in the score.")


def frisbee() -> None:
    """Throw frisbee."""
    global points
    print(f"{pet_name} is excited!")
    while input("Throw? yes/no- ") == "yes": 
        distance = int(randint(0, 50))
        if distance <= 5:
            print(f"Oops. You only threw it {distance} feet. {pet_name} was disappointed.")
            print(f"{pet_name}'s happiness decreased {SAD_EMOJI}.")
            points -= POINTS_DECREASE
            print(f"Now {pet_name}'s happiness is {points}")
        else:
            if distance >= 5 and distance <= 45:
                print(f"Nice! You threw it {distance} feet and {pet_name} is having fun.")
                print(f"{pet_name}'s happiness increased {HAPPY_EMOJI}!")
                points += POINTS_INCREASE
                print(f"Now {pet_name}'s happiness is {points}")
            else:
                if distance <= 50:
                    print(f"Wow {player}! That throw was really impressive! You threw {distance} feet!")
                    print(f"{pet_name} really had fun fetching that one!")
                    print(f"{pet_name}'s happiness increased {HAPPY_EMOJI}!")
                    points += POINTS_DECREASE
                    print(f"Now {pet_name}'s happiness is {points}")


if __name__ == "__main__":
    main()