# for numbers in [2,4,6]:
    # print(numbers)


# for numbers in range(2,6):
    # print(numbers)


count = 1
while count <=3:
    print(count)
    count +=1


names=["Aman","Ayesha","Hurera"]

for name in names:
    print(name)



numbers = 5 

while numbers > 0:
    print(numbers)
    numbers -= 1

#range
for number in range(1,6):
    print(number)


#break
for number in [1,2,3,4,5]:
    if number == 3:
        print("found it")
        break   
    print(number)
    
students=["Aman","Ayesha"]
scores={
"Aman":72,
"Ayesha":45
}

for names in students:
    marks = scores[names]

    if marks <50:
       continue
    
    print(names,"pass")
    # else:
    #  print(names,"fail")    
