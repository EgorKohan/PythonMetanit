text = "Hello, {first_name}.".format(first_name="Tom")
print(text)

info = "Name: {name}\tAge: {age}.".format(name="Bob", age=23)
print(info)

text = "Name: {0}\tAge: {1}.".format("Bob", 23)
print(text)

text = "Hello, {0} {0} {0}".format("Tom")
print(text)

'''
s: для вставки строк

d: для вставки целых чисел

f: для вставки дробных чисел. Для этого типа также можно определить через точку количество знаков в дробной части.

%: умножает значение на 100 и добавляет знак процента

e: выводит число в экспоненциальной записи

{:[количество_символов][запятая][.число_знаков_в_дробной_части] плейсхолдер}
'''

source = "{:d} symbols"
number = 5
target = source.format(number)
print(target)

print("{:,d} symbols (2)".format(1500))
print("{:.5f} symbols (3)".format(12.123123))

n1 = 23.8589578
print(f"{n1:10.2f}")
n2 = 25
print(f"{n2:8d}")

number = .12345
print("{:%}".format(number))
print("{:.0%}".format(number))
print("{:.1%}".format(number))

print(f"{number:%}")
print(f"{number:.0%}")
print(f"{number:.1%}")

info = "Name: %s, age: %d" % ("Tom", 35)
print(info)