word = input()
i = 0
check =""
while i < len(word):
    if(word[i] == word[i].upper()) :
        check += word[i].lower()
    else :
        check += word[i].upper()
    i += 1
print(check)
