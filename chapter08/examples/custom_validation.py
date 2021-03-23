import pyinputplus as pyip

def adds_up_to_ten(numbers):
    numbers_list = list(numbers)
    for i, digit in enumerate(numbers_list):
        numbers_list[i] = int(digit)
    if sum(numbers_list) != 10:
        raise Exception(
    f'The digits must add up to 10, not {sum(numbers_list)}.')
    return int(numbers) # return an int form of numbers

response = pyip.inputCustom(
    adds_up_to_ten, # No parentheses after adds_up_to_ten here
    'Enter any sequence of numbers that add up to 10 to get out: ')
