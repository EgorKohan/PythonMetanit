class Person:
    pass #Этот оператор применяется, когда синтаксически необходимо определить некоторый код, однако мы не хотим его, и вместо конкретного кода вставляем оператор pass.


tom = Person()
bob = Person()


class Person2:
    def say_hello(self):
        print("Hello")


tom = Person2()
tom.say_hello()


class Person3:
    def say(self, message):
        print(message)


tom = Person3()
tom.say("Hello guys")

print("---")


class Person4:
    def say(self, message):
        print(message)

    def say_hello(self):
        self.say("Hello work")


tom = Person4()
tom.say_hello()

print("---")


class Person5:
    def __init__(self):
        print("Creation of Person5")

    def say_hello(self):
        print("Hello")


tom = Person5()
tom.say_hello()

print("---")


class Person6:
    def __init__(self, name):
        self.name = name
        self.age = 1


tom = Person6("Tom")
print(tom.name)
print(tom.age)
tom.age = 37
print(tom.age)

print("---")


class Person7:
    def __init__(self, name):
        self.name = name
        self.age = 1


tom = Person7("Tom")
# print(tom.company) Invoke an error
tom.company = "Microsoft"
print(tom.company)