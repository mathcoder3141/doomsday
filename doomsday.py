import math
from constants import *


def date_prompt():
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
    if d_cal == 0:
        print("Doomsday for {} {} was a Sunday".format(month, year))
        while day < doo:
            print("{} is a Sunday".format(doo))
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
        print("Doomsday for {} {} was a Monday".format(month, year))
        while doo > day:
            print("{} is a Monday".format(doo))
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
        print("Doomsday for {} {} was a Tuesday".format(month, year))
        while doo > day:
            print("{} is a Tuesday".format(doo))
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
        print("Doomsday for {} {} was a Wednesday".format(month, year))
        while doo > day:
            print("{} is a Wednesday".format(doo))
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
        print("Doomsday for {} {} was a Thursday".format(month, year))
        while doo > day:
            print("{} is a Thursday".format(doo))
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
        print("Doomsday for {} {} was a Friday".format(month, year))
        while doo > day:
            print("{} is a Friday".format(doo))
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
        print("Doomsday for {} {} was a Saturday".format(month, year))
        while doo > day:
            print("{} is also a Saturday".format(doo))
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


user_m, user_d, user_y = date_prompt()
confirm = input(f"You entered {user_d} {user_m} {user_y}. Is this correct (y/n)? ")
while confirm.lower().startswith('n'):
    date_prompt()
    confirm = input(f"You entered {user_d} {user_m} {user_y}. Is this correct (y/n)? ")

if int(user_y) % 400 == 0 and int(user_y) % 4 == 0:
    doomsday = doomsday_calc(user_y)
    doom = doomsday_LY[user_m]
    doomsday_dec(doomsday, user_m, user_d, user_y, doo=doom)
elif int(user_y) % 4 == 0:
    doomsday = doomsday_calc(user_y)
    doom = doomsday_LY[user_m]
    doomsday_dec(doomsday, user_m, user_d, user_y, doo=doom)
else:
    doomsday = doomsday_calc(user_y)
    doom = doomsday_NLY[user_m]
    doomsday_dec(doomsday, user_m, user_d, user_y, doo=doom)
