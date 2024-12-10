#operations exercise

n1=int(input("number 1: "))
n2=int(input("number 2: "))
op=str(input("operation (add/multiply/substract/divide) : "))

if op=="add":
    print(f"{n1}+{n2}={n1+n2}")
if op=="multiply":
    print(f"{n1}*{n2}={n1*n2}")
if op=="substract":
    print(f"{n1}-{n2}={n1-n2}")
if op=="divide":
    print(f"{n1}+{n2}={n1+n2}") if n2!=0 else print("division per zero!")