#Programmed by: Shaivi Sen
#Rollno.: 57
#List assignment no.: 16
#Store marks of 5 students in a list and calculate the average marks.
marks=[45,67,57,34,89]
sum=0
for i in marks:
    sum+=i
avg=sum/len(marks)
print(marks)
print("Agerage:",avg)