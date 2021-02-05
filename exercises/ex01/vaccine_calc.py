"""A vaccination calculator."""

__author__ = "730236759"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...
population: int = input("Enter population: ")
doses_administered: int = input ("Enter number of doses administered: ")
doses_per_day: int = input ("Enter number of doses administered per day: ")
target_percent_vaccinated: int= input("Enter the target percent vaccinated as an integer out of 100: ")
population_vaccinated = round((int(doses_administered))/2)
target_population = round(((float(int(target_percent_vaccinated))/100)*float(int(population)))-(int(population_vaccinated)))
number_days_until_target = int(((int(target_population))*2) / (int(doses_per_day))) 

today: datetime = datetime.today()
future: timedelta = timedelta(int(number_days_until_target))
target_date: datetime = today + future

print("We will reach " + str(int(target_percent_vaccinated)) + "% vaccinated in " + str(int(number_days_until_target)) + " days which falls on " + target_date.strftime("%B %d, %Y"))
