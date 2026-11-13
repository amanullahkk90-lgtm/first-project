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



from practice_tools import contact,sreach
contact_list=[
contact.create_contact("Aman","2222"),
contact.create_contact("zahida","3333"),
contact.create_contact("Ali","4444")
]
found_phone=sreach.find_contact(contact_list,"Aman")
print(found_phone)
another_sreach=sreach.find_contact(contact_list,"zain")
print(another_sreach)


from practice_tools import dice,winner

player_roll=dice.roll_dice()
computer_roll=dice.roll_dice()
result=winner.decide_winner(player_roll,computer_roll)

print(f"your roll:{player_roll}")
print(f"computer roll :{computer_roll}")
print(f"result :{result}")