
#i assumed input will be automatically entered in seconds
print("Runner 1:")
name1=str(input("Name: "))
time1=input("Time(in second): ")

print("Runner 2:")
name2=str(input("Name: "))
time2=input("Time(in second): ")

if(time1==time2):
    print(f"{name1} and {name2} have the same time")
else:
    winner=name1 if time1>time2 else name2
    print(f"The faster runner is {winner}")

