#Programmed by: Shaivi Sen
#Rollno.: 57
#List assignment no.: 7
#Ask a user for a fruit name. Check if it exists in your fruit_basket list using the in keyword.
fruit_basket=["Apple","Mango","Gauva","Grapes","Watermelon"]
ask=input("Enter a fruit name:")
if ask in fruit_basket:
    print("Present in the fruit basket")
else:
    print("Not present in the fruit basket")
    