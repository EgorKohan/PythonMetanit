class Person:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def display_info(self):
        print(f"Name: {self.__name}")


class Employee(Person):
    def work(self):
        print(f"{self.name} is working")


tom = Employee("Tom")
tom.work()
tom.display_info()

print("---")


#  класс работника
class Employee:
    def work(self):
        print("Employee works")


#  класс студента
class Student:
    def study(self):
        print("Student studies")


class WorkingStudent(Employee, Student):  # Наследование от классов Employee и Student
    pass


tom = WorkingStudent()
tom.work()
tom.study()

print("---")


class Person2:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def display_info(self):
        print(f"Name: {self.__name}")


class Employee2(Person2):
    def __init__(self, name, company):
        super().__init__(name)
        self.__company = company

    @property
    def company(self):
        return self.__company

    def display_info(self):
        print(f"Name: {self.name}, company: {self.company}")

    def work(self):
        print(f"{self.name} is working")


tom = Employee2("Tom", "Microsoft")
tom.work()
tom.display_info()

print("---")


class Person3:

    def __init__(self, name):
        self.__name = name  # имя человека

    @property
    def name(self):
        return self.__name

    def do_nothing(self):
        print(f"{self.name} does nothing")


#  класс работника
class Employee3(Person3):

    def work(self):
        print(f"{self.name} works")


#  класс студента
class Student3(Person3):

    def study(self):
        print(f"{self.name} studies")


def act(person):
    if isinstance(person, Student3):
        person.study()
    elif isinstance(person, Employee3):
        person.work()
    elif isinstance(person, Person3):
        person.do_nothing()


tom = Employee3("Tom")
bob = Student3("Bob")
sam = Person3("Sam")

act(tom)
act(bob)
act(sam)