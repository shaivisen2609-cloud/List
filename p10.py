#Programmed by: Shaivi Sen
#Rollno.: 57
#List assignment no.: 10
#Given a list of 10 student marks, count how many students scored above 40.
marks=[45,67,57,34,39,78,37,65,59,31]
count=0
for i in marks:
    if i>40:
        count+=1
print(count,"students scored above 40")
