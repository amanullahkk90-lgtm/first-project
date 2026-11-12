

from practice_tools import calc

print(calc.add(3,4))
print(calc.sub(9,19))
print(calc.multipy(3,4))
print(calc.divide(1600,400))







from practice_tools import greeting
message=greeting.greet("aman")
print(message)
farewell=greeting.bye("aman")
print(farewell)

from practice_tools import student
frist_Student= student.introduction("aman","python")
result1=student.calculate_average(90,60,55)

second_student= student.introduction("zahida","English")
result2=student.calculate_average(70,80,90)

print(frist_Student)
print("your average is :",result1)
print(second_student)
print("your average is :",result2)