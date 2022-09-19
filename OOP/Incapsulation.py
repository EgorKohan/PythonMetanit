class Person:
    def __init__(self, name):
        self.name = name
        self.age = 1

    def display_info(self):
        print(f"Name: {self.name}, age: {self.age}")


tom = Person("Tom")
tom.name = "Spider-Man"
tom.age = -102
tom.display_info()

print("---")


class Person1:
    def __init__(self, name):
        self.__name = name
        self.__age = 1

    def set_age(self, age):
        if 1 < age < 110:
            self.__age = age
        else:
            print("Incorrect age")

    def get_age(self):
        return self.__age

    def get_name(self):
        return self.__name

    def display_info(self):
        print(f"Name: {self.__name}, age: {self.__age}")


tom = Person1("Tom")
print(tom.get_age())
tom.set_age(15)
print(tom.get_age())
tom.set_age(150)
print(tom.get_age())

print("---")


class Person2:
    def __init__(self, name):
        self.__name = name
        self.__age = 1

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if 1 < age < 110:
            self.__age = age
        else:
            print("Incorrect age")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    def display_info(self):
        print(f"Person2. Name: {self.__name}, age: {self.__age}")


tom = Person2("Tom2")
print(tom.age)
tom.age = 120
print(tom.age)
tom.age = 80
print(tom.age)

print(tom.name)
tom.name = "Patrick"
print(tom.name)