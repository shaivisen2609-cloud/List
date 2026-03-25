#Programmed by: Shaivi Sen
#Rollno.: 57
#Dictionary assignment no.:21
'''"A small shop sells 5 items. You need to create a program that acts as a POS (Point of Sale) system.
Tasks:
The Database: Create a dictionary called menu where keys are item names (e.g., ""Samosa"", ""Tea"", ""Coffee"") and values are their prices.
The Shopping List: Create an empty list called cart.
The Input Loop: Use a while loop to ask the user to type an item name to add to their cart. Type ""done"" to stop.
Validation: If the user types an item not in the menu, print ""Item not available.""
The Bill: After ""done"" is typed, loop through the cart list. For each item, look up its price in the menu dictionary and calculate the total sum.
Final Output: Print a ""Receipt"" showing the items bought and the final total price."'''
menu={"Samosa":30,"Tea":20,"Coffee":80,"Pizza":150,"Momo":40}
print("Menu:",menu)
cart=[]
bill=0
while True:
    ask=input("Enter item name:")
    if ask in menu:
        cart.append(ask)
    elif ask=="done":
        break
    else:
        print("Item is not available")
print("Cart:",cart)
print("Receipt:")
for key,value in menu.items():
    if key in cart:
        bill+=value
        print(key,"-",value)
print("Total:",bill)
