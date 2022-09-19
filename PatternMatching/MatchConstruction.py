# match in python looks like switch in java

def print_hello(language):
    match language:
        case "russian":
            print('привет')
        case "english":
            print('hello')
        case "german":
            print("Hallo")
        case "american english" | "british english" | "canada english":
            print("Hello again")
        case _:
            print("Unknown language")


print_hello("english")
print_hello("german")
print_hello("russian")

print("---")


def print_data(user):
    match user:
        case("Tom" | "Tomas" | "Tommy", 37):
            print("default user")
        case("Tom", age):
            print(f"Age: {age}")
        case(name, 22):
            print(f"Name: {name}")
        case(name, age):
            print(f"Name: {name}, age: {age}")


print_data(("Tom", 37))
print_data(("Tom", 28))
print_data(("Tom", 22))
print_data(("Tomas", 37))
print_data(("Sam", 22))
print_data(("Bob", 41))
print_data(("Tom", 33, "Google"))

print("---")


def print_data(user):
    match user:
        case ("Tom", 37) | ("Bob", 21):
            print("default user")
        case (name, age):
            print(f"Name: {name}, age: {age}")


print_data(("Tom", 37))
print_data(("Bob", 21))
print_data(("Jimmy", 14))

print("---")


def print_data(user):
    match user:
        case ("Tom", 37) | ("Bob", 21):
            print("default user")
        case ("Sam", _):
            print(f"It's Sam")
        case (_, _):
            print("Undefined user")


print_data(("Tom", 37))
print_data(("Sam", 100))
print_data(("Bill", 100))

print('---')


def print_data(user):
    match user:
        case (name, age, company):
            print(f"Name: {name}, age: {age}, company: {company}")
        case (name, age):
            print(f"Name: {name}, age: {age}")
        case (name):
            print(f"Name: {name}")


print_data(("Tom"))
print_data(("Tom", 23))
print_data(("Tom", 45, "Google"))
print_data(("Tom", None))

print('---')


def print_data(user):
    match user:
        case (name, age, *rest):
            print(f"Name: {name}, age: {age}, rest info: {rest}")
        case (name, age):
            print(f"Name: {name}, age: {age}")
        case (name):
            print(f"Name: {name}")


print_data(("Tom"))
print_data(("Tom", 23))
print_data(("Tom", 45, "Google"))
print_data(("Tom", None))

print('---')


def print_data(user):
    match user:
        case (name, age, *_):
            print(f"Name: {name}, age: {age}, rest don't make sense")
        case (name, age):
            print(f"Name: {name}, age: {age}")
        case (name):
            print(f"Name: {name}")


print_data(("Tom"))
print_data(("Tom", 23))
print_data(("Tom", 45, "Google"))
print_data(("Tom", None))

print('---')


def print_people(people):
    match people:
        case["Tom", "Sam", "Bob"]:
            print("Default people")
        case["Tom", second, _]:
            print(f"Second person: {second}")
        case[first, second, third]:
            print(f"{first}, {second}, {third}")


print_people(["Tom", "Sam", "Bob"])
print_people(["Tom", "Mike", "Bob"])
print_people(["Bill", "Sam", "Bob"])
print_people(["Tom", "Kate"])

print('---')


def print_people(people):
    match people:
        case[_]:
            print("1 person")
        case[_, _]:
            print("2 people")
        case[_, _, _]:
            print("3 people")
        case _:
            print("Undefined")


print_people(["Tom"])
print_people(["Tom", "Sam"])
print_people(["Tom", "Sam", "Bob"])
print_people("Tom")

print('---')


def print_people(people):
    match people:
        case ["Tom", *rest]:
            print(f"First: Tom, other: {rest}")


print_people(["Tom", "Bob", "Mike"])

print('---')


def print_people(people):
    match people:
        case[first, *_]:
            print(f"First: {first}")


print_people(["Tom", "Mike", "Bob"])

print('---')


def print_people(people):
    match people:
        case["Tom" | "Tomas" | "Tommy", "Sam", "Bob"]:
            print("Default people")
        case["Bob", "Mike"] | ["Alice", "Bill"]:
            print("Default people too")


print_people(["Tommy", "Sam", "Bob"])
print_people(["Bob", "Mike"])
print_people(["Alice", "Bill"])

print('---')


def look(words):
    match words:
        case {"red": "красный", "blue": "синий"}:  # если в словаре words слова red и blue
            print("Слова red и blue есть в словаре")
        case {"red": "красный"}:        # если в словаре words есть слово red
            print("Слово red есть в словаре, а слово blue отсутствует")
        case {"blue": "синий"}:        # если в словаре words есть слово blue
            print("Слово blue есть в словаре, а слово red отсутствует")
        case {}:
            print("Слова red и blue в словаре отсутствует")
        case _:
            print("Это не словарь")


look({"red": "красный", "blue": "синий", "green": "зеленый"})
look({"red": "красный", "green": "зеленый"})
look({"blue": "синий", "green": "зеленый"})
look({"green": "зеленый"})
look("yellow")

print('---')


def look(words):
    match words:
        case{"red": "красный" | "алый" | "червонный"}:
            print("Red есть в словаре")
        case{}:
            print("Red отсутствует в словаре")


look({"red": "красный", "green": "зеленый"})
look({"blue": "синий", "green": "зеленый"})
look({"green": "зеленый"})

print('---')


def look(words):
    match words:
        case{"red": "красный"} | {"blue": "синий"}:
            print("Red или blue есть в словаре")
        case{}:
            print("Red и blue отсутствует в словаре")


look({"red": "красный", "green": "зеленый"})
look({"blue": "синий", "green": "зеленый"})
look({"green": "зеленый"})

print('---')


def look(words):
    match words:
        case{"red": _} | {"blue": _}:
            print("Red или blue есть в словаре")
        case{}:
            print("Red и blue отсутствует в словаре")


look({"red": "красный", "green": "зеленый"})
look({"blue": "синий", "green": "зеленый"})
look({"green": "зеленый"})

print('---')


def look(words):
    match words:
        case{"red": red, "blue": blue}:
            print(f"Red: {red} и blue: {blue} есть в словаре")
        case{}:
            print("Red и blue отсутствует в словаре")


look({"red": "красноватый", "blue": "синеватый", "green": "зеленый"})
look({"blue": "синеватый", "green": "зеленый"})
look({"green": "зеленый"})

print('---')


def look(words):
    match words:
        case{"red": "красный", **rest}:
            print(f"Red, rest: {rest}")
        case{}:
            print("Red isn't applicable")


look({"red": "красный", "blue": "синий", "green": "зеленый"})
look({"red": "красный", "blue": "синий"})

print('---')


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def print_person(person):
    match person:
        case Person(name="Tom", age=37):
            print("Default person")
        case Person(name=name, age=37):
            print(f"Name: {name}")
        case Person(name="Tom", age=age):
            print(f"Age: {age}")
        case Person(name=name, age=age):
            print(f"Name: {name}, age: {age}")


print_person(Person("Tom", 37))
print_person(Person("Bob", 37))
print_person(Person("Tom", 26))
print_person(Person("Alice", 19))
print_person(Person(age=45, name="Alice"))

print('---')


def print_person(person):
    match person:
        case Person(name="Tom" | "Tomas" | "Tommy"):
            print("Default person")
        case Person(name=name, age=37):
            print(f"Name: {name}")
        case Person(name="Tom", age=age):
            print(f"Age: {age}")
        case Person(name=name, age=age):
            print(f"Name: {name}, age: {age}")


print_person(Person("Tommy", 45))

print('---')


class Student:
    def __init__(self, name):
        self.name = name


def print_person(person):
    match person:
        case Person(name="Tom" | "Tomas" | "Tommy") | Student(name="Jimmy"):
            print("Default person")
        case Person(name=name) | Student(name=name):
            print(f"Name: {name}")
        case _:
            print("Undefined")


print_person(Person(name="Tom", age=31))
print_person(Student("Jimmy"))
print_person(Student("Alice"))

print('---')


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    __match_args__ = ("name", "age") #Благодаря этому Python будет знать, что при указании атрибутов атрибут name будет идти первым, а атрибут age - вторым.


def print_person(person):
    match person:
        case Person(name, 37):
            print(f"Name: {name}")
        case Person("Tom", age):
            print(f"Age: {age}")
        case _:
            print("Undefined")


print_person(Person("Bob", 37))
print_person(Person("Tom", 22))