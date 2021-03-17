"""
The Collatz Sequence

Write a function named collatz() that has one parameter named number.
If number is even, then collatz() should print number // 2 and return
this value.
If number is odd, then collatz() should print and return 3 * number + 1.

The write a program that lets the user type in an integer and that keeps
calling collatz() on that number until the function returns the value 1.
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

print('Enter a starting integer for the collatz sequence:')
user_number = int(input())
while True:
    user_number = collatz(user_number)
    print(user_number)
    if user_number == 1:
        break
