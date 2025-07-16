people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house":"Slytherin"}
]

print(people[0]["name"])

for h in people:
    print(h["house"])



# def func(person):
#     return person["name"]


# people.sort(key = func)
people.sort(key = lambda person: person["name"])

print (people)