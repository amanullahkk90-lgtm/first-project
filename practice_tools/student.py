def introduction(name,course):
    return (f"my name is {name}and i am learning {course}")

def calculate_average(mark1,mark2,mark3):
    total = mark1 + mark2 + mark3
    average= total/3
    return average


def create_student(name,marks):
    return{
        "name":name,
        "marks":marks
    }

def create_record(name,attended,total):
    return{
        "name":name,
        "attended":attended,
        "total":total
    }