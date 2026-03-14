#Programmed by: Shaivi Sen
#Rollno.: 57
#List assignment no.: 21
'''"A teacher stores marks of students in a list
marks = [78, 65, 89, 90, 56]
Write a program to:
Print all marks
Find total marks
Find average marks
Find highest marks
Find lowest marks"'''
marks = [78, 65, 89, 90, 56]
total=0
for i in marks:
    print(i)
    total+=i
print("Total:",total)
avg=total/len(marks)
print("Average:",avg)
'''marks.sort()
print("Highest marks:",marks[-1])
print("Lowest marks:",marks[0])'''
print("Highest marks:",max(marks))
print("Lowest marks:",min(marks))