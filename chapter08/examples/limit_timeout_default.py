import pyinputplus as pyip

response = pyip.inputNum('Enter num (2 chances): ', limit=2)
response = pyip.inputNum('Enter num (you have 5s): ', timeout=4)
response = pyip.inputNum('Enter num (2 chances, defaults to N/A): ',
limit=2, default='N/A')
