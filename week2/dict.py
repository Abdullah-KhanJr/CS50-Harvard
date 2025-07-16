person = {
    "name": "Abdullah",
    "age": 20,
    "dob": 2005,
    "gender": "male"
}

person2 = {
    "name": ["Abdullah", "Ahmed", "Khan"]
}

print(person)
print()
print(person["name"])
print()
print(person2["name"])
print()
print(person2["name"][1])

person["city"] = "Thana"

print(person)