import pprint
message = 'It was a bright cold day in April,' \
    ' and the clocks were striking thirteen.'
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] += 1

# Both lines below are equivalent
#pprint.pprint(count)
print(pprint.pformat(count))
