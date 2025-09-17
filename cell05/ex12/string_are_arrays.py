import re
Message = input("Enter Your Message : ")

if(Message == ""):
    print("none")
else:
    numbers = re.findall("z", Message)  
    for i in numbers:
        print("z",end="")