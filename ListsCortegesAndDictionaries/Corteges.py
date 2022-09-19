'''
Кортеж (tuple) представляет последовательность элементов, которая во многом похожа на список за тем исключением,
что кортеж является неизменяемым (immutable) типом. Поэтому мы не можем добавлять или удалять элементы в кортеже,
изменять его.

Для создания кортежа используются круглые скобки, в которые помещаются его значения, разделенные запятыми:
'''

tom = ("Tom", 23)
print(tom)

tom = "Tom", 23
print(tom)

tom = ("Tom",)
print(tom)

data = ["Tom", 37, "Google"]
tom = tuple(data)
print(tom)

tom = ("Tom", 23, "Google")
print(len(tom))

print("---")

tom = ("Tom", 37, "Google", "Software developer")
print(tom[0])
print(tom[1])
print(tom[2])
print(tom[3])
print(tom[-1])

# tom[0] = "Tomas" Error, because cortege is immutable

print("---")

name, age, company, position = ("Tom", 37, "Google", "Software Developer")
print(name)
print(age)
print(company)
print(position)

print("---")

tom = ("Tom", 37, "Google", "Software Developer")

print(tom[1:3])

print(tom[:3])

print(tom[3:])

print("---")

#Особенно удобно использовать кортежи, когда необходимо возвратить из функции сразу несколько значений.
#Когда функция возвращает несколько значений, фактически она возвращает в кортеж:

def get_user():
    name = "Tom"
    age = 22
    company = "Google"
    return name, age, company

user = get_user()
print(user)

print("---")


def print_person(name, age, company):
    print(f"Name: {name}, age: {age}, company: {company}")


tom = "Tom", 22
print_person(*tom, "Microsoft")

bob = ("Bob", 41, "Apple")
print_person(*bob)

print("---")

tom = ("Tom", 22, "Google")
for item in tom:
    print(item)

tom = ("Tom", 22, "Google")

i = 0
while i < len(tom):
    print(tom[i])
    i += 1

print("---")

tom = "Tom", 22
if "Google" in tom:
    print("He works in Google")
else:
    print("Idk where he works")