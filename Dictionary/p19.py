#Programmed by: Shaivi Sen
#Rollno.: 57
#Dictionary assignment no.:19
'''"Create a simple phone book using a dictionary where name is the key and phone number is the value.
Features
Students should implement:
Add new contact
Display all contacts
Search contact by name
Delete a contact"'''
name="Khushi","Suhani","Lovely"
phone=9076896502,9170478657,9876543223
store=dict(zip(name,phone))
print(store)
store["Mansi"]=9026325411
print(store)
print(store.values())
search_name=input("enter name :")
for key,value in store.items():
    if search_name == key:
        print(key,value)
store.pop("Suhani")
print("deleted contact",store)