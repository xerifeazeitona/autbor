import pyinputplus as pyip

response = pyip.inputNum('Enter num (min 4): ', min=4)
response = pyip.inputNum('Enter num (greater than 4): ', greaterThan=4)
response = pyip.inputNum('Enter num (between 4 and 6): ', min=4, lessThan=6)
