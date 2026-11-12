def find_grade(marks):
    average=sum(marks)/len(marks)

    if average >=80:
        return "A"
    elif average >=60:
        return "B"
    elif average >=50:
        return "C"
    else:
        return "failed"


