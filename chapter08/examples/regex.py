import pyinputplus as pyip

response = pyip.inputNum(
    'Enter num (roman allowed): ', allowRegexes=[r'(I|V|X|L|C|D|M)+', r'zero'])

response = pyip.inputNum(
    'Enter an odd number: ', blockRegexes=[r'[02468]$'])

response = pyip.inputStr(
    "Enter a string ('cat' not allowed): ",
    allowRegexes=[r'caterpillar', r'category'], blockRegexes=[r'cat'])
    