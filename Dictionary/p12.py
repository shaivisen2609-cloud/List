#Programmed by: Shaivi Sen
#Rollno.: 57
#Dictionary assignment no.: 12
#You have two lists: keys = ['ID', 'Name', 'Salary'] and values = [101, 'Rahul', 50000]. Convert them into a single dictionary
keys=["ID","Name","Salary"]
values=[101,"Rahul",50000]
#print(dict(zip(keys,values)))
dict={}
for i in range(len(keys)):
    dict[keys[i]]=values[i]
print(dict)