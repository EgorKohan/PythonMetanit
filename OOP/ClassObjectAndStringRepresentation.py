class Person:
    def __init__(self, name, age):
        self.name = name  # устанавливаем имя
        self.age = age  # устанавливаем возраст

    def display_info(self):
        print(f"Name: {self.name}  Age: {self.age}")

    def __str__(self):
        return f"Name: {self.name}, age: {self.age}"


tom = Person("Tom", 23)
print(tom)