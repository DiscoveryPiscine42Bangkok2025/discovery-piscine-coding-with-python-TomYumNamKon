def find_the_redheads(family):
    arr = []
    for i , j in family.items():
        if(j == "red"):
            arr.append(i)
    return arr

dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

print(find_the_redheads(dupont_family))