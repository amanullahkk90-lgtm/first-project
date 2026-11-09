def greet(id):
     if id==0:
         print("hello",id)
         id = id + 1
     if(id==9):
         return
    
greet(id)

greet(0)

def add(a,b):
    return(a+b)

answer = add(2,5)
print(answer)


def double(numbers):
    return(numbers * 2)
ans = double(6)
print(ans)


def is_passing(mark):
    return(mark>=50)

# result= is_passing(40)
# print(result)

marks = [60,40,75]

for mark in marks:
    result= is_passing(mark)
    print(mark,result)



def sum_number(numbers):
  total=0
  for num in numbers:
    total= total + num
  return total
numbers=[]
for i in range(5):
  num=int(input("enter a number :"))


  if num < 0:
    continue

  numbers .append(num)

print("finale list",numbers)

print(sum_number(numbers))


def calculate_discount(total):
    if total >500 :
        discount=total *0.15
    elif total >=200:
        dicount= total *0.10
    else:
        discount=0

    return total

calculate_discount()


print("finale amount after discount",calculate_discount)


import calc

print(calc.add(3,4))
