import random
import datetime
import string

#function to generate random usernames made from letters and digits
def generateuser():
    user_length=random.randint(4,10)
    username=''.join(random.choices(string.ascii_letters+string.digits,k=user_length))
    return username




ops={"SUBSTRACTION":"-","ADDITION":"+","MULTIPLICATION":"*","DIVISION":"/"}

file_name =str(input("enter file name (without extension):")) 


with open(file_name+".txt",'a') as file:

    for i in range(3): #set range to 3 for testing 

        operation_text,operation_sign=random.choice(list(ops.items())) #generate random operation and its sign
        op1=random.randint(1,100) #generate the two operands
        op2=random.randint(1,100)
        numb=random.randint(1000,99999) #set the big number idk what it is
        username=generateuser()
        now = datetime.datetime.now() #set the date and time
        formatted_datetime = '"'+now.strftime("%Y-%m-%d %H:%M:%S")+'"'
        file.write(f"\n{operation_text},{op1}{operation_sign}{op2},1,{numb},{username},{formatted_datetime}\n") #write to file
        
        
