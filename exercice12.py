w=int(input("width: "))
h=int(input("height: "))

print("#"*w)
[print("#"+" "*(w-2)+"#")  for i in range(h)]
print("#"*w)