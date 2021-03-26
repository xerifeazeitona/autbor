"""
An assertion is a sanity check to make sure your code isn’t doing 
something obviously wrong.
"""
ages = [26, 57, 92, 54, 22, 15, 17, 80, 47, 73]
ages.sort()

assert ages[0] <= ages[-1] # Assert that the first age is <= the last age

ages.reverse()
assert ages[0] <= ages[-1] # this one raises an AssertionError
