import math
from constants import *


def date_prompt():
    """
    Prompts the user to enter a month, year, and date.

    :return: A tuple of the entered month, date as an integer, and the year.
    """
    month = input('Enter a month: ')
    while month not in months:
        month = input('Enter a valid month: ')
    year = input('Enter a year greater than 1582: ')
    while float(year) < 1582:
        year = input('Enter a valid year: ')

    day = input('Enter a day: ')
    if month == "February" and float(year) % 4 != 0:
        while float(day) > 28:
            day = input('Enter a valid day: ')
    if month in days30:
        while float(day) > 30:
            day = input('Enter a valid day: ')
    if month in days31:
        while float(day) > 31:
            day = input('Enter a valid day: ')
    return month, int(day), year


def doomsday_calc(year):
    """
    Calculates the doomsday for a given year.

    :param year: The year parameter that the user entered.
    :return: An integer representing the doomsday for a given year.
    """
    ltd = year[2:]
    ftd = year[:2]
    mil = ftd + "00"
    if int(mil) % 400 == 0:
        coeff = 2
        d_ca = (coeff + int(ltd) + math.floor(int(ltd) / 4)) % 7
    elif int(mil) % 400 == 100:
        coeff = 0
        d_ca = (coeff + int(ltd) + math.floor(int(ltd) / 4)) % 7
    elif int(mil) % 400 == 200:
        coeff = 5
        d_ca = (coeff + int(ltd) + math.floor(int(ltd) / 4)) % 7
    elif int(mil) % 400 == 300:
        coeff = 3
        d_ca = (coeff + int(ltd) + math.floor(int(ltd) / 4)) % 7
    return d_ca


def doomsday_dec(d_cal, month, day, year, doo):
    """
    Function prints what day of the week of the entered day.

    :param d_cal: The calculated doomsday from the `doomsday_calc()` function.
    :param month: The month the user entered.
    :param day: The day the user entered.
    :param year: The year the user entered.
    :param doo: The doomsday for the given month.
    :return: This function returns nothing because it prints the output.
    """
    if d_cal == 0:
        while day < doo:
            doo -= 7
        daydiff = abs(doo - day)
        if daydiff == 0:
            print("{} {} {} was a Sunday".format(month, day, year))
        elif daydiff == 1:
            print("{} {} {} was a Monday".format(month, day, year))
        elif daydiff == 2:
            print("{} {} {} was a Tuesday".format(month, day, year))
        elif daydiff == 3:
            print("{} {} {} was a Wednesday".format(month, day, year))
        elif daydiff == 4:
            print("{} {} {} was a Thursday".format(month, day, year))
        elif daydiff == 5:
            print("{} {} {} was a Friday".format(month, day, year))
        elif daydiff == 6:
            print("{} {} {} was a Saturday".format(month, day, year))

    elif d_cal == 1:
        while doo > day:
            doo -= 7
        daydiff = abs(doo - day)
        if daydiff == 0:
            print("{} {} {} was a Monday".format(month, day, year))
        elif daydiff == 1:
            print("{} {} {} was a Tuesday".format(month, day, year))
        elif daydiff == 2:
            print("{} {} {} was a Wednesday".format(month, day, year))
        elif daydiff == 3:
            print("{} {} {} was a Thursday".format(month, day, year))
        elif daydiff == 4:
            print("{} {} {} was a Friday".format(month, day, year))
        elif daydiff == 5:
            print("{} {} {} was a Saturday".format(month, day, year))
        elif daydiff == 6:
            print("{} {} {} was a Sunday".format(month, day, year))

    elif d_cal == 2:
        while doo > day:
            doo -= 7
        daydiff = abs(doo - day)
        if daydiff == 0:
            print("{} {} {} was a Tuesday".format(month, day, year))
        elif daydiff == 1:
            print("{} {} {} was a Wednesday".format(month, day, year))
        elif daydiff == 2:
            print("{} {} {} was a Thursday".format(month, day, year))
        elif daydiff == 3:
            print("{} {} {} was a Friday".format(month, day, year))
        elif daydiff == 4:
            print("{} {} {} was a Saturday".format(month, day, year))
        elif daydiff == 5:
            print("{} {} {} was a Sunday".format(month, day, year))
        elif daydiff == 6:
            print("{} {} {} was a Monday".format(month, day, year))

    elif d_cal == 3:
        while doo > day:
            doo -= 7
        daydiff = abs(doo - day)
        if daydiff == 0:
            print("{} {} {} was a Wednesday".format(month, day, year))
        elif daydiff == 1:
            print("{} {} {} was a Thursday".format(month, day, year))
        elif daydiff == 2:
            print("{} {} {} was a Friday".format(month, day, year))
        elif daydiff == 3:
            print("{} {} {} was a Saturday".format(month, day, year))
        elif daydiff == 4:
            print("{} {} {} was a Sunday".format(month, day, year))
        elif daydiff == 5:
            print("{} {} {} was a Monday".format(month, day, year))
        elif daydiff == 6:
            print("{} {} {} was a Tuesday".format(month, day, year))

    elif d_cal == 4:
        while doo > day:
            doo -= 7
        daydiff = abs(doo - day)
        if daydiff == 0:
            print("{} {} {} was a Thursday".format(month, day, year))
        elif daydiff == 1:
            print("{} {} {} was a Friday".format(month, day, year))
        elif daydiff == 2:
            print("{} {} {} was a Saturday".format(month, day, year))
        elif daydiff == 3:
            print("{} {} {} was a Sunday".format(month, day, year))
        elif daydiff == 4:
            print("{} {} {} was a Monday".format(month, day, year))
        elif daydiff == 5:
            print("{} {} {} was a Tuesday".format(month, day, year))
        elif daydiff == 6:
            print("{} {} {} was a Wednesday".format(month, day, year))

    elif d_cal == 5:
        while doo > day:
            doo -= - 7
        daydiff = abs(doo - day)
        if daydiff == 0:
            print("{} {} {} was a Friday".format(month, day, year))
        elif daydiff == 1:
            print("{} {} {} was a Saturday".format(month, day, year))
        elif daydiff == 2:
            print("{} {} {} was a Sunday".format(month, day, year))
        elif daydiff == 3:
            print("{} {} {} was a Monday".format(month, day, year))
        elif daydiff == 4:
            print("{} {} {} was a Tuesday".format(month, day, year))
        elif daydiff == 5:
            print("{} {} {} was a Saturday".format(month, day, year))
        elif daydiff == 6:
            print("{} {} {} was a Sunday".format(month, day, year))

    else:
        while doo > day:
            doo -= 7
        daydiff = abs(doo - day)
        if daydiff == 0:
            print("{} {} {} was a Saturday".format(month, day, year))
        elif daydiff == 1:
            print("{} {} {} was a Sunday".format(month, day, year))
        elif daydiff == 2:
            print("{} {} {} was a Monday".format(month, day, year))
        elif daydiff == 3:
            print("{} {} {} was a Tuesday".format(month, day, year))
        elif daydiff == 4:
            print("{} {} {} was a Wednesday".format(month, day, year))
        elif daydiff == 5:
            print("{} {} {} was a Thursday".format(month, day, year))
        elif daydiff == 6:
            print("{} {} {} was a Friday".format(month, day, year))


def doomsday():
    user_m, user_d, user_y = date_prompt()
    confirm = input(f"You entered {user_d} {user_m} {user_y}. Is this correct (y/n)? ")
    while confirm.lower().startswith('n'):
        date_prompt()
        confirm = input(f"You entered {user_d} {user_m} {user_y}. Is this correct (y/n)? ")

    if int(user_y) % 400 == 0 and int(user_y) % 4 == 0:
        doomsday = doomsday_calc(user_y)
        doom = doomsday_LY[user_m]
        result = str(doomsday_dec(doomsday, user_m, user_d, user_y, doo=doom))
    elif int(user_y) % 4 == 0:
        doomsday = doomsday_calc(user_y)
        doom = doomsday_LY[user_m]
        result = str(doomsday_dec(doomsday, user_m, user_d, user_y, doo=doom))
    else:
        doomsday = doomsday_calc(user_y)
        doom = doomsday_NLY[user_m]
        statement = doomsday_dec(doomsday, user_m, user_d, user_y, doo=doom)
        result = str(statement)
    return result

if __name__ == "__main__":
    doomsday()