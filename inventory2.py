def addToInventory(inventory, addedItems):
    global inv
    # print('Original Inventory: ' + str(inventory))
    # print('Original Items: ' + str(addedItems))
    for eachItem in addedItems:
        if eachItem in inventory:
            # print(eachItem + ': it\'s there')
            inv[eachItem] = inv.get(eachItem) + 1
            # print(str(inv))
        else:
            # print(eachItem + ': it\'s not there')
            inv.setdefault(eachItem,1)
            # print(str(inv))

def displayInventory(inventory):
    print("** Inventory: **")
    item_total = 0
    for k,v in inventory.items():
        item_total = item_total + v
        print(str(v) + ' ' + str(k))
    print("Total number of items: " + str(item_total))

inv = {'gold coin': 42, 'rope': 1}
# dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'emerald', 'gold bar', 'gold bar', 'sword', 'dagger', 'gold coin', 'emerald', 'sapphire', 'gold coin', 'gold bar', 'emerald']
addToInventory(inv, dragonLoot)
displayInventory(inv)