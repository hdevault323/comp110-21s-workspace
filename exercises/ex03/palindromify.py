"""EX03 - palindromify function."""

__author__: str = "730236759"


def main() -> None:
    """Entrypoint of the program."""
    word: str = input("Enter first half of palindrome: ")
    print("This can be palindromed in an even or odd way.")
    print("Palindromes of odd length will flip around the middle letter, so that it is not repeated.")
    print("Palindromes of even length flip in between a repeated middle character.")
    even_odd: str = input("Is this an even(true) or odd(false) palindrome? ")
    if even_odd == "true":
        y = True
    else:
        y = False
    palindromify(word, y)
    print(palindromify(word, y))


def palindromify(x: str, y: bool) -> str:
    """This function returns the palindrome of a series of letters given."""
    if y:
        palindrome = list(x)
        palindrome.reverse()
        i = 0
        while i < len(palindrome):
            x += str(palindrome[i])
            i += 1
        return x    
    if not y:
        palindrome = list(x)
        palindrome.reverse()
        i = 1
        while i < len(palindrome):
            x += str(palindrome[i])
            i += 1
        return x  
    return x


if __name__ == "__main__":
    main()