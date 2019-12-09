# Items that exist in each room and the functions you can use to interact with them
#TODO Define items in each room
inventory=[]
room1items = []
room2items = []
room3items = ['lantern']
room4items = []
room5items = ['sword']
room6items = []
room7items = []
room8items = []
room9items = []
room10items = []
room11items = []
room12items =['gold ring']
allItems = [room1items, room2items, room3items, room4items, room5items, room6items,room7items,room8items,room9items,room10items,room11items, room12items]

# Returns item to be added to inventory if it exists in this room and removes it from the list of items in the coom
def pick_up(itemName, roomNum):
    if itemName in allItems[roomNum-1]:
        allItems[roomNum-1].remove(itemName)
        inventory.append(itemName)
        print('{} added to inventory!'.format(itemName))
        return itemName
    else:
        print("---------------------------------------------------------")
        print("Not a valid item to pick up")
        return -1

# Puts the item down in the current room, adds it to the item list of the current room, 
# and returns 0 to indicate that it was successfully removed.
def put_down(itemName, roomNum):
    print("You put down the ", itemName)
    allItems[roomNum-1].append(itemName)
    return 0

def useItem(itemName, inventory):
    found=False
    if itemName in inventory:
        found = True
    return found

