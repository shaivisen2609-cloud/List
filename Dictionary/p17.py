#Programmed by: Shaivi Sen
#Rollno.: 57
#Dictionary assignment no.:17
#Given a dictionary with some duplicate values, find a way to print all the unique values.
dictionary={"A":20,"B":4,"Z":78,"A":56,"G":34,"S":90,"Z":65}
print(dict(set(dictionary.items())))
