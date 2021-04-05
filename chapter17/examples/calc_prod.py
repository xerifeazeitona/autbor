"""
Epoch timestamps can be used to profile code, that is, measure how long
a piece of code takes to run. If you call time.time() at the beginning
of the code block you want to measure and again at the end, you can
subtract the first timestamp from the second to find the elapsed time
between those two calls.
"""
import time

def calc_prod():
    """Calculate the product of the first 100,000 numbers."""
    product = 1
    for i in range(1, 100000):
        product *= i
    return product

start_time = time.time()
prod = calc_prod()
end_time = time.time()
print(f'The result is {len(str(prod))} digits long.')
print(f'Took {round(end_time - start_time, 2)} seconds to calculate.')
