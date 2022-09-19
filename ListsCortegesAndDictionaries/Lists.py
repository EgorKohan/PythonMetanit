numbers = [1, 2, 3, 4, 5]

people = ["Tom", "Sam", "Bob"]

numbers1 = []
numbers2 = list()

objects = [1, 2.6, "Hello", True]

numbers3 = [1, 2, 3, 4, 5]
numbers4 = list(numbers3)
print(numbers4)

print("---")

letters = list("Hello")
print(letters)

print("---")

numbers5 = [5] * 6
print(numbers5)

print("---")

people2 = ["Tom"] * 3
print(people2)

print("---")

students = ["Sam", "Bob"] * 4
print(students)

print("---")

people = ["Tom", "Sam", "Bob"]
print(people[0])
print(people[1])
print(people[2])
print(people[-1])
print(people[-2])
print(people[-3])

print("---")

people = ["Tom", "Sam", "Bob"]
print(people)
print(people[0])
people[0] = "Tomas"
print(people)
print(people[0])

print("---")

people = ["Tom", "Sam", "Bob"]
tom, sam, bob = people
print(tom)
print(sam)
print(bob)

# В данном случае переменным tom, bob и sam последовательно присваиваются элементы из списка people. \
# Однако следует учитывать, что количество переменных должно быть равно числу элементов присваиваемого списка.

print("---")

people = ["Tom", "Sam", "Bob"]
for person in people:
    print(f"Person: {person}")

i = 0
while i < len(people):
    print(people[i])
    i += 1

print("---")

numbers1 = [1, 2, 3, 4, 5]
numbers2 = list([1, 2, 3, 4, 5])
if numbers1 == numbers2:
    print("numbers1 equal to numbers2")
else:
    print("numbers1 is not equal to numbers2")

print("---")

'''
Для управления элементами списки имеют целый ряд методов. Некоторые из них:

append(item): добавляет элемент item в конец списка

insert(index, item): добавляет элемент item в список по индексу index

extend(items): добавляет набор элементов items в конец списка

remove(item): удаляет элемент item. Удаляется только первое вхождение элемента. Если элемент не найден, генерирует исключение ValueError

clear(): удаление всех элементов из списка

index(item): возвращает индекс элемента item. Если элемент не найден, генерирует исключение ValueError

pop([index]): удаляет и возвращает элемент по индексу index. Если индекс не передан, то просто удаляет последний элемент.

count(item): возвращает количество вхождений элемента item в список

sort([key]): сортирует элементы. По умолчанию сортирует по возрастанию. Но с помощью параметра key мы можем передать функцию сортировки.

reverse(): расставляет все элементы в списке в обратном порядке

copy(): копирует список

Кроме того, Python предоставляет ряд встроенных функций для работы со списками:

len(list): возвращает длину списка

sorted(list, [key]): возвращает отсортированный список

min(list): возвращает наименьший элемент списка

max(list): возвращает наибольший элемент списка
'''

people = ["Tom", "Bob"]
people.append("Alice")
people.insert(1, "Bill")
people.extend(["Mike", "Sam"])
index_of_tom = people.index("Tom")
removed_item = people.pop(index_of_tom)
last_item = people.pop()
people.remove("Alice")
print(people)
people.clear()

print("---")

# Если определенный элемент не найден, то методы remove и index генерируют исключение.
# Чтобы избежать подобной ситуации, перед операцией с элементом можно проверять его наличие с помощью ключевого слова in:

people = ["Tom", "Bob", "Alice", "Sam"]

if "Alice" in people:
    people.remove("Alice")
print(people)

print("---")

people = ["Tom", "Bob", "Alice", "Sam", "Bill", "Kate", "Mike"]

del people[1]
print(people)
del people[:3]
print(people)
del people[1:]
print(people)

print("---")

people = ["Tom", "Bob", "Alice", "Tom", "Bill", "Tom"]
people_count = people.count("Tom")
print(people_count)

print("---")

# Sorting

people = ["Tom", "Bob", "Alice", "Sam", "Bill"]
people.sort()
people.reverse()
print(people)

people = ["Tom", "bob", "alice", "Sam", "Bill"]
people.sort()
print(people)

people.sort(key=str.lower)
print(people)

people = ["Tom", "bob", "alice", "Sam", "Bill"]
sorted_people = sorted(people, key=str.lower)
print(people)
print(sorted_people)

print("---")

numbers = [9, 21, 12, 1, 3, 15, 18]
print(max(numbers))
print(min(numbers))

print("---")

people1 = ["Tom", "Bob", "Alice"]
people2 = people1
people2.append("Sam")
print(people1)
print(people2)

people1 = ["Tom", "Bob", "Alice"]
people2 = people1.copy()
people2.append("Sam")
print(people1)
print(people2)

print("---")

people = ["Tom", "Bob", "Alice", "Sam", "Tim", "Bill"]

slice_people1 = people[:3]
print(slice_people1)

slice_people2 = people[1:3]
print(slice_people2)

slice_people3 = people[1:5:2]
print(slice_people3)

print("---")

people1 = ["Tom", "Bob", "Alice"]
people2 = ["Tom", "Sam", "Tim", "Bill"]
people3 = people1 + people2
print(people3)   # ["Tom", "Bob", "Alice", "Tom", "Sam", "Tim", "Bill"]

print("---")

people = [
    ["Tom", 29],
    ["Alice", 33],
    ["Bob", 27]
]

print(people[0])
print(people[0][0])
print(people[0][1])

for person in people:
    print(person)