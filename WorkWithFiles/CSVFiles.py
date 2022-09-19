import csv

FILENAME = "users.csv"

users = [
    ("Tom", 28),
    ("Alice", 23),
    ("Bob", 34)
]

with open(FILENAME, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(users)

with open(FILENAME, "a", newline="") as file:
    user = ("Sam", 31)
    writer = csv.writer(file)
    writer.writerow(user)

with open(FILENAME, "r", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row[0], "-", row[1])

print("---\n" * 2, end="")

FILENAME2 = "users2.csv"

users_dict = [
    {"name": "Tom", "age": 28},
    {"name": "Alice", "age": 23},
    {"name": "Bob", "age": 34}
]

with open(FILENAME2, "w", newline="") as file:
    columns = ["name", "age"]
    writer = csv.DictWriter(file, fieldnames=columns)
    writer.writeheader()

    writer.writerows(users_dict)

    user = {"name": "Sam", "age": 40}
    writer.writerow(user)

with open(FILENAME2, "r", newline="") as file:
    reader = csv.DictReader(file)
    for line in reader:
        print(line["name"], "-", line["age"])


