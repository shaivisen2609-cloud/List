#Programmed by: Shaivi Sen
#Rollno.: 57
#Dictionary assignment no.:14
#Create a dictionary inventory = {'Pens': 10, 'Erasers': 5}. Ask the user which item they bought and decrease that item's count by 1
inventory = {'Pens': 10, 'Erasers': 5}
ask=input("Enter the name of item :")
for key,value in inventory.items():
    if key==ask:
        #value-=1
        inventory[key]=value-1
print(inventory)
