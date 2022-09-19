class Person:
    type = "Person"
    description = "Describes a person"


print(Person.type)
print(Person.description)

Person.type = "Class Person"
print(Person.type)

print("---")


class Person:
    type = "Person"

    def __init__(self, name):
        self.name = name


tom = Person("Tom")
bob = Person("Bob")
print(tom.type)
print(bob.type)

Person.type = "Class Person"
print(tom.type)
print(bob.type)

print("---")


class Person:
    default_name = "Undefined"

    def __init__(self, name):
        if name:
            self.name = name
        else:
            self.name = Person.default_name


tom = Person("Tom")
bob = Person("")
print(tom.name)  # Tom
print(bob.name)  # Undefined

print("---")


class Person:
    name = "Undefined"

    def print_name(self):
        print(f"Name: {self.name}")


tom = Person()
bob = Person()
tom.print_name()
bob.print_name()

bob.name = "Bob4ik"
tom.print_name()
bob.print_name()

Person.name = "Abob4ik"
tom.print_name()
bob.print_name()

print("---")


class Person:
    __type = "Person4ik"

    @staticmethod
    def print_type():
        print(f"Type: {Person.__type}")


tom = Person()
Person.print_type()
tom.print_type()