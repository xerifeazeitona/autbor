"""
Date Detection
Write a regular expression that detects dates in the DD/MM/YYYY format.
Assume that the days range from 01 to 31, the months range from 01 to 12,
and the years range from 1000 to 2999. Note that if the day or month is
a single digit, it’ll have a leading zero.
The regular expression doesn’t have to detect correct days for each
month or for leap years; it will accept nonexistent dates like
31/02/2020 or 31/04/2021.
Then store these strings into variables named month, day, and year, and
write additional code that can detect if it is a valid date.
"""

import re

date_regex = re.compile(r'((0|1|2|3)\d)/((0|1)\d)/((1|2)\d\d\d)')

def leap_year(year):
    """
    Returns 1 for leap years and 0 for non leap years.
    Leap years are every year evenly divisible by 4, except for years
    evenly divisible by 100, unless the year is also evenly divisible
    by 400.
    """
    if year % 4 == 0 and (year % 100 == 0 and year % 400 == 0):
        return 1
    return 0

def is_valid_date(date_string):
    """Evaluates if a date is valid"""
    mo = date_regex.search(date_string)
    if mo:
        day = int(mo.group(1))
        month = int(mo.group(3))
        year = int(mo.group(5))
        if month in [4, 6, 9, 11] and day <= 30:
            return True
        elif month == 2 and day <= 28 + leap_year(year):
            return True
        elif month in [1, 3, 5, 7, 8, 10, 12] and day <= 31:
            return True
    return False

test_dates = [
    '22/03/2021',
    '39/01/2018',
    '01/04/2020',
    '07/19/1999',
    '31/04/1990',
    '29/02/2021',
    '29/02/2000',
    '29/02/1900'
    ]

print('\nTesting dates...\n')
for date in test_dates:
    if is_valid_date(date):
        print(f'{date} is a valid date')
    else:
        print(f'{date} is invalid')
print('\n...done!')
