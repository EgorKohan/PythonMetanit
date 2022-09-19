def print_person(person):
    match person:
        case "Tom" | "Tomas" | "Tommy" as name:
            print(f"Name: {name}")
        case _:
            print("Undefined")


print_person("Tom")
print_person("Tomas")
print_person("Bob")

print('---')


def print_person(person):
    match person:
        case ("Tom" | "Tomas" as name, 37 | 38 as age):
            print(f"Name: {name}, age: {age}")
        case ("Tom" | "Bob", _) as pers:
            print(f"Name: {pers[0]}, age: {pers[1]}")


print_person(("Tom", 37))
print_person(("Bob", 45))

print('---')


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    __match_args__ = ("name", "age")

    def __str__(self):
        return f"Name: {self.name}, age: {self.age}"


def print_family(family):
    match family:
        # case(Person() as husband, Person() as wife):
        #     print(f"Husband: {husband}. Wife: {wife}")
        case(first, second):
            print(f"First: {first}, second: {second}")
        case _:
            print("Undefined")


print_family((Person("Tom", 33), Person("Alice", 32)))
