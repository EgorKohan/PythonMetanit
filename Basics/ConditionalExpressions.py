a = 5
b = 6
result = 5 == 6  # сохраняем результат операции в переменную
print(result)  # False - 5 не равно 6
print(a != b)  # True
print(a > b)  # False - 5 меньше 6
print(a < b)  # True

print("---")

bool1 = True
bool2 = False
print(bool1 == bool2)  # False - bool1 не равно bool2

print("---")


num1 = '1'
num2 = 1
print(type(num1))
print(type(num2))
print(num1 == num2)

isMarried = True
isDivorced = False

print("---")

print(isMarried and isDivorced)
print(isMarried or isDivorced)
print(not isMarried)

print("---")

str1 = "Hello"
str2 = "llo"
str3 = "ZigZag"
print(str2 in str1)
print(str3 in str1)
print(str3 not in str1)
