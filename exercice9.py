cities={}

while 1==1:
    name=str(input("enter the name of the city: "))
    if(name.lower()=="stop"):
        break    
    cities[name]=len(name)*1000000

sorted_cities=dict(sorted(cities.items(),key=lambda item:item[1],reverse=True))
print("sorted cities:")   
print(sorted_cities) 
