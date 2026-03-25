#Programmed by: Shaivi Sen
#Rollno.: 57
#Dictionary assignment no.:16
#Allow a user to input a name and a phone number via input() and store it in a dictionary until they type "exit".
store={}
while True:
    name=input("Enter your name:")
    if name=="exit":
        break
    phone=int(input("Enter your phone no.:"))
    store[name]=phone
print(store)
