numbers=[15,7,23,5,10]
count=0
for i in numbers:
    count=count+i
print(count)    




numbers=[10,20,30,40,50]
count=0
total=0

for i in numbers:
    total=total + i
    count=count + 1
if count >0:
    average=total/count
    print(average)
else:
    print("the list is empty")    

numbers=[-12,-4,-19,-7]
largest=numbers[0]
for i in numbers:
    if i >largest:
        largest =i
print(largest)    
