#Programmed by: Shaivi Sen
#Rollno.: 57
#List assignment no.: 18
'''"A shop recorded the number of customers for 7 days.
List example: [50, 45, 60, 70, 65, 55, 80]
Find the total customers in the week."'''
record=[50, 45, 60, 70, 65, 55, 80]
total=0
for customers in record:
    total+=customers
print("Total customers in the week:",total)