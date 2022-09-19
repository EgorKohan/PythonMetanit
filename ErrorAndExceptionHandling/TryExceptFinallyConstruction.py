try:
    message = int(input("Input a number: "))
    print(f"Inputted number: {message}")
except (ZeroDivisionError, ValueError) as e:
    print(f"Error: {e}")
    print("Incorrect number!")
finally:
    print("End")

print("---")

try:
    number1 = int(input("Input a first number "))
    number2 = int(input("Input a second number"))
    if number2 == 0:
        raise Exception("Second number cannot be 0")
    print("Result of dividing ", number1 / number2)
except ValueError:
    print("Incorrect data")
except Exception as e:
    print(e)
print("End")

print("---")


class PersonAgeException(Exception):
    def __init__(self, age, minage, maxage):
        self.age = age
        self.minage = minage
        self.maxage = maxage

    def __str__(self):
        return f"Incorrect value {self.age}. It should be between {self.minage} and {self.maxage}"


class Person:
    def __init__(self, name, age):
        self.__name = name
        minage, maxage = 1, 110
        if minage < age < maxage:
            self.__age = age
        else:
            raise PersonAgeException(age, minage, maxage)

    def __str__(self):
        return f"Name: {self.__name}, age: {self.__age}"


try:
    tom = Person(age=10, name="Tom")
    print(tom)
    bob = Person(age=1000, name="Bob")
    print(bob)
except PersonAgeException as e:
    print(f"Incorrect person age: {e}")