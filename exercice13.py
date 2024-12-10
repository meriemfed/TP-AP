
while 1==1:
    text=str(input("Please type in a string: "))
    if text=='':
        break
    print(f"{text}")
    print("-"*len(text)) #i used this one
    #print("\033[4m" + text + "\033[0m") i found this  ANSI escape code online

