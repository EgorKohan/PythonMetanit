a = 2
b = 2.5
c = a + b
print(c)

print("---")

'''
int(): преобразует значение в целое число

float(): преобразует значение в число с плавающей точкой

str(): преобразует значение в строку
'''

a = "2"
b = 3
# c = a + b Error
c = int(a) + b
print(c)

age = 22
message = "Age: " + str(age)
print(message)