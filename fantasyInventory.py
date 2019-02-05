#Use dictionaries and lists to model a basic RPG inventory

stuff ={'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

dragonLoot =['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

#prints inventory and calculates total number of items
def displayInventory(inventory):
    print('Inventory:')

    item_total = 0

    for k, v in inventory.items():
        print(str(v) + ' ' + str(k))
        item_total += v

    print('Total number of items: ' + str(item_total))


#adds list of items to an inventory dictionary
def addToInventory(inventory, addedItems):
    for i in addedItems:
        if i in inventory.keys():
            inventory[i] += 1
        else:
            inventory.setdefault(i, 1)


addToInventory(stuff, dragonLoot)
displayInventory(stuff)
