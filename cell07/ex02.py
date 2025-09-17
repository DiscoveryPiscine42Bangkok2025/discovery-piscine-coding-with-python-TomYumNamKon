def average(clas):
    sum = 0
    count = 0
    for i in clas.values():
        sum += i
        count += 1
    if count == 0:
        return None
    return sum / count


class_3B = {
    "marie": 18,
    "jean": 15,
    "coline": 8,
    "luc": 9
}

class_3C = {
    "quentin": 17,
    "julie": 15,
    "marc": 8,
    "stephanie": 13
}

print(f"Average for class 3B: {average(class_3B)}.")
print(f"Average for class 3C: {average(class_3C)}.")