users = {"Tom", "Bob", "Alice", "Tom"}
print(users)

people = ["Mike", "Bill", "Ted"]
users = set(people)
print(users)
print(len(users))

print('---')

users = set()
users.add("Sam")
print(users)

# if remove not existing element then error

if "Sam" in users:
    users.remove("Sam")
    print("Deleted")
else:
    print("Not in set")

print(users)

# discard doesn't generate an error if element doesn't exist

users.discard("Sam")

print(users)

print("---")

users = {"Tom", "Bob", "Alice"}

for user in users:
    print(user)

print("---")

users = {"Tom", "Bob", "Alice"}
students = users.copy()
print(students)

print("---")

users = {"Tom", "Bob", "Alice"}
users2 = {"Sam", "Kate", "Bob"}

union = users.union(users2)
print(union)

users = {"Tom", "Bob", "Alice"}
users2 = {"Sam", "Kate", "Bob"}

print(users.intersection(users2))

users = {"Tom", "Bob", "Alice"}
users2 = {"Sam", "Kate", "Bob"}

difference = users.difference(users2)
print(difference)
print(users - users2)

users = {"Tom", "Bob", "Alice"}
users2 = {"Sam", "Kate", "Bob"}

print(users.symmetric_difference(users2))

print("---")

users = {"Tom", "Bob", "Alice"}
superusers = {"Sam", "Tom", "Bob", "Alice", "Greg"}

print(users.issubset(superusers))
print(superusers.issuperset(users))

print('---')

frozen_users = frozenset({"Tom", "Bob", "Alice"})
'''
В такое множество мы не можем добавить новые элементы, как и удалить из него уже имеющиеся. Собственно поэтому frozen set поддерживает ограниченный набор операций:

len(s): возвращает длину множества

x in s: возвращает True, если элемент x присутствует в множестве s

x not in s: возвращает True, если элемент x отсутствует в множестве s

s.issubset(t): возвращает True, если t содержит множество s

s.issuperset(t): возвращает True, если t содержится в множестве s

s.union(t)

: возвращает объединение множеств s и t
s.intersection(t): возвращает пересечение множеств s и t

s.difference(t): возвращает разность множеств s и t

s.copy(): возвращает копию множества s
'''