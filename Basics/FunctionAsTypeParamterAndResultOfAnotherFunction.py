def say_hello(): print("Hello")


def say_goodbye(): print("Good bye")


message = say_hello
message()
message = say_goodbye
message()


def sum(a, b): return a + b


def multiply(a, b): return a * b


operation = sum
result = operation(5, 6)
print(result)

operation = multiply
print(operation(5, 6))

print("---")


def do_operation(a, b, operation):
    result = operation(a, b)
    print(f"result = {result}")


def sum(a, b): return a + b


def multiply(a, b): return a * b


do_operation(5, 4, sum)
do_operation(5, 4, multiply)

print("---")


def subtract(a, b): return a - b


def select_operation(choice):
    if choice == 1:
        return sum
    elif choice == 2:
        return subtract
    else:
        return multiply


operation = select_operation(1)
print(operation(10, 6))

operation = select_operation(2)
print(operation(10, 6))

operation = select_operation(3)
print(operation(10, 6))


