Message = input("Enter Your Message : ")
NewMessage = Message.split()
print(f"parameters: {len(NewMessage)}")
for i in NewMessage:
    print(f"{i}: {len(i)}")