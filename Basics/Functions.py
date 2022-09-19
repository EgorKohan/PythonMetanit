def sayHello():
    print("Hello")

print("Bye")

sayHello()
sayHello()
sayHello()

def sayHello2(): print("Hello2")

print("---")

def sayHello(): print("Hello")
def sayBye(): print("Bye")

sayHello()
sayBye()

print("---")

'''
Локальные функции
Одни функции могут определяться внутри других функций - внутренние функции еще называют локальными. 
Локальные функции можно использовать только внутри той функции, в которой они определены. Например:
'''


def print_messages():
    def say_hello3(): print("Hello")
    def say_bye3(): print("Bye")
    say_hello3()
    say_hello3()


print_messages()

print("---")


'''
Организация программы и функция main
В программе может быть определено множество функций. И чтобы всех их упорядочить, одним из способов их 
организации является добавление специальной функции (обычно называется main), в которой потом уже вызываются другие функции:
'''


def main():
    say_hello()
    say_goodbye()


def say_hello():
    print("Hello")


def say_goodbye():
    print("Good Bye")


# Вызов функции main
main()