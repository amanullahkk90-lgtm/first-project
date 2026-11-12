def check_pass(marks):
    average=sum(marks)/len(marks)
    if average>=50:
        return "passed"
    else:
        return"failed"