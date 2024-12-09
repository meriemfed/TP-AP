age1=int(input("Please type in the age of the first person:"))
age2=int(input("Please type in the age of the second person:"))

if(age1==age2):
    print("Both people are the same age!")
else:
    old=age1 if age1>age2 else age2

    print(f"The older age is:{old}")