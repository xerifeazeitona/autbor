"""
While examples
"""
# basic while
spam = 0
while spam < 5:
    print('Hello, world!')
    spam += 1

# break statement
while True:
    print('\nPlease type your name.')
    name = input()
    if name == 'your name':
        break
print('Thank you!')

# continue statement
while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe. What is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted.')
