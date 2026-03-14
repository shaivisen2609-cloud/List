#Programmed by: Shaivi Sen
#Rollno.: 57
#List assignment no.: 20
'''"A cricket player scored runs in 6 matches.
Example: [45, 60, 10, 80, 55, 90]
Find:
Total runs
Highest score"'''
scored=[45, 60, 10, 80, 55, 90]
total=0
for runs in scored:
    total+=runs
print("Total runs:",total)
scored.sort()
print("Highest runs:",scored[-1])