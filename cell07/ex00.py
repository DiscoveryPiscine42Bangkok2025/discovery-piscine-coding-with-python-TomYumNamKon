def array_of_names(dic):
    fullnames = []
    for first, last in dic.items():
        full = f"{first.capitalize()} {last.capitalize()}"
        fullnames.append(full)
    return fullnames


# ทดสอบ
persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(persons))
