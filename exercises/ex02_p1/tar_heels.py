"""Tar Heels exercise redux as a structured program."""

__author__ = "730236759"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    choice: int = int(input("Enter an int: "))
    print(tar_heels(choice))


def tar_heels(choice: int) -> str: 
    """Solving Tar Heel Arithmetic Puzzle."""
    if int(choice) % 2 == 0 and int(choice) % 7 == 0:
        return("TAR HEELS")
    else: 
        if int(choice) % 2 == 0:
            return("TAR")
        else: 
            if int(choice) % 7 == 0: 
                return("HEELS")
            return("CAROLINA")


if __name__ == "__main__":
    main()
