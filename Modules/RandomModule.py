import random

number = random.random()
print(number)
number = random.random() * 100
print(number)

number = random.randint(20, 35)
print(number)

number = random.randrange(10)
print(number)
number = random.randrange(10, 12)
print(number)
number = random.randrange(5, 40, 7)
print(number)

numbers = list(range(1, 10))
random.shuffle(numbers)
choice = random.choice(numbers)

print(choice)