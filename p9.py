#Programmed by: Shaivi Sen
#Rollno.: 57
#List assignment no.: 9
#Write a program that takes a list of names and a "search_name" from the user. 
# Print the index where the name is found, or "Not Found."
name=["Radha","Sandhya","Priya","Jiya","Neha"]
user=input("Enter a name:")
if user in name:
    print("Found",name.index(user))
else:
    print("Not found")
