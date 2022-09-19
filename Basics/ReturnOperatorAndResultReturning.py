def get_message():
    return "Hello METANIT.COM"


message = get_message()
print(message)

print(get_message())


def double(number):
    return number * 2


print(double(4))


def print_person(name, age):
    if age > 120 or age < 1:
        print("Invalid age")
        return
    print(f"Name: {name}  Age: {age}")


print_person("Tom", 22)
print_person("Bob", -102)