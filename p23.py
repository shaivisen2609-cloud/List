#Programmed by: Shaivi Sen
#Rollno.: 57
#List assignment no.: 23
'''"A cricket player scored runs in 6 matches.
Example: [45, 60, 10, 80, 55, 90]
Write a program to:
Find total runs
Find highest score
Count how many matches player scored more than 50 runs"'''
scored=[45, 60, 10, 80, 55, 90]
total=0
count=0
for run in scored:
    if run>50:
        count+=1
    total+=run
print("Total runs:",total)
scored.sort()
print("Highest score:",scored[-1])
print("No. of players scored more than 50:",count)
