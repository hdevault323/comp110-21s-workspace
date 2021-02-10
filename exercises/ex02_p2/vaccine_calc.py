"""Vaccine calculator exercise as a structured program."""

from datetime import datetime, timedelta

__author__ = "730236759"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    population: int = int(input("Population: "))
    doses: int = int(input("Doses administered: "))
    doses_per_day: int = int(input("Doses per day: "))
    target: int = int(input("Target percent vaccinated: "))
    number_days: int = days_to_target(population, doses, doses_per_day, target)
    completion_date: str = future_date(int(number_days))
    print("We will reach " + str(target) + "% vaccination in " + str(number_days) + ", ")
    print("which falls on " + completion_date)


def days_to_target(population: int, doses: int, doses_per_day: int, target: int) -> int: 
    """The number of days until the target population is vaccinated."""
    population_vaccinated = round((int(doses)) / 2)
    target_population = round((float(int(target)) / 100) * float(int(population)))
    target_population_remaining = int(target_population) - (int(population_vaccinated))
    return round(((int(target_population_remaining)) * 2) / (int(doses_per_day)))     


def future_date(number_days: int) -> str:
    """Returns prijected date vaccination goal will be reached."""
    today: datetime = datetime.today()
    future: timedelta = timedelta(int(number_days))
    date_completed: datetime = today + future
    return date_completed.strftime("%B %d, %Y")


if __name__ == "__main__":
    main()