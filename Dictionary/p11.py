#Programmed by: Shaivi Sen
#Rollno.: 57
#Dictionary assignment no.: 11
#Create two dictionaries (e.g., set1 and set2 of items) and merge them into one using the .update() method or the | operator
set1={"pen":20,"book":100}
set2={"copy":75,"bag":200}
set1.update(set2)
print(set1)
print(set1|set2)