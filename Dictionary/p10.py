#Programmed by: Shaivi Sen
#Rollno.: 57
#Dictionary assignment no.: 10
#Given a dictionary of student names and their marks, print only the names of students who scored above 75
stu_mark={"jiya":76,"aditi":59,"anu":82,"avaya":49,"lata":91}
for key,value in stu_mark.items():
    if value>75:
        print(key)