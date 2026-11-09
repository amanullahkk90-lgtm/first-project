age = 20
if age >= 18:
    print("adult")

x=15
print(10 < x <20)

#if/else

age = 16
if age >= 18:
    print("can vote")
else:
    print("too young too vote")


#if/elif/else

marks= 82

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade ="A"
elif marks >=70:
    grade ="B"
else:
    grade ="fail or lower"

print(grade)

#nested condtions

 
age = 19
has_id = False

if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("Show your ID")
else:
    print("Under 18")


#or/and opeartors

username = "Aman"
password = "1234"

if username == "Aman" and password == "1234":
    print("Login successful")


day = "saturday"
if day=="saturday" or "sunday":
    print("weekend")    
