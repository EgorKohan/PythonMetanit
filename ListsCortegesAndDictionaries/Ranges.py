print(range(5))
print(range(1, 5))
print(range(2, 10, 2))
print(range(10, 2, -2))

print("---")

for i in range(5):
    print(i, end=" ")

print("---")

for i in range(1, 10):
    for j in range(1, 10):
        print(i * j, end="\t")
    print("\n")

print("---")

numbers = list(range(10))
print(numbers)

numbers = list(range(2, 10))
print(numbers)

numbers = list(range(10, 2, -2))
print(numbers)