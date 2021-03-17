"""
Input Validation

Add try and except statements to the previous project to detect whether
the user types in a noninteger string. Normally, the int() function will
raise a ValueError error if it is passed a noninteger string. In the
except clause, print a message to the user saying they must enter an
integer.
"""

def collatz(number):
    """
    Returns
     - number // 2 if number is even
     - 3 * number + 1 if number is odd
    """
    if number % 2 == 0:
        return number // 2
    return 3 * number + 1

# Input validation
while True:
    print('Enter a starting integer for the collatz sequence:')
    try:
        user_number = int(input())
    except ValueError:
        print("We're not going anywhere until you enter an integer!!")
        continue
    break

# Collatz sequence
while True:
    user_number = collatz(user_number)
    print(user_number)
    if user_number == 1:
        break
