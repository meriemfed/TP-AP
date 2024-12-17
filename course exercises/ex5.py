import math

while True:
    n=int(input("Please enter a number:"))
    if n==0:
        break

    print("invalid number") if n<0 else print(math.sqrt(n))

    
