"""EX03 - prime functions."""

__author__: str = "730236759"


primes_list: list[int]


def main() -> None:
    """Entrypoint of the program."""
    prime_number: int = int(input("Choose a number: "))
    is_prime(prime_number)
    print(is_prime(prime_number))
    low_range: int = int(input("Enter low number in range: "))
    high_range: int = int(input("Enter high number in range: "))
    list_primes(low_range, high_range)
    print(list_primes(low_range, high_range))


def is_prime(x: int) -> bool:
    """This function returns a "True" bool if the argument is prime."""
    if x <= 1:
        return False
    else: 
        if x == 2 or x == 3 or x == 5:
            return True 
        else:
            if x % 2 == 0 or x % 3 == 0 or x % 5 == 0:
                return False
            else: 
                for i in range(2, (x + 1), 1):
                    if (x % i) == 0 and (x != i):
                        return False
    return True


def list_primes(a: int, y: int) -> list[int]:
    """This function returns a list of all prime numbers within a range."""
    chosen_range: range = range(a, y, 1)
    primes_list = []
    i = 0
    while i < (len(chosen_range)):
        if is_prime(chosen_range[i]):
            primes_list.append(chosen_range[i])
        i += 1
    return primes_list


if __name__ == "__main__":
    main()