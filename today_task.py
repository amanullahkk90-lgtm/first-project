student_name="amanullah khan"
age_as_text= "23" # age is given in text for to converion 
height=1.65
age = int(age_as_text) # age is converted into integer
is_ready= True

print("name", student_name)
print("Age", age)
print("Height", height)
print("Ready", is_ready)

#list & dictionaries
fruits = ["apple","banana","cherry"]
print(fruits[0])
print(fruits[-1])
print(fruits[0:2])

#modify list
fruits.append("mango")
fruits.insert(1,"kiwi")
fruits[0] = "grape"
fruits.remove("banana")
last= fruits.pop()
del fruits[0]

#dictionaries

student ={"name":"Aman","age":21,"major":"cs"}

print(student["name"])
print(student.get("gpa"))
print(student.get("gpa",0.0))

student["age"] = 22
student["gpa"] = 3.5 
del student["major"]
student.update({"city":"karachi","year":4})


num1= 10
num2= "20"

int(result = num1 + num2)


print("10" + "20" +"20")
