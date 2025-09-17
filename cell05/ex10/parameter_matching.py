MessagePassword = input("Enter Your Key Password : ")
Message = input("What was the parameter? ")
if(MessagePassword == "" or Message == ""):
    print("none")
elif(Message == MessagePassword):
    print("Good job!")
else: 
    print("Nope, sorry...")
