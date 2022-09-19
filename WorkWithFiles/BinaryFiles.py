import pickle

FILENAME = "user.dat"

name = "Tom"
age = 19

with open(FILENAME, "wb") as file:
    pickle.dump(name, file)
    pickle.dump(age, file)

with open(FILENAME, "rb") as file:
    name = pickle.load(file)
    age = pickle.load(file)
    print(f"Name: {name}, age: {age}")

print("---\n" * 2, end="")

FILENAME2 = "users2.dat"

users = [
    {"name": "Tom", "age": 19},
    {"color": "red", "smell": "salt"}
]

with open(FILENAME2, "wb") as file:
    pickle.dump(users, file)

with open(FILENAME2, "rb") as file:
    load = pickle.load(file)
    print(load)