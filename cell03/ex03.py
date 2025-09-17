for n in range(1, 11):
    i = 0
    result = ""
    while i <= 10:
        result = result + " " + str(i * n)
        i += 1
    print("Table de :" + result)