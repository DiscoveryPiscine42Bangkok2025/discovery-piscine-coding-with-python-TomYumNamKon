import re

MainMessage = input("Enter Your Main Message : ")
Message = input("Enter Your Messafe : ")
if(MainMessage == "" or Message == ""):
    print("none")
numbers = re.findall(MainMessage, Message)  
print(len(numbers))