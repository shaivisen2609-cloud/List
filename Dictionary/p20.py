#Programmed by: Shaivi Sen
#Rollno.: 57
#Dictionary assignment no.:20
'''"Create Attendance System where 
Faculty should:
Add attendance for 5 students
Count total present students
Display absent students"'''
attendance={"A":1,"B":1,"C":0,"D":1,"E":0}
present=0
namepre=""
absent=0
nameabs=""
for key,value in attendance.items():
    if value==1:
        present+=1
        namepre+=key+","
    else:
        absent+=0
        nameabs+=key+","
print("Present Student:",present,"-",namepre)
print("Absent Student:",absent,"-",nameabs)



