"""Fortune cookie exercise redux as a structured program."""

from random import randint

__author__ = "730236759"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print("Your fortune cookie says...")
    print((fortune_cookie()))
    print("Now, go spread positive vibes!")


def fortune_cookie() -> str:
    """Possible fortunes returned by fortune cookie"""
    cookie_input = int(randint(0, 100)) 
    if cookie_input < 25:
        return("Good fortunes are coming your way!")
    else: 
        if cookie_input < 50:
            return("You will have a fantastic day!")
        else: 
            if cookie_input < 75:
                return("You will have a long and happy life!")
            else: 
                if cookie_input <= 100:
                    return("Someone specail is coming into your life!")


# Python Idiom for "starting" the program when run as a module.
# The special dunder variable __name__ will be "__main__" when run as module. 
if __name__ == "__main__":
    main()
