import pdb

groceryList = []

print("""
--------- GROCERY LIST ---------
------- [a] Add New Items ------
------- [b] Delete an Item ------
------- [c] Show Items ---------
------- [d] Exit ---------------
  """)

def showList():
  print(", ".join(groceryList))

def addGroceries(groceryToAdd):
  groceryList.append(groceryToAdd)
  showList()

def task():

  groceryItem = input("What would you like to do? ")

  if groceryItem == "b":
    showList()
    itemToDelete = input("What do you want to remove? ")
    groceryList.remove(itemToDelete)
    showList()
    task()
  if groceryItem == "c":
    showList()
    task()
  if groceryItem == "d":
    print("Things to get at the groery store are " + ", ".join(groceryList))
    exit()
  if groceryItem == "a":
    grocery_to_add = input("What would you like to add? ")
    addGroceries(grocery_to_add)
    task()

task()
