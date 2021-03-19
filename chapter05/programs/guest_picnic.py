allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
			 'Bob': {'ham sandwiches': 3, 'apples': 2},
			 'Carol': {'cups': 3, 'apple pies': 1}}

def total_brought(guests, item):
    num_brought = 0
    for value in guests.values():
        num_brought += value.get(item, 0)
    return num_brought

print('Number of things being brought:')
print(f" - Apples         {total_brought(allGuests, 'apples')}")
print(f" - Cups           {total_brought(allGuests, 'cups')}")
print(f" - Cakes          {total_brought(allGuests, 'cakes')}")
print(f" - Ham Sandwiches {total_brought(allGuests, 'ham sandwiches')}")
print(f" - Apple Pies     {total_brought(allGuests, 'apple pies')}")
