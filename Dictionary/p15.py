#Programmed by: Shaivi Sen
#Rollno.: 57
#Dictionary assignment no.:15
#Given a dictionary of employees and their salaries, increase every salary by 10% and update the dictionary
employee={"Shyam":6000,"Jiya":4500,"Seema":6500}
print("Dictionary:",employee)
for name,salary in employee.items():
    employee[name]=salary+salary*10//100
print("Uptaded dictionary:",employee)