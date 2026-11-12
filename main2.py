from practice_tools import books,availability

book_record=books.create_book("Harry Potter",6)
book_availabilty=availability.check_availability(book_record["copies"])
print(f"Book name : {book_record['Title']}")
print(f"title : {book_availabilty}")

from practice_tools import employee,workhours

employee_record=employee.create_employee("Aman",[8,7,9,8,8])
employee_hour=workhours.check_hours(employee_record["hours"])

print(f"employee name :{employee_record['name']}")
print(f"weekly result :{employee_hour}")