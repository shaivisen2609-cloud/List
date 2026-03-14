#Programmed by: Shaivi Sen
#Rollno.: 57
#List assignment no.: 22
'''"Marks of students are stored in a list.
marks = [78, 35, 90, 40, 55]
Write a program to:
Print PASS if marks ≥ 40
Print FAIL if marks < 40
Count how many students passed"'''
marks = [78, 35, 90, 40, 55]
passcount=0
for i in marks:
    if i>=40:
        passcount+=1
        print(i,"- Pass")
    else:
        print(i,"- Fail")
print("No. of student pass:",passcount)
