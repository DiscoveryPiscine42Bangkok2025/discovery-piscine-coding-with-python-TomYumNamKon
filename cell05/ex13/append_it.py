import re 

Message = input("Enter Your Message : ")
if(Message == ""):
    print("none")
else:
    NewMessage = Message.split(" ")
    for i in NewMessage:
        if(re.findall("ism$", i)):
            continue
        else:
            print(i+"ism")