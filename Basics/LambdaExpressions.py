'''
Лямбда-выражения в языке Python представляют небольшие анонимные функции, которые определяются с помощью оператора
lambda. Формальное определение лямбда-выражения:
lambda [параметры] : инструкция
'''

message = lambda: print("Hello")

message()

square = lambda n: n * n
print(square(5))

sum = lambda a, b: a + b
print(sum(1, 2))

print("---")


def do_operation(a, b, operation):
    print(operation(a, b))


do_operation(11, 2, lambda a, b: a + b)
do_operation(11, 2, lambda a, b: a * b)

print("---")


def select_operation(choice):
    if choice == 1:
        return lambda a, b: a + b
    elif choice == 2:
        return lambda a, b: a - b
    else:
        return lambda a, b: a * b


operation1 = select_operation(1)
print(operation1(10, 20))
operation1 = select_operation(2)
print(operation1(10, 20))
operation1 = select_operation(3)
print(operation1(10, 20))
