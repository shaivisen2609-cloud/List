#Programmed by: Shaivi Sen
#Rollno.: 57
#List assignment no.: 5
#Create a list of 10 random integers. Use a for loop to print each number multiplied by 2.
import random 
number=[]
for count in range(1,11):
    temp=random.randrange(1,100)
    number.append(temp)
print(number)
for i in number:
    print(i*2)