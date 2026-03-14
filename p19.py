#Programmed by: Shaivi Sen
#Rollno.: 57
#List assignment no.: 19
'''"A teacher stored attendance of students in a list (1 = present, 0 = absent).
Example: [1,1,0,1,0,1,1]
Write a program to:
Count total present
Count total absent
Print attendance percentage"'''
list=[1,1,0,1,0,1,1]
present=0
absent=0
for i in list:
    if i==1:
        present+=1
    else:
        absent+=1
print("Total present:",present)
print("Total absent:",absent)
per_present=present/len(list)*100
print("Percentage of students present:",per_present)