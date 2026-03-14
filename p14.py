#Programmed by: Shaivi Sen
#Rollno.: 57
#List assignment no.: 14
#Store prices of 5 items in a list. Calculate the total bill and the average price per item.
itemprices=[250,600,470,100,380]
sum=0
for price in itemprices:
    sum+=price
print(itemprices)
print("Total bill:",sum)
avg=sum/len(itemprices)
print("Average:",avg)
