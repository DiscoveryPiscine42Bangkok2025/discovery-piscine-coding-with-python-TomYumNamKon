Message = input("Enter Your Message : ")
NewMessage = Message.split(" ")
if(NewMessage == ['']):
    print("none")
else:
    print(Message.lower())