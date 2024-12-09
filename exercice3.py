total=int(input("Total amount:"))
nb_items=int(input("Number of items:"))
day=str(input("Day of the week:").lower) 

if(day in ["monday","tuesday","wednesday","thursday","friday"]):
    if(nb_items>5):
        print("Total price after discount:",total-(total*0.15),"dinars")
    else:
        print("Total price after discount:",total-(total*0.10),"dinars")
else:
     if(nb_items>5):
        print("Total price after discount:",total-(total*0.25),"dinars")
     else:
        print("Total price after discount:",total-(total*0.20),"dinars")