#temperature exercise
temp=int(input("Please enter a temperature in Fahrenheit: "))

c=5/9*(temp-32)
print(f"{temp} degrees Fahrenheit equals {c:.2f} degrees Celcius")
print("Brr! it's cold in here!") if c<0 else None