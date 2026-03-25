#Programmed by: Shaivi Sen
#Rollno.: 57
#Dictionary assignment no.:18
'''"Create a program to manage student marks using dictionary.
Features
Store student name and marks
Display all students
Search student
Find topper
Calculate class average"'''
student={"Avya":73,"Bhumi":49,"Ziya":78,"Arya":59,"Geeta":34,"Sumi":90,"Manu":65}
print("All students:",student)
max=0
name=0
for key,value in student.items():
    if value>max:
        max=value
        name=key
print(name)
print(max)
print("Topper:",name,"-",max)