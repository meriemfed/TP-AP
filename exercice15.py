word=str(input("Please type in a string:"))

vowels=['a','e','o']

for v in vowels:
    if word.rfind(v)!=-1:
        print(f"{v} found")
    else:
        print(f"{v} not found")      
 

