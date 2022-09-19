dictionary = {1: "Tom", 2: "Bob", 3: "Bill"}

emails = {"tom@gmail.com": "Tom", "bob@gmail.com": "Bob", "sam@gmail.com": "Sam"}

objects = {1: "Tom", "2": True, 3: 106}

objects = {}

objects = dict()

user_list = [
    ["1", "Tom"],
    ["2", "Bob"],
    ["3", "Alice"]
]

user_dict = dict(user_list)
print(user_list)
print(user_dict)

user_tuple = (
    (1, "Tom"),
    ("2", "Bob"),
    (3, "Alice")
)

print(dict(user_tuple))

user_dict = dict(user_tuple)

print(user_dict[1])
print(user_dict["2"])
user_dict[1] = "Tomas"
print(user_dict)
user_dict[4] = "Granny"
print(user_dict)

print('---')

print(user_dict.get(1))
print(user_dict.get(5, "Abobik"))
print(user_dict)

print('---')

users = {
    1: "Tom",
    2: "Bob",
    3: "Alice"
}

print(users)
del users[1]
print(users)

if 4 in users:
    del users[4]
    print("4 deleted")
else:
    print("4 not found")

print(users.pop(2, "Abobik"))
print(users.pop(2, "Abobik"))

users.clear()

print('---')

users = {
    1: "Tom",
    2: "Bob",
    3: "Alice"
}

users2 = {
    4: "Kate",
    5: "Sam",
    6: "Julia"
}

users.update(users2)

print(users)

print('---')

users = {
    1: "Tom",
    2: "Bob",
    3: "Alice"
}

for key, name in users.items():
    print(key, name)

for key in users.keys():
    print(key)

for value in users.values():
    print(value)

print("---")

users = {
    "Tom": {
        "phone": "+971478745",
        "email": "tom12@gmail.com"
    },
    "Bob": {
        "phone": "+876390444",
        "email": "bob@gmail.com",
        "skype": "bob123"
    }
}

old_email = users["Tom"]["email"]
users["Tom"]["email"] = "supertom@gmail.com"
print(users["Tom"])

if "skype" in users["Tom"]:
    print(users["Tom"]["skype"])
else:
    print("Not found skype")