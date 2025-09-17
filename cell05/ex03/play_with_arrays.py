MyArray = [2, 8, 9, 48, 8, 22, -12, 2]
MyNewArray = [] 
i = 0
j = 0

print(MyArray)
while i < len(MyArray) :
    if(MyArray[i] > 5):
        MyNewArray.append(0)
        MyNewArray[j] = MyArray[i] + 2
        j = j + 1
    i = i + 1
print(set(MyNewArray))