#
## Threadbare Game - Inventory
#
inventory = []

def check():
    inventory = inventory.sort()
    print inventory

def add(item):
    inventory.append(item)
    check()

def remove(item):
    inventory.remove()
    check()

add("panties")
add("lube")
add("DVD of Cool Runnings")

remove("panties")