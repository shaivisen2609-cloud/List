#Programmed by: Shaivi Sen
#Rollno.: 57
#List assignment no.: 15
#A week's temperatures are stored in a list. Find how many days were "Hot" (above 35°C)
temp=[28,35,23,31,37,45,39]
days=0
for i in temp:
    if i>35:
        days+=1
print(days,"days are Hot in a week")