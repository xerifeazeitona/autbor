"""
Sandwich Maker
Write a program that asks users for their sandwich preferences.
The program should use PyInputPlus to ensure that they enter valid
input, such as:
- Using inputMenu() for a bread type: wheat, white, or sourdough.
- Using inputMenu() for a protein type: chicken, turkey, ham, or tofu.
- Using inputYesNo() to ask if they want cheese.
- If so, using inputMenu() to ask for a cheese type: cheddar, Swiss, or
    mozzarella.
- Using inputYesNo() to ask if they want mayo, mustard, lettuce, or
    tomato.
- Using inputInt() to ask how many sandwiches they want. Make sure this
    number is 1 or more.

Come up with prices for each of these options, and have your program
display a total cost after the user enters their selection.
"""

import pyinputplus as pyip


def list_stringinator(list_argument):
    """
    Returns a string with all the items separated by a comma and a
    space with 'and' inserted before the last item
    """
    return_string = ''
    for item in list_argument:
        # First item doesn't get anything
        if list_argument.index(item) == 0:
            return_string = item
        # Last item gets a ' and '
        elif list_argument.index(item) == (len(list_argument) - 1):
            return_string = return_string + ' and ' + item
        # All other items get a ', '
        else:
            return_string = return_string + ', ' + item

    return return_string


bread = {'wheat': 1, 'white': 2, 'sourdough': 3}
protein = {'chicken': 1, 'turkey': 2, 'ham': 3, 'tofu': 4}
cheese = {'no cheese': 0, 'cheddar': 1, 'swiss': 2, 'mozzarella': 3}
extras = {'mayo': 1, 'mustard': 2, 'lettuce': 3, 'tomato': 4}

print('\nWelcome to our restaurant!')
# Bread selection
customer_bread = pyip.inputMenu(
    list(bread.keys()), '\nWhat kind of BREAD would you like?\n')
print(f'{customer_bread.title()} bread selected.')
# Protein selection
customer_protein = pyip.inputMenu(
    list(protein.keys()), '\nWhat kind of PROTEIN would you like?\n')
print(f'{customer_protein.title()} protein selected.')
# Cheese selection
customer_cheese = 'no cheese'
if pyip.inputYesNo('\nWould you like to add cheese? (y/n) ') == 'yes':
    customer_cheese = pyip.inputMenu(
        list(cheese.keys())[1:], '\nWhat kind of CHEESE would you like?\n')
    print(f'{customer_cheese.title()} cheese selected.')
# Extras selection
customer_extras = []
for key in extras.keys():
    if pyip.inputYesNo(f'\nWould you like to add {key}? (y/n) ') == 'yes':
        customer_extras.append(key)
        print(f'{key} added.')
# How many sandwiches?
quantity = pyip.inputInt(
    '\nHow many sandwiches would you like (min 1)?: ', min=1)
# Display order
order = '\n'
if quantity > 1:
    order += f'{quantity} {customer_protein} sandwiches'
else:
    order += f'{quantity} {customer_protein} sandwich'
order += f' on a {customer_bread} bread with {customer_cheese}'
if customer_extras:
    order += f', {list_stringinator(customer_extras)}'
order += ' coming right up!\n'
print(order)
# Calculate total cost
print('Calculating total...')
total = 0
total += bread[customer_bread]
total += protein[customer_protein]
total += cheese[customer_cheese]
if customer_extras:
    for customer_extra in customer_extras:
        total += extras[customer_extra]
total *= quantity

print(f"\nThat will be ${format(total, '.2f')} moneys please.")
