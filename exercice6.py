ammount=str(input("Please type in a price:"))
#i used the split method to seperate dinars and centimes parts
am=ammount.split(".")
print("Dinars: ",am[0])
print("Centimes: ",am[1])
