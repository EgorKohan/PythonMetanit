'''
Guard или ограничения шаблонов позволяют установить дополнительные условия, которым должно соответсвовать выражение.
 Ограничение задается сразу после шаблона с помощью ключевого слова if, после которого идет условие ограничения:
'''


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def enter(person):
    match person:
        case Person(name=name, age=age) if age < 18:
            print(f"name: {name}, access is denied")
        case Person(name=name):
            print(f"Name: {name}, access is granted")


enter(Person("Tom", 16))
enter(Person("Bob", 22))

print('---')


def check_data(data):
    match data:
        case name, age if name == "admin" or age not in range(1, 101):
            print("Invalid data")
        case name, age:
            print(f"Data is correct. Name: {name}, age: {age}")


check_data(("admin", 10))
check_data(("Tom", 120))
check_data(("Tom", 22))