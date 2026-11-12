from practice_tools import calc
result= calc.add(13,19)
print(result)

result2=calc.sub(1000,324)
print(result2)


third_answer=calc.multipy(6,4)
print(third_answer)



first_number=8
second_number=5
thrid_number=3
result3=calc.multipy(first_number,third_answer)
print(result3)


student_marks=[90,80,70]
average=calc.calculate_average(student_marks)

print(average)


from practice_tools import result,student,eligibility
student_data=student.create_student("Aman",[90,80,70])
status=result.check_pass(student_data["marks"])
print(f"student:{student_data['name']}")
print(f"Marks:{student_data['marks']}")
print(f"result:{status}")


student_record=student.create_record("aman",18,24)
check = eligibility.check_attendance(
    student_record["attended"],
    student_record["total"]
)
print(f"student:{student_record['name']}")
print(f"Attendance: {student_record['attended']}/{student_record['total']}")
print(f"can sit in exam:{check}")

from practice_tools import shopping,bill,grading
order=shopping.create_order("Aman",[400,350,450])
finale_bill=bill.calculate_Bill(order['prices'])
print(f"customer :{order['customer']}")
print(f"finale bill :{finale_bill}")


student_record2=student.create_student("Sara",[70,80,90])
check_average=grading.find_grade(student_record2["marks"])
print(f"student:{student_record2['name']}")
print(f"average grade :{check_average}")