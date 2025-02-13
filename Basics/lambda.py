people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"},
]

def f(person):
    return person["name"]

# lambda - function , person - argument that it takes, person["name"] - what it returns
people.sort(key=lambda person: person["name"])

print(people)