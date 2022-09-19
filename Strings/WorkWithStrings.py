message = "Hello World!"
print(message)

name = 'Tom'
print(name)

text = ("asdasd"
        "asd"
        "asdasdasd")
print(text)

text = '''Privet
asd
asd
asasasas
'''

print(text)

text = "Hello"
print(text[2])
print(text[-1], end="\n\n")

for c in text:
        print(c)

print(text[:3])
print(text[2:5])
print(text[3:])
print(text.upper())
print(text.lower())
print(ord(text[2]))
print(len(text))
print("He" in text)