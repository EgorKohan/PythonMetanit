with open("hello.txt", "w") as file:
    file.write("Hello World!")

with open("hello.txt", "a") as file:
    file.write("\nGood bye, World!")

with open("hello.txt", "a") as file:
    print("\nHello World (print)!", file=file)

with open("hello.txt", "r") as file:
    for line in file:
        print(line, end="")

print("\n" * 2, end="")

with open("hello.txt", "r") as file:
    str1 = file.readline()
    print(str1, end="")
    str2 = file.readline()
    print(str2, end="")

print("\n" * 2, end="")

with open("hello.txt", "r") as file:
    line = file.readline()
    while line:
        print(line, end="")
        line = file.readline()

print("\n" * 2, end="")

with open("hello.txt", "r") as file:
    text = file.read()
    print(text, end="")

print("\n" * 2, end="")

with open("hello.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line, end="")

print("\n" * 2, end="")

with open("hello.txt", "r", encoding="utf8") as file:
    text = file.read()
    print(text)


print("---\n" * 3, end="")


lines_list = []
for i in range(4):
    line = input(f"Input a row {i + 1}: ")
    lines_list.append(line + "\n")

with open("test.txt", "w") as file:
    for line in lines_list:
        file.write(line)

print("Read messages: ")
with open("test.txt", "r") as file:
    print(file.read())