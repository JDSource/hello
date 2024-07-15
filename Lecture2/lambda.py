people = [
    {"name": "Harry", "house": "Gryffendor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Sytherin"}
]

people.sort(key=lambda person: person["name"])

print(people)