stock = {
    "pens":8,
    "notebooks":0,
    "folders":3

}

for item ,quantity  in stock.items():
    if quantity > 0:
        print(item,"is in stock" , quantity)
    else:
        print(item,"is out of stock",quantity)    
    
    
    # print(item,quantity > 0)



#list

numbers = [2,7,4,9]

for number in numbers:
    if number > 5:
        print(number)


students =["Aman","Ayesha","Hurera"]

score = {

       "Aman":72,
       "Ayesha":45,
       "Hurera":60
}
for name in students:
    mark = score[name]
   
    if mark >= 50:
        print(name,"pass")
    else:
        print(name,"fail")    




students = ["Aman","Ayesha","Hurera"]

score={

    "Aman":72,
    "Ayesha":45,
    "Hurera":57
}

def is_passing(mark):
    return mark >= 50

pass_count= 0
fail_count=0

for name in students:
    mark = score[name]

    if is_passing(mark):
        pass_count +=1
    else:
        fail_count += 1    
print("students who passed :" , pass_count)  
print("student who failed: " , fail_count)      




students = ["Aman","Ayesha","Hurera"]

score = {
"Aman":72,
"Ayesha":45,
"Hurera" :65
}
index=0

while index < len(students):
    name=students[index]
    mark=score[name]

    print(name,mark)

    index +=1


stock ={
 "Pens":8,
 "Notebook":0,
 "Folders":3

}
total_available=0
for items,quantity in stock.items():
    if quantity > 0:
        print(items,"is in stock")
    
        total_available += quantity
    else:
        print(items,"out of stock")    
print("total available",total_available)        