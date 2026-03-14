#Programmed by: Shaivi Sen
#Rollno.: 57
#List assignment no.: 8
#Given a list of numbers 1-20, create a new list that contains only the even numbers.
list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
even_list=[]
for num in list:
    if num%2==0:
        even_list.append(num)
print(even_list)