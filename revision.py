def pass_fail(marks):
    passed = []
    failed = []

    for num in marks:
        if num >= 50:
            passed.append(num)
        else:
            failed.append(num)

    return passed, failed


passed, failed = pass_fail([75, 40, 50, 30, 90])

print("Passing marks:", passed)
print("Failing marks:", failed)


def replace_negative(numbers):
    result=[]

    for num in numbers:
        if num <0:
            result.append(0)
        else:
            result.append(num)
    return result

print(replace_negative([5,-3,0,-8,9]))            