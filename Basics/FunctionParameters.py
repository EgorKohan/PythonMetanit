def say_hello(name):
    print(f"Hello, {name}")


say_hello("Tom")
say_hello("Bob")
say_hello("Alice")

print("---")


def print_person(name, age):
    print(f"Name: {name}")
    print(f"Age: {age}")


print_person("Egor", 21)

print("---")


def say_hello(name="Tom"):
    print(f"Hello, {name}")


say_hello()


def print_person(name, age=18):
    print(f"Name: {name}, age: {age}")


print("Egor")

print("---")

print_person(age=21, name="Egor")

print("---")

'''
Символ * позволяет установить, какие параметры будут именнованными - то есть такие параметры, которым можно
передать значения только по имени. Все параметры, которые располагаются справа от символа *, получают значения 
только по имени.
Можно сделать все параметры именнованными, поставив перед списком параметров символ *.
'''


def print_person(name, *, age, company):
    print(f"Name: {name}, age: {age}, company: {company}")


print_person("Egor", age=21, company="Netcracker")


def print_person(*, name, age, company):
    print(f"Name: {name}, age: {age}, company: {company}")


print_person(name="Egor", age=21, company="Netcracker")

print("---")

'''
Если наоборот надо определить параметры, которым можно передавать значения только по позиции, то есть позиционные
 параметры, то можно использовать символ /: все параметры, которые идут до символа / , являются позиционными 
 и могут получать значения только по позиции
 '''


def print_person(name, age, company, /):
    print(f"Name: {name}, age: {age}, company: {company}")


print_person("Egor", 21, "Netcracker")

print("---")

'''
Неопределенное количество параметров
С помощью символа звездочки можно определить параметр, через который можно передавать 
неопределенное количество значений. Это может быть полезно, когда мы хотим, чтобы функция 
получала несколько значений, но мы точно не знаем, сколько именно. Например, определим функцию подсчета суммы чисел:
'''


def sum(*numbers):
    result = 0
    for i in numbers:
        result += i
    print(f"Sum = {result}")


sum(1, 2, 3, 4, 5)
sum(11, 2, 32, 4, 5)
# sum(11, 2, '21', 4.5, 5, True)

