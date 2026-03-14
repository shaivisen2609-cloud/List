#Programmed by: Shaivi Sen
#Rollno.: 57
#List assignment no.: 13
#Create a list of ages. Create two new lists: minors (under 18) and adults (18 and above)
agelist=[10,19,22,34,20,16,18,25,33,56,32,12]
minors=[]
adults=[]
for age in agelist:
    if age<18:
        minors.append(age)
    else:
        adults.append(age)
print("minors (under 18):",minors)
print("adults (18 and above):",adults)
