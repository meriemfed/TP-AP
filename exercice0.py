n=int(input("How many people need a ride?"))
m=int(input("How many people fit in one taxi?"))

full_taxi=n//m
if(n%m!=0):
    full_taxi+=1

print("Number of taxis needed:",full_taxi)