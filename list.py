marks=[45,72,50,30]

for mark in marks:
    if mark >=50:
        print(mark,"pass")
    else:
        print(mark,"fail")    

stock ={
"Pens":8,
"Notebooks":0,
"Folders":3
}
for items in stock:
    quantity=stock[items]
    if quantity > 0:
        print(items,quantity,"in stock")
    else:
        print(items,quantity,"out of stock")    


products=["Notebooks","pens","Folders"]
stock ={
"pens":8,
"Notebooks":0,
"Folders":3
}  

total_quantites=0
for product in products:
    quantity = stock[product]
    if quantity <=2 :
        print(product,"is in stock") 
        total_quantites += quantity
    else:
        print(product,"enough stock")
print("available quantity of all products ",total_quantites)        







products = [ "notebooks","pens","folders"]

stock={
"pens":8,
"notebooks":0,
"folders":3
}
if stock[products[0]]<=2:
    print(products[0],"low stocks")
else:
    print(products[0],"enough stock")    
if stock[products[1]]<=2:
    print(products[1],"low stock")
else:
    print(products[1],"enough sotck")
if stock[products[2]]<=2:
    print(products[2],"low stock")
else:
    print(products[2],"enough stock")                