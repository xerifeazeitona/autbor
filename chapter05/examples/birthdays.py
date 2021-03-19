birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True:
    prompt = 'Enter a name: (blank to quit) '
    name = input(prompt)
    if name == '':
        break
    if name in birthdays:
        print(f'{birthdays[name]} is the birthday of {name}')
    else:
        print(f'I do not have birthday information for {name}')
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated.')
