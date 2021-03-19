"""
List to Dictionary Function for Fantasy Game Inventory

Imagine that a vanquished dragon’s loot is represented as a list of
strings like this:

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

Write a function named addToInventory(inventory, addedItems), where
the inventory parameter is a dictionary representing the player’s
inventory (like in the previous project) and the addedItems parameter
is a list like dragonLoot.
The addToInventory() function should return a dictionary that represents
the updated inventory.
Note that the addedItems list can contain multiples of the same item.
"""

def display_inventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(f"{v} {k}")
        item_total += v
    print(f"Total number of items:  {item_total}")

def add_to_inventory(inventory, addedItems):
    for item in addedItems:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = add_to_inventory(inv, dragon_loot)
display_inventory(inv)
