name = "Tom"


def say_hi():
    print(f"Hello, {name}")


def say_bye():
    print(f"Good bye, {name}")


say_hi()
say_bye()

print("---")


def say_hi():
    name = "Sam"
    surname = "Johnson"
    print("Hello", name, surname)


def say_bye():
    name = "Tom"
    print("Good bye", name)


say_hi()
say_bye()

print("---")

# Если же мы хотим изменить в локальной функции глобальную переменную, а не определить локальную, то необходимо использовать ключевое слово global:


def say_hi():
    global name
    name = "Sam"
    surname = "Johnson"
    print("Hello", name, surname)


def say_bye():
    print("Good bye", name)

say_hi()
say_bye()

print("---")

'''
Выражение nonlocal прикрепляет идентификатор к переменной из ближайщего окружающего контекста 
(за исключением глобального контекста). Обычно nonlocal применяется во вложенных функциях, когда 
надо прикрепить идентификатор 
за переменной или параметром окружающей внешней функции. Рассмотрим ситуацию, где это выражение может пригодиться:
'''


def outer():
    n = 5

    def inner():
        print(n)

    inner()
    print(n)


outer()


def outer():
    n = 5

    def inner():
        nonlocal n  # указываем, что n - это переменная из окружающей функции
        n = 25
        print(n)

    inner()
    print(n)


outer()